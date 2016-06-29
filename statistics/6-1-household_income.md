[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

4.65758573589 4.70949835561 -0.0627676925804 -0.337946664585

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
  print 'log_upper: %.1f\nmean: %f\nmedian: %f\nskew: %f\nPearson skew: %f\n' \
    'frac below mean: %f\n' % (upper, mean, median, skew(log_sample),
    p_skew(log_sample), frac)

interpolate(5.0)
interpolate(6.0)
interpolate(7.0)
interpolate(8.0)
```
