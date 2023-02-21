import os #standard library
import sys

#!/usr/bin/env python

__author__ = "Brennan Copp"
__credits__ = ""
__version__ = "1.0"

# import the cvs file of raw data
FilePath= os.path.join("Resources", "election_data.csv")

#put with statement before this
Votes = [row[2] for row in csvreader]

#turn votes into dictionary with candidates as key and # votes as value

# sum of total all votes 

# list of candidates who received votes

# percentage of votes for each candidate

# sum of votes for each candidate

# largest increase change over a period

# winner based on popular vote

# NOTE: Analysis should show up in the terminal and exported to a text file
# NOTE: repo needs to have detailed 'README.md' file
