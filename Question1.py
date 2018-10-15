#!/usr/bin/env python3

datafile = open("../CO-OPS__8729108__wl.csv")

wmax = 0
for i in datafile:
	if i.startswith('Date'): continue
	date_curr = i[:10]
	time_curr = i[11:16]
	if i[17:22].startswith(','): continue
	wlevel_curr = float(i[17:22])
	if wlevel_curr > wmax:
		wmax = wlevel_curr
		datemax = date_curr
		timemax = time_curr
print("The maximum water level of", wmax, "was observed on", datemax, "at", timemax)	
