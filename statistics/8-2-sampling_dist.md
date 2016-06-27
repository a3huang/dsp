[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

10 0.772059 (1.266820, 3.715689)
100 0.207557 (1.706145, 2.395852)
1000 0.061950 (1.899947, 2.102595)
10000 0.020130 (1.968949, 2.034037)
100000 0.006217 (1.990308, 2.009845)

#### Python Code:
```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def Estimate_L(n):
  results = list()
  for i in range(1000):
    results.append(1/np.mean(np.random.exponential(scale=0.5, size=n)))

  ax.hist(results)
  ax.set_title('n = %d' % n, fontsize=14, fontweight='bold')
  ax.set_xlabel('L')
  ax.set_ylabel('Frequency')
  ax.tick_params(axis='both', which='major', pad=8)
  ax.set_xticklabels(ax.get_xticks().tolist(), ha='left')
  ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
  ax.locator_params(axis='x', nbins=6)
  ax.locator_params(axis='y', nbins=6)
  ax.xaxis.get_major_ticks()[-1].set_visible(False)
  ax.yaxis.get_major_ticks()[-1].set_visible(False)

  return (np.std(results), np.percentile(results, [5, 95]))

fig, ax = plt.subplots(3,2)
fig.suptitle('Histograms of L', fontsize=18, fontweight='bold')
ax = ax.flat
stderrors = list()
for i in range(1,6):
  error, confint = Estimate_L(10**i, ax[i-1])
  stderrors.append(error)
  print '%d %f (%f, %f)' % (10**i, error, confint[0], confint[1])
fig.delaxes(ax[-1])
plt.subplots_adjust(wspace=0.4, hspace=0.8)
plt.show()

plt.figure()
plt.plot(range(1,6), stderrors)
plt.title('Standard Errors of L', fontsize=18, fontweight='bold', y=1.01)
plt.xlabel('Sample Size (powers of 10)')
plt.ylabel('Standard Error Estimates')
plt.xticks(range(1,6), y=-.01)
plt.yticks(x=-.01)
plt.savefig('StdError-8-2')
```
