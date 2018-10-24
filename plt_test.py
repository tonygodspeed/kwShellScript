"""
=====================================
Custom tick formatter for time series
=====================================

When plotting time series, e.g., financial time series, one often wants
to leave out days on which there is no data, i.e. weekends.  The example
below shows how to use an 'index formatter' to achieve the desired plot
"""

'''
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker

datafile = cbook.get_sample_data('aapl.csv', asfileobj=False)
print('loading %s' % datafile)
r = mlab.csv2rec(datafile)

r.sort()
r = r[-30:]  # get the last 30 days


# first we'll do it the default way, with gaps on weekends
fig, axes = plt.subplots(ncols=2, figsize=(8, 4))
ax = axes[0]
ax.plot(r.date, r.adj_close, 'o-')
ax.set_title("Default")
fig.autofmt_xdate()

# next we'll write a custom formatter
N = len(r)
ind = np.arange(N)  # the evenly spaced plot indices


def format_date(x, pos=None):
    thisind = np.clip(int(x + 0.5), 0, N - 1)
    return r.date[thisind].strftime('%Y-%m-%d')

ax = axes[1]
ax.plot(ind, r.adj_close, 'o-')
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
ax.set_title("Custom tick formatter")
fig.autofmt_xdate()

plt.show()
'''

import matplotlib.pyplot as plt

# data
x = [0, 5, 9, 10, 15]
y = [0, 1, 2, 3, 4]

# trick to get the axes
fig, ax = plt.subplots()

# make ticks and tick labels
xticks = range(min(x), max(x) + 1, 3)
xticklabels = ['2000010' + str(n) for n in range(1, len(xticks) + 1)]

# plot data
ax.plot(x, y, 'mo:')

# set ticks and tick labels
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels, rotation=15)

# show the figure
plt.show()

'''
import numpy as np
import pylab as pl
#from matplotlib.dates import AutoDateLocator, DateFormatter

#autodates = AutoDateLocator()
#yearsFmt = DateFormatter('%Y-%m-%d %H:%M:%S')
#ax = pl.gca();
#figure = pl.figure();
#ax.xaxis.set_major_formatter(mondayFormatter)
x1 = [20170427,20170428, 20170429, 20170430, 20170501]# Make x, y arrays for each graph
y1 = [1, 4, 9, 16, 25]
'''
x2 = [1, 2, 4, 6, 8]
y2 = [2, 4, 8, 12, 16]
'''
fig=pl.figure(figsize=(15,8))
ax1=fig.add_subplot(111)
#pl.axis([20170427,20170501,0,25])

#fig,ax1 = pl.subplots();
#import matplotlib.dates as mdate
#ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y%m%d'))

ax1.set_xticks(x1)
#fig.autofmt_xdate();
#pl.xticks(pd.date_range(demo0719.index[0],demo0719.index[-1],freq='1min'))
ax1.set_xticklabels(x1)
#pl.xticks(x1,x1);

pl.plot(x1, y1, 'r')# use pylab to plot x and y
#figure.autofmt_xdate();
#ax.xaxis.set_major_locator(autodates)


pl.title('Plot of y vs. x')# give plot a title
pl.xlabel('x axis')# make axis labels
pl.ylabel('y axis')

 
#pl.xlim(0.0, 9.0)# set axis limits
#pl.ylim(0.0, 30.)
 
 
pl.show()# show the plot on the screen

#pl.savefig('D:/MyFig.jpg')
'''
