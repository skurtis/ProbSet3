#!/usr/bin/env python3

datafile = open("CO-OPS__8729108__wl.csv") # open the CSV file as the variable "datafile"

diffmax = 0 # starts the max difference between final and initial mean as 0
for i in datafile:
	if i.startswith('Date'): # skips the first line (header) but makes sure the previous line is designated as "prevline" 
		prevline = i
		# the previous line needs to be called as the current line before the loop begins again 
		continue

	if prevline.startswith('Date'): # skips the first line of data since there is no preceding data to subtract
		prevline = i
		continue

	if i[17:22].startswith(','): continue # this skips the line with missing data

	date_curr = i[:10] # these positions in the line represent the date 
	time_curr = i[11:16] # these positions in the line represent the time
	diff_curr = float(i[17:22]) - float(prevline[17:22]) # these positions in the line represent the water level
	# The float command is used to convert the strings to numbers.
	# The difference between the previous and current water level is calculated 

	if diff_curr > diffmax: 
		# If the difference (increase) in water level is greater than before, then update the water level difference, time, and date
		diffmax = diff_curr
		datemax = date_curr
		timemax = time_curr
	prevline = i 

print("The maximum increase in water level was", round(diffmax,3), "that was observed on", datemax, "at", timemax)	
# the round function is used to round the water level to three decimal points
# the max water level increase and its time and date are inputted into the print function 
