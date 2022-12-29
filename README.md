# TIC - Toxic Internet Communities

An Analysis on Toxic Internet Communities

## Introduction

The proliferation of “toxic” behavior online has always been an issue, but with recent public discourse on a variety of topics ranging from politics, gaming, and so on, people online are more comfortable than ever to exhibit these behaviors. It is an issue, not only because it can be emotionally distressing, but also because it encourages behaviors that can lead to radicalization. Whether politically motivated, or sparked by uncontrolled anger, radicalization has become a more serious problem in the United States with the January 6th insurrection that occurred in 2021. It is an issue that must be examined further to see what root causes are, as well as how communities can connect to further advance radicalization without realizing it. This is a thought experiment on how toxic communities interact with each other.

Though this project does not claim to offer a clear solution to the problem, it explores these ideas and how they can proliferate, and offers an opportunity to explore multiple communities who have the potential to go down this route. It encourages future work to involve looking into the metrics further, to better realize how we can construct an online space that utilizes free speech, yet also monitors for potential dangers along the way.

A toxic person is someone who uses language to emotionally manipulate and distress others. These metrics can be quantified, and according to Google’s Perspective API, there are a few main categories that can be explored. These categories include: INSULT, PROFANITY, THREAT, SEXUALLY EXPLICIT, FLIRTATION, ATTACK ON AUTHOR, ATTACK ON COMMENTER, INCOHERENT, INFLAMMATORY, and OBSCENE. These metrics are the basic building blocks of what toxic behavior is made of. This project explores these metrics in further detail when comparing different communities. 

Though we can recognize these behaviors as they are happening within a community, this project explores how we can detect these issues in realtime and find parallels between different communities of people. Different communities can be toxic in different ways, and it is more of a thought experiment to explore how these communities differ when it comes to toxic behavior. This project analyzes these communities by firstly grabbing a sample of posts in the communities, preprocessing the data by removing noise, running a sentiment analysis algorithm on text to determine its toxicity level, clustering communities together, and finally analyzing distances between communities using average metrics.

## Overview

### About the Dataset

The dataset was created by the program. The user can query from Twitter, the query would be the community that they are collecting data from. This data is then stored in the SQLite database, unfiltered and uncleaned. The next steps would be to then clean it, and finally analyze it.

#### Data Generation

Using Twitter’s API, posts within communities will be gathered to further analyze. This will be done by using terms the community is known by to look up posts within them. For example, the gaming community will have the queries “gaming, gamer, gamers” and so on.
The same amount of data will be requested from each community. Communities that will be examined and their keywords include:

| Gaming | Politics     | Youtube   | Stem        |
| ------ | --------     | --------- | ----------- |
| Gaming | Politics     | YouTube   | Science     |
| Gamer  | Donald Trump | YouTubers | Technology  | 
| Gamers | Joe Biden    |           | Engineering |
|        |              |           | Math        |

This is to cover a large area of people who may or may not intersect in communities. Once data is gathered, it will be stored in the database as is, alongside the post ID that Twitter provides. Due to the time constraint of the project, only a small number of communities will be examined, though the breadth of each community should be enough to generate meaningful results for each community listed above.

### Preprocessing

Preprocessing
Data from Twitter is littered with noise, so data cleaning must take place. Removal of Twitter features such as retweets, hashtags, mentions, urls, and so on are required for good data to be passed through the sentiment analysis algorithm. This, alongside awkward spaces and punctuation will also be removed. The end goal of the preprocessing step is to have a sentence that one could find in a book or article.

Data will also be clustered under multiple constraints:

- Which community it is a part of
- Similar distance measures
- Similar topics talked about

This is with the end goal of comparing different clusters to see if there are any ways to “bridge” them together.

### Analysis

When analyzing this cleaned data, the main goal was to find how different communities compared to each other using the different toxicity metrics provided by Google’s Perspective API. This process can be broken down into smaller steps:

**Cluster the Data -> Find Representatives of Clusters -> Find Distances Between Clusters**

When examining the data, it naturally falls into clusters already. These clusters are the communities that each post is from. Each post has 4 distinct metrics when run through the Perspective API. These metrics include: toxicity, insult, threat, sexually explicit. With this in mind, we can then find representatives of each cluster to use to find distances between clusters.

When finding representatives of each cluster, there were two algorithms thought to use. K-Means and K-Medoids. The program uses the K-Medoids algorithm due to its efficiency and nature to decrease dissimilarity between points within the cluster, as well as not being as sensitive to outliers. The program uses scikit-learn’s K-Medoids algorithm to achieve this. Once a representative is found, it acts as the anchor point for all other clusters to base their distance measures off of.

## Experimental Setup

### Dataset

The dataset was created by the program. The user can query from Twitter, the query would be the community that they are collecting data from. This data is then stored in the SQLite database, unfiltered and uncleaned. The next steps would be to then clean it, and finally analyze it.

### Platform

The program is a Python program. A command line interface is run, where the user can query for data, clean data, and finally analyze the data. This was all created by Shannon Thornton, and used as the sole program for the project. The main libraries used for analysis were numpy and scikit-learn, each are popular libraries used for machine learning and statistical analysis like what was done for this project. Visualizations were made using matplotlib.

### Tools Used

A command line interface was created for facilitating the process. This CLI allows users to generate data from Twitter, clean the data, and run analysis algorithms on the data to generate CSV files and diagrams. To achieve this, the following tools were used:

- Python
  - The programming language used
  - Allows for a wide array of libraries
  - Easy to construct scripts for
- SQLite
  - Data storage
  - Portable and lightweight
- Twitter API
  - To query data from
- Google’s Perspective API
  - Used to analyze pieces of text for its “toxicity” level
- Numpy
  - Used for general analysis and number crunching
- Scikit-Learn
  - Used for statistical analysis


## Results
