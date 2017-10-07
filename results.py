#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

results.py

Josh Kaplan
_jk@jhu.edu


"""
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt 
import numpy as np


def reject_outliers(data):
    """ 
    Based on : 
    https://stackoverflow.com/questions/11686720/is-there-a-numpy-builtin-to-reject-outliers-from-a-list
    """
    m = 1
    u = np.mean(data)
    s = np.std(data)
    return [d for d in data if (u - m*s < d < u + m*s)]


# Read execution times of program 1
with open('p1.dat') as f:
   X1 =  f.read().splitlines()

# Read execution times of program 2
with open('p2.dat') as f:
   X2 =  f.read().splitlines()

X1 = [ int(x) for x in X1 if int(x) > 0 ]
X2 = [ int(x) for x in X2 if int(x) > 0 ]
X1 = reject_outliers(X1)
X2 = reject_outliers(X2)

plt.plot(X1, 'b.', markersize=0.5)
plt.plot(X2, 'r.', markersize=0.5)
#plt.plot(X1, 'b-')
#plt.plot(X2, 'r-')

#### Option 1
#x = np.arange(len(X1))
#m, b = np.polyfit(x, X1, 1)
#prog1 = plt.plot(x, m*x+b, 'b-')
#
#x = np.arange(len(X2))
#m, b = np.polyfit(x, X2, 1)
#prog2 = plt.plot(x, m*x+b, 'r-')

### Option 2
x = np.arange(len(X1))
m = np.mean(X1)
prog1 = plt.plot(x, m + 0*x, 'b-')

x = np.arange(len(X2))
m = np.mean(X2)
prog2 = plt.plot(x, m + 0*x, 'r-')

ax = plt.gca()
lo = 0.9 * min([min(X1), min(X2)])
hi = 1.1 * max([max(X1), max(X2)])
ax.set_ylim(lo, hi)
ax.set_xlabel('Samples')
ax.set_ylabel('Execution Time (microseconds)')
b_patch = mpatches.Patch(color='blue', label='Program 1')
r_patch = mpatches.Patch(color='red', label='Program 2')
plt.legend(handles=[b_patch, r_patch])
plt.show()
