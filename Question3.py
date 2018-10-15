#!/usr/bin/env python3

datafile = open("../CO-OPS__8729108__wl.csv")

diffmax = 0
for i in datafile:
	if i.startswith('Date'): 
		prevline = i
		continue
	if prevline.startswith('Date'): 
		prevline = i
		continue
	if i[17:22].startswith(','): continue
	date_curr = i[:10]
	time_curr = i[11:16]
	diff_curr = float(i[17:22]) - float(prevline[17:22])
	if diff_curr > diffmax:
		diffmax = diff_curr
		datemax = date_curr
		timemax = time_curr
	prevline = i
print("The maximum increase in water level was", round(diffmax,3), "that was observed on", datemax, "at", timemax)	
