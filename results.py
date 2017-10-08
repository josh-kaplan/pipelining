#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

results.py

Josh Kaplan
_jk@jhu.edu

Displays the results of the program timer.

"""
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt 
import numpy as np

def rm_outliers(data):
    u, s = np.mean(data), np.std(data)
    return [d for d in data if (u-s < d < u+s)]

# Read execution times of program 1
with open('p1.dat') as f:
   X1 =  f.read().splitlines()

# Read execution times of program 2
with open('p2.dat') as f:
   X2 =  f.read().splitlines()

# Reject outliers and plot raw data
X1 = rm_outliers([ int(x) for x in X1 if int(x) > 0 ])
X2 = rm_outliers([ int(x) for x in X2 if int(x) > 0 ])
plt.plot(X1, 'b.', markersize=0.5)
plt.plot(X2, 'r.', markersize=0.5)

# Plot mean values for program 1
x = np.arange(len(X1))
plt.plot(x, 0*x + np.mean(X1), 'b-')

# Plot mean values for program 2
x = np.arange(len(X2))
plt.plot(x, 0*x + np.mean(X2), 'r-')

# Configure plot settings and show plot
ax = plt.gca()
ax.set_ylim(0.9*min([min(X1), min(X2)]), 1.1*max([max(X1), max(X2)]))
ax.set_ylabel('Execution Time (microsec)')
b = mpatches.Patch(color='blue', label='Program 1')
r = mpatches.Patch(color='red', label='Program 2')
plt.legend(handles=[b, r])
plt.show()
