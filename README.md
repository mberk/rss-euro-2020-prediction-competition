# Welcome to the RSS Euro 2020 Prediction Competition!

## Rules

1. The goal of the competition is to make probabilistic predictions of the outcome of every game in the Euro 2020 tournament
2. Entrants are free to use any data they wish, _provided it is publicly available_. This includes data scraped from public websites
3. Predictions are to be made for all group games and _every possible_ knockout game
4. Submissions must be made before kick-off of the first game, 20:00 BST on 11th June 2021
5. Code and data (or links to the data if the data sets are large) used to generate the predictions must be included in a submission so that the judging panel can reproduce the results
6. Participants are free to enter either as individuals or as teams
7. Entrants may update their predictions at any point before the start of the tournament by submitting a new entry but only the most recent submission will be scored
8. The two entries with the best log-score ([see Scoring below](#scoring)) will win a prize ([see Prizes below](#prizes)) along with a third entry chosen by the judging panel based on the methodology used

## Scoring

* Entries will be scored according to the log-score
* Each group stage game will receive the score:
```
-(log(p_team1_win)*I(team1_win) + log(p_draw)*I(draw) + log(p_team2_win)I(team2_win))
```
where  `I(.)` is the indicator function and e.g. `p_team1_win` is the entrant's estimate of the probability that team 1 wins the match
* For knockout games, the outcome is based on the score after extra-time/penalties if relevant and the contribution is:
```
-(log(p_team1_win)*I(team1_win) + log(p_team2_win)*I(team2_win))
```
* The individual scores for all games that actually take place will be summed to provide an overall score for the entry
* The lower the score, the better (note the minus signs!)

## Prizes

* All winners will be invited to present their work at the 2021 RSS conference with reasonable expenses paid
* All winners will receive an appropriately tacky trophy!

## Making a Submission

* An example submission file can be found here: [submission-template.csv](submission-template.csv)
* Entrants should email a zip file to statisticsinsport@rss.org.uk that contains the submission file along with the code and data used to generate it
* If the zip file exceeds 10 megabytes then please do not submit the data but instead clearly comment the code with what data was used and where it can be obtained from. If the submission relies on scraped data and this is too large to be included then the scraping code must be included instead
* When making a submission please indicate whether entering as a team or individual and your name or team name and team members' names as appropriate

## Getting Started

To help you get started, we have added [an IPython Notebook](Euro%202020%20Predictions%20-%20Getting%20Started.ipynb) that describes fitting a model to a publicly available data set and producing some predictions in the correct format

## Questions?

Any questions can be emailed to statisticsinsport@rss.org.uk or asked by creating a GitHub issue

## Coming Soon

* Live leaderboard

## Suggested Resources

### StatsBomb Free Data

* Available here: https://github.com/statsbomb/open-data
* This is a very detailed data set. The following description is taken from their website:
  * Location of players on the pitch in any shot, including the position and actions of the Goalkeeper 
  * Detailed information on ALL players applying defensive pressure on a player in possession – including how long the pressure lasted 
  * Which foot a player passes with, and many more minor enhancements 
* This free data mainly consists of matches from La Liga and various women's competitions but most relevantly contains data from the men’s 2018 World Cup

### [football-data.co.uk](football-data.co.uk)

* This is a seminal data source for club level data
* It’s fairly basic but comprehensive and continually updated

### Kaggle data set “European Soccer Database”

* Available here: https://www.kaggle.com/hugomathien/soccer
* Data set includes:
  * +25,000 matches
  * +10,000 players 
  * 11 European Countries with their lead championship 
  * Seasons 2008 to 2016 
  * Players and Teams' attributes* sourced from EA Sports' FIFA video game series, including the weekly updates 
  * Team line up with squad formation (X, Y coordinates) 
  * Betting odds from up to 10 providers 
  * Detailed match events (goal types, possession, corner, cross, fouls, cards etc…) for +10,000 matches 
* This is the highest rated relevant data set on Kaggle but only goes up to 2016

### Kaggle data set “International football results from 1872 to 2020”

* Available here: https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017
* This is basic data – just results, the tournament and the location – but highly relevant and covers an impressive time range

### Kaggle data set “FIFA 19 complete player dataset”

* Available here: https://www.kaggle.com/karangadiya/fifa19
* This data set contains player ratings from the video game FIFA 19
* Despite the unusual source, this is a very detailed data set of 18,000+ players with 90+ attributes
