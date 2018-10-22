#!/usr/bin/env python3

# IMPORTANT: Make sure that the dataset CO-OPS__8729108__wl.csv is located in the same working directory as the python scripts and Jupyter notebooks.

datafile = open("CO-OPS__8729108__wl.csv") # The CSV file is opened as the variable "datafile"

wmax = 0 # the max water level is initially set to 0

for i in datafile:
	if i.startswith('Date'): continue # skips the first line (header) 
	if i[17:22].startswith(','): continue # skips the line of missing data 

	date_curr = i[:10] # these positions in the line represent the date
	time_curr = i[11:16] # these positions in the line represent the time
	wlevel_curr = float(i[17:22]) # these positions in the line represent the water level
		# the float command is used to convert the data from a string to a number

	if wlevel_curr > wmax: # if a water level higher than the current maximum is called
		wmax = wlevel_curr # the max water level and its time and date are updated
		datemax = date_curr
		timemax = time_curr

print("The maximum water level of", wmax, "was observed on", datemax, "at", timemax)	
# The above line prints the statement on the highest water level 
