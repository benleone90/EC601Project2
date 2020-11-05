# EC 601 Project 2 - Tweet Analysis

Tweet anaylsis of user input Twitter handles using Tweepy API and Google Nautral Language Processing to determint the tweet's sentiment score.

## Setup

To begin working with this project and analyzing tweets, you must have developers accounts for both the Twitter API and Google Cloud Services. You will need to import you own API credentials into the project to authenticate with both serivces.

## Featured Uses

The primary test/user case is with in the [Project Main](https://github.com/benleone90/EC601_Project2/blob/master/EC601_Project_Main.py) file. This test allows users to enter any Twitter user's handle and extract a certain number of their past tweets to analyze their sentiment.

Additionaly, a user can compare the sentiment of the most recent tweets of two Twitter accouts to see how positive or negative they are.

## Tweet Analyzer MVP

The minimum viable product of this project is to be able to accept user inputs for Twitter handles and have the Tweepy API query Twitter to recieve the correct number of tweets requested. The program must then pass these tweets to the Google Natual Language Processing API and return the sentiment and magnitude of what was sent.

## Potential Users

- Student who wants to analyze a user's Twitter feed sentiment
- Journalists who want to see if VIPs are using their influence for postitive or negative outcomes
- Researchers to track sentiment over time

## User Stories

- A user would like to see if tweets I am seeing daily are positive or negative.
- A user wants to evaluate if the sentiment of a tweet impacts their feelings on an issue/group/person.
- A user wants to see if people are reacting more positively or negatively to unfolding events.

## Unit Tests

Unit tests for this project were to ensure the the list of tweets was empty before the program appened each tweet into the list

## Issues

- ~~9/27/2020 Unable to extract "full_text" tweets from JSON~~
  - Issue resoved after implementing `tweet_mode='extended'` parameter into the Tweepy API
