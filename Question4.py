
# coding: utf-8

# # Problem Set 3 Question 4
# 
# The below code is for plotting a graph of water level over time using matplotlib.pyplot. 
# 
# First, the required modules (matplotlib.pyplot and numpy) are imported. I call the CSV file as a variable called "datafile". I create empty lists to store the timecounts ("times"), the dates the level was recorded ("dates"), and the water levels themselves ("levels"). I start the variable "count" at zero so that its value will be added to the timecounts each time the for loop cycles. 
# 
# For each line in the data file, I use if statements to pass over the lines containing the header or containing missing data. The water levels list is updated each time with the most current measurement and the dates list with the date of the most current measurement. The timecounts list is updated with the current measurement number, which is afterward increased by one. 

# In[62]:


#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

datafile = open("CO-OPS__8729108__wl.csv") 

times = []
levels = []
dates = []
count = 0

for i in datafile:
    if i.startswith('Date'): continue 
    if i[17:22].startswith(','): continue
    levels = levels + [float(i[17:22])] 
    dates = dates + [i[:10]] 
    times = times + [count]
    count = count + 1


# I use the below code to indicate on the figure the date for which each measurement occurs. I first create a list of the unique dates using numpy. To find out on which lines a new date is recorded, I divide the total number of measurements by the number of days recorded. I enter the lines on which a new date is recorded into the "days4" list. 

# In[63]:


uniq_dates = np.unique([dates])
day = len(dates)/len(uniq_dates)
days4 = [day*0+1,day*1+1,day*2+1,day*3+1]


# I plot a line graph of the timecount on the x axis and the water level on the y axis. I generate tick marks on the x-axis for each date measurements were recorded.

# In[64]:


fig = plt.figure()
plt.plot(times, levels, '-')
plt.xlabel('Time')
plt.ylabel('Water level')
plt.xticks(days4, uniq_dates);

