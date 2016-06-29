[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

The following table displays the results for different values of the log upper bound.

|log_upper|mean|median|skew|Pearson skew|frac below mean|
|:---:|:---:|:---:|:---:|:---:|:---:|
|5.0|4.645700|4.709498|-0.080693|-0.435652|0.439841|
|6.0|4.657586|4.709498|-0.062768|-0.337947|0.450603|
|7.0|4.669471|4.709498|0.009902|-0.241471|0.461742|
|8.0|4.681357|4.709498|0.171310|-0.154707|0.472889|

#### Python Code:
```python
import chap06soln
import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None

def skew(xs):
  mean = np.mean(xs)
  return sum((x - mean)**3 for x in xs) / len(xs)

def p_skew(xs):
  mean = np.mean(xs)
  median = np.median(xs)
  sd = np.std(xs)
  return 3 * (mean - median) / sd

def interpolate(upper):
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

interpolate(5.0, md=True)
interpolate(6.0, md=True)
interpolate(7.0, md=True)
interpolate(8.0, md=True)
```
