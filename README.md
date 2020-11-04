# EC 601 Project 2 - Tweet Analysis

Tweet anaylsis using Tweepy API and Google Nautral Language sentiment analysis

## Setup

To begin working with this project, you must have developers accounts for the Twitter API as well as Google Cloud Services. You will need to import you own API credentials into the project to authenticate with both serivces.

## Tests

The primary test/user case is with in the "project_main" file. This test allows users to enter any Twitter user's handle and extract a certain number of their past tweets to analyze their sentiment. Additionaly, a user can compare the sentiment of the most recent tweets of two Twitter accouts to see how positive or negative they are.

The secondary test that can be run in this document is to stream tweets based of certain hashtags or text.

Lastly, a user is able to compare the sentiment of two accounts and their most recents tweets. The program will output both tweets and their sentiment and display which is more positive.

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

## Issues

- Unable to extract "full_text" tweets from JSON
