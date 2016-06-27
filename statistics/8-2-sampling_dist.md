[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

The results for several sample sizes are shown below:

| Sample Size | Standard Error | 90% Confidence Interval |
|-------------|:----------------:|:-------------------------:|
|10|0.751612 |(1.283413, 3.741700)|
|100|0.202648 |(1.712411, 2.362234)| 
|1000|0.062765 |(1.906998, 2.109332)| 
|10000|0.019660 |(1.968973, 2.032203)| 
|100000 |0.006327 |(1.990008, 2.010539)|

The histograms of the estimator L for each of the above sample sizes are shown below:

![alt-text](https://github.com/a3huang/dsp/blob/master/img/hist_all.png)

Since L is the MLE of lambda, by asymptotic theory we have the following for large n:

<img src="http://latex.codecogs.com/svg.latex?L&space;\sim&space;N(\lambda,&space;n^{-1}&space;I^{-1})" title="L \sim N(\lambda, n^{-1} I^{-1})" />

In other words, the MLE is asymptotically normal with mean being the true value of lambda and variance of order O(1/n). This is apparent in the above histograms as we can see that the distribution centers around the true value 2 for large n. We can also see from the histograms that the variance decreases with n as the distribution concentrates more tightly around 2 for large n.

Below is the plot of empirical standard errors for L. As expected, the errors decrease as n gets larger.

![alt-text](https://github.com/a3huang/dsp/blob/master/img/StdError-8-2.png)

#### Python Code:
```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# generates histogram, standard error, and 90% confidence interval for L        
def Estimate_L(n, ax):
  results = list()
  for i in range(1000):
    results.append(1/np.mean(np.random.exponential(scale=0.5, size=n)))

  # plot single histogram on passed in axis object                              
  ax.hist(results)
  ax.set_title('n = %d' % n, fontsize=14, fontweight='bold')
  ax.set_xlabel('L')
  ax.set_ylabel('Frequency')
  ax.locator_params(axis='x', nbins=6)
  ax.locator_params(axis='y', nbins=6)
  ax.set_xticklabels(ax.get_xticks().tolist(), ha='left')
  ax.tick_params(axis='both', which='major', pad=8)
  ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
  ax.xaxis.get_major_ticks()[-1].set_visible(False)
  ax.yaxis.get_major_ticks()[-1].set_visible(False)

  return (np.std(results), np.percentile(results, [5, 95]))

# set up plotting region for histograms                                         
fig, ax = plt.subplots(3,2)
fig.suptitle('Histograms of L', fontsize=18, fontweight='bold')
ax = ax.flat

# collect standard errors into a list for plotting                              
stderrors = list()
for i in range(1,6):
  error, confint = Estimate_L(10**i, ax[i-1])
  stderrors.append(error)
  print '%d %f (%f, %f)' % (10**i, error, confint[0], confint[1])

# put all histograms into a single file                                         
fig.delaxes(ax[-1])
plt.subplots_adjust(wspace=0.4, hspace=0.8)
plt.savefig('hist_all')

# plot standard errors
plt.figure()
plt.plot(range(1,6), stderrors)
plt.title('Standard Errors of L', fontsize=18, fontweight='bold', y=1.01)
plt.xlabel('Sample Size (powers of 10)')
plt.ylabel('Standard Error Estimates')
plt.xticks(range(1,6), y=-.01)
plt.yticks(x=-.01)
plt.savefig('StdError-8-2')
```
