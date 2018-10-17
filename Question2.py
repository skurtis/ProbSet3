#!/usr/bin/env python3

import pandas as pd
import re
# Import the necessary modules

cols = ["DateTime","WaterLevel","Sigma","O","F","R","L","Quality"]
# Creates a list of modified column names since the original file has column names consisting of multiple words

df = pd.read_csv("CO-OPS__8729108__wl.csv",sep=',',header=None,names=cols)
# Creates the dataframe "df" by importing a CSV file using pandas called as pd. "cols" represents the column names.

maxlevel1 = max(df.WaterLevel[1:424])
maxlevel2 = max(df.WaterLevel[425:])
maxlevel = max([maxlevel1,maxlevel2])
# Since there is a missing data line, I calculate the maximum value of all data before and after this line separately.
# I then calculate the maximum between those two sets of data.

maxDT = df.DateTime[df.WaterLevel == maxlevel] 
# Finds the line containing the maximum water level and input that into the date and time column.

maxDTstr = str(maxDT)
# Turns the date and time of the max water level into a string to easily find items within it.

print("The highest water level of",maxlevel,"was observed on",re.findall('[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]',maxDTstr)[0], \
"at",re.findall('[0-9][0-9]:[0-9][0-9]',maxDTstr)[0])
# Uses the findall function and regular expressions to find the date and time within the string.
# Calling the 0th item within the findall output generates a string to feed into the print function. 
