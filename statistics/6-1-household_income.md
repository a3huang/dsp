[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

The following table displays the results for different values of the log upper bound.

|log_upper|mean|median|skew|Pearson skew|frac below mean|
|:---:|:---:|:---:|:---:|:---:|:---:|
|5.0|4.645700|4.709498|-0.951620|-0.435652|0.439841|
|6.0|4.657586|4.709498|-0.641354|-0.337947|0.450603|
|7.0|4.669471|4.709498|0.080519|-0.241471|0.461742|
|8.0|4.681357|4.709498|1.054188|-0.154707|0.472889|

We see that the mean, median, and fraction of incomes below the mean seem to be relatively stable with respect to log_upper. However, the skew seems to vary in magnitude and even changes sign depending on the value of log_upper. While the Pearson skew keeps the same sign for each value of log_upper, its magnitude seems to decrease as we increase log_upper. The Pearson skew suggests that the data is left skewed for each of the above values of log_upper, but the skew suggests that the data is left skewed for some values and right skewed for others.

Below are the histograms of log_sample for each value of log_upper. From visual inspection, it seems that some of them are left skewed while others are right skewed, as suggested by the skew statistic.
![alt-text](https://github.com/a3huang/dsp/blob/master/img/hists-6-1.png)

#### Python Code:
```python
import chap06soln
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

def skew(xs):
  mean = np.mean(xs)
  sd = np.std(xs)
  return sum((x - mean)**3 for x in xs) / len(xs) / sd**3

def p_skew(xs):
  mean = np.mean(xs)
  median = np.median(xs)
  sd = np.std(xs)
  return 3 * (mean - median) / sd

def interpolate(upper, ax, md=False):
  df = chap06soln.hinc.ReadData()
  log_sample = chap06soln.InterpolateSample(df, log_upper=upper)
  mean = np.mean(log_sample)
  median = np.median(log_sample)
  frac = len([i for i in log_sample if i < mean]) / float(len(log_sample))
  
  # option to help with creating table in markdown                              
  if md == True:
    print '|%.1f|%f|%f|%f|%f|%f|' % (upper, mean, median, skew(log_sample),
      p_skew(log_sample), frac)
  else:
    print 'log_upper: %.1f\nmean: %f\nmedian: %f\nskew: %f\nPearson skew:' \
      '%f\nfrac below mean: %f\n' % (upper, mean, median, skew(log_sample),
      p_skew(log_sample), frac)
  
  # plot single histogram on passed in axis object                              
  ax.hist(log_sample)
  ax.set_title('log_upper = %.1f' % upper, fontsize=14, fontweight='bold')
  ax.set_xlabel('log_sample')
  ax.set_ylabel('Frequency')
  ax.locator_params(axis='x', nbins=7)
  ax.tick_params(axis='both', which='major', pad=8)

#interpolate(5.0, md=True) # left skewed                                        
#interpolate(6.0, md=True) # left skewed                                        
#interpolate(7.0, md=True) # slightly right skewed
#interpolate(8.0, md=True) # right skewed

# plotting the 4 histograms together at once
fig, ax = plt.subplots(2,2)
fig.suptitle('Histograms of log_sample', fontsize=18, fontweight='bold')
ax = ax.flat
for i in range(1,5):
  interpolate(4.0 + i, ax[i-1], md=True)
plt.subplots_adjust(wspace=0.5, hspace=0.5, top=.88)
plt.savefig('hists-6-1')
```
