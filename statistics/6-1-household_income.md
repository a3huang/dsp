[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

4.65758573589 4.70949835561 -0.0627676925804 -0.337946664585

#### Python Code:
```python
import chap06soln
import numpy as np

def skew(xs):
  mean = np.mean(xs)
  return sum((x - mean)**3 for x in xs) / len(xs)
def p_skew(xs):
  mean = np.mean(xs)
  median = np.median(xs)
  sd = np.std(xs)
  return 3 * (mean - median) / sd

df = chap06soln.hinc.ReadData()
log_sample = chap06soln.InterpolateSample(df, log_upper=6.0)
mean = np.mean(log_sample)
median = np.median(log_sample)

print mean, median, skew(log_sample), p_skew(log_sample)
```
