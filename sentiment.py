#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 12:13:10 2023

@author: giannidiarbi

 Gianni Diarbi
 DS2000
 Spring 2023
 HW 6 Problem 1
 sentiment.py
 
"""

REDDIT_FILE = "reddit.txt"

import matplotlib.pyplot as plt

SENT_WORDS = {"value" : .5, "happy" : .6, "enjoy" : .75, "good" : .5, 
              "great" : .8, "best" : .75, "fulfilling" : .75, "unique" : .5,
              "lucky" : .25, "advantage" : .75, "experience" : .25,
              "lenient" : .25, "loved" : 1, "love" : .5, "cool" : .25, 
              "appreciate" : .25, "claims" : -.25, "unlucky" : -.25, 
              "expensive" : -1, "bad" : -.5, "hated" : -1, "hard" : -.2,
              "never" : -.1, "cold" : -.3,"depressed" : -.75, "upset" : -.25, 
              "problem" : -.25, "transfers" : .3, "gross" : -.1, 
              "dislike" : -.4, "failed" : -.5, "failing" : -.25, 
              "transfer" : -1, "stressful" : -.4, "trouble" : -.5, 
              "miserable" : -1, "regretted" : -.75, "problematic" : -.5, 
              "too": -.5, "require" : -.1, "sucks" : -.5, "nowhere" : -.25}

def read_file(filename):
    ''' Function: read_file
        Parameter: String, the filename
        Returns: Lowercase, stripped 1d list of strings 
        Does: Reads in all file contents and makes all characters lowercase
    '''
    lst = []
    
    with open (filename, "r") as infile:
        for line in infile:
            lowered_line = line.lower().strip()
            lst.append(lowered_line)          
    return lst
  
def sentiment_score(words, sent_words):
    ''' Function: sentiment_score
        Parameters: List of strings (words),
                    dictionary of word : value
        Return: Sentiment score - float (-1 to +1)
        Does: Iterates over the list of words,
            adjust score according to values in the dictionary,
            and divide by the length
    '''
    score = 0
    for word in words:
        if word in sent_words:
            score += sent_words[word]
    return score / len(words)

def alpha(text):
    ''' Function: alpha
        Parameters: Text (string)
        Return: Text (string) containing ONLY alpha characters
        Does: Removes punctuation and numbers from given string
    '''
    for item in text:
        if item.isalpha() == False:
            text = text.replace(item, ' ')
    return text

def tokenize(lst):
    ''' Function: tokenize
        Parameters: 1d list of strings
        Return: 2D list of strings
        Does: Separates each comment into a list of strings, creating
                a larger 2D list of individual comment lists
    '''
    lst_lines = []
    
    for i in lst:
        lst = i.split()
        lst_lines.append(lst)
    return lst_lines
        
def main():
   
    # Gather data - using read_file function, read in the file, make all 
    # characters lowercase, and remove "\n" from each line 
    sentences = read_file(REDDIT_FILE)
    
    # Modify the contents of the file: remove all non-alpha characters and
    # tokenize words, and append tokenized words to a list
    words = []
    
    for i in sentences:
        no_punctuation = alpha(i)
        words.append(no_punctuation)
    words = tokenize(words)
    
    # Computation - use sentiment_score function to compute sentiment scores
    # for each comment, and append these values to a list
    sentiment_scores = []
    
    for word in words:
        score = sentiment_score(word, SENT_WORDS)
        sentiment_scores.append(score)
        
    # Reverse the order so that scores are represented old-to-new 
    sentiment_scores.reverse()
    
    # Create lists for individual sentiment score categories (pos, neg, neut.)
    
    positive = []
    neutral = []
    negative = []
    
    # Initialize a value for the list position
    list_pos = 0
    
    # Create lists for comments' position (order added)
    positive_pos = []
    neutral_pos = []
    negative_pos = []
    
    # Iterate over scores to categorize them: neutral, positive, or negative?
    # Append score to appropriate list and assign it a position (order)
    for score in sentiment_scores:
        if score > 0:
            positive.append(score)
            list_pos += 1
            positive_pos.append(list_pos)
        elif score == 0:
            neutral.append(score)
            neutral_pos.append(list_pos)
            list_pos += 1
        else:
            negative.append(score)
            list_pos += 1
            negative_pos.append(list_pos)
            
    # Communication - plot the scores in different colors
    plt.scatter(positive_pos, positive, color = "forestgreen", label = 
                "Positive")
    plt.scatter(neutral_pos, neutral, color = "yellow",
                label = "Neutral")
    plt.scatter(negative_pos, negative, color = "red", label = "Negative")
    
    # Add axes labels, a title, and a legend to plot
    plt.xlabel("Order of Comments Added: Oldest to Newest")
    plt.ylabel("Sentiment Score, -1 to 1")
    plt.title("Northeastern Sentiments on Reddit")
    plt.legend()
    plt.show()
    
main()