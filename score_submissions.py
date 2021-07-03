import argparse
import os

import numpy as np
import pandas as pd


def anonymise_name(name: str) -> str:
    return ''.join(c for c in name if c.isupper())


def score_submissions(path_to_submissions_file: str, path_to_match_results_file: str) -> pd.DataFrame:
    match_results = pd.read_csv(path_to_match_results_file)
    mirrored_match_results = pd.DataFrame(
        {
            'team1_name': match_results['team2_name'],
            'team2_name': match_results['team1_name'],
            'Group': match_results['Group'],
            'team1_win': match_results['team2_win'],
            'draw': match_results['draw'],
            'team2_win': match_results['team1_win']
        }
    )
    submissions = pd.read_excel(path_to_submissions_file, sheet_name=None, engine='openpyxl')

    scores = []
    for name, submission in submissions.items():
        if name.startswith('!'):
            # Ignore malformed submission for now
            continue
        df = pd.concat(
            [
                match_results.merge(submission, on=['team1_name', 'team2_name', 'Group']),
                mirrored_match_results.merge(submission, on=['team1_name', 'team2_name', 'Group'])
            ]
        )
        assert len(df) == len(match_results)
        # Handle probabilities of 0
        df.loc[df['p_team1_win'] == 0, 'p_team1_win'] = 1e-12
        df.loc[df['p_team2_win'] == 0, 'p_team2_win'] = 1e-12
        df.loc[(df['p_draw'] == 0) & (df['Group'] != 'Knockout'), 'p_draw'] = 1e-12
        # Normalise probabilities
        df.loc[df['Group'] == 'Knockout', 'p_draw'] = 0
        df['p_team1_win'] = df['p_team1_win'] / df[['p_team1_win', 'p_team2_win', 'p_draw']].sum(axis=1)
        df['p_team2_win'] = df['p_team2_win'] / df[['p_team1_win', 'p_team2_win', 'p_draw']].sum(axis=1)
        df['p_draw'] = df['p_draw'] / df[['p_team1_win', 'p_team2_win', 'p_draw']].sum(axis=1)
        df_group = df[df['Group'] != 'Knockout']
        df_ko = df[df['Group'] == 'Knockout']
        score = -(np.log(df_group['p_team1_win']) * df_group['team1_win'] + np.log(df_group['p_draw']) * df_group['draw'] + np.log(df_group['p_team2_win']) * df_group['team2_win']).sum()
        score += -(np.log(df_ko['p_team1_win']) * df_ko['team1_win'] + np.log(df_ko['p_team2_win']) * df_ko['team2_win']).sum()
        scores.append({'submission': anonymise_name(name), 'score': score})

    scores = pd.DataFrame(scores).sort_values(['score'])
    return scores


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--submissions-file',required=True)
    parser.add_argument('--match-results-file', required=True)
    parser.add_argument('--output-file', required=True)

    args = parser.parse_args()

    results = score_submissions(args.submissions_file, args.match_results_file)
    results.to_csv(args.output_file, index=False)


if __name__ == '__main__':
    main()

