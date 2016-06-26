[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

#### Python Code:
```python
import numpy as np
import matplotlib.pyplot as plt

def Estimate_L(n):
  results = list()
  for i in range(1000):
    results.append(1/np.mean(np.random.exponential(scale=0.5, size=n)))

  counts, bins, patches = plt.hist(results)
  plt.title('Histogram of L for Sample Size: %d' % n, fontsize=18,
    fontweight='bold', y=1.01)
  plt.xlabel('L')
  plt.ylabel('Frequency')
  plt.xticks(y=-.01)
  plt.xticks()[1][0].set_visible(False)
  plt.xticks()[1][-1].set_visible(False)
  plt.yticks(x=-.01)
  plt.savefig('Histogram_%d' % n)

  return (np.std(results), np.percentile(results, [5, 95]))

stderrors = list()
for i in range(1,6):
  plt.figure()
  error, confint = Estimate_L(10**i)
  stderrors.append(error)
  print '90%% Confidence Interval for L w/ Sample Size %d: (%f, %f)' % \
    (10**i, confint[0], confint[1])


plt.figure()
plt.plot(range(1,6), stderrors)
plt.title('Standard Errors of L', fontsize=18, fontweight='bold', y=1.01)
plt.xlabel('Sample Size (powers of 10)')
plt.ylabel('Standard Error Estimates')
plt.xticks(range(1,6), y=-.01)
plt.yticks(x=-.01)
plt.savefig('StdError-8-2')
```
