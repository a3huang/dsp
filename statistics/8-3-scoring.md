[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

To simulate a game, we generate appropriate random values from an exponential distribution until the sum of these "time intervals" exceed 1. We estimate the scoring rate by taking the number of time intervals between goals before the overall sum exceeds 1, and then adding 1 to it.

For soccer, the average number of goals scored per game is usually around 3 to 5. Below are the results for a sample size of 10,000 and a scoring rate of 4 goals per game on average.

|Bias|RMSE|Standard Error|90% Confidence Interval|
|:---:|:---:|:---:|:---:|
|2.00|2.82|1.98|(3.00, 9.00)|

Below is the accompanying histogram for these results.
![alt-text](https://github.com/a3huang/dsp/blob/master/img/hist-8-3.png)

As we can see, despite the large sample size, the histogram is skewed and there is a clear bias as it tends to overestimate the true scoring rate of 4. We can also see this from the mean error (or bias), which has a value of 2. This tells us that on average (out of 10,000 trials) the estimated scoring rate overestimates the true scoring rate by 2.

It is interesting to note that for small values of lambda, the histograms of the estimates tend to be skewed, even for very large values of n. However, once lambda gets large enough (at about 80), increasing n tends to make the histograms look more symmetric.

Below is a histogram for a sample size of 10,000 and a lambda of 100.
![alt-text](https://github.com/a3huang/dsp/blob/master/img/hist2-8-3.png)

The following table presents results for several sample sizes, while keeping lam = 100 constant.

|Sample Size|Bias|RMSE|Standard Error|90% Confidence Interval|
|:---|:---:|:---:|:---:|:---:|
|10|-0.10|7.85|7.85|(87.80, 112.10)|
|100|1.47|10.46|10.35|(85.95, 118.05)|
|1000|1.62|10.16|10.03|(86.00, 118.00)|
|10000|1.88|10.15|9.97|(86.00, 118.00)|

We see that as n increases, the values of bias, RMSE, and standard error seem to remain largely the same. In contrast, if we hold n = 10,000 constant and vary lambda, we get the following results:

|Lambda|Bias|RMSE|Standard Error|90% Confidence Interval|
|:---|:---:|:---:|:---:|:---:|
|10|1.91|3.66|3.13|(7.00, 18.00)|
|100|2.24|10.54|10.30|(86.00, 119.00)|
|1000|1.25|31.88|31.85|(951.00, 1054.05)|
|10000|1.62|100.84|100.82|(9833.00, 10165.10)|

Here we see that while the bias takes on roughly the same values for each lambda, the RMSE and standard error seem to be roughly proportional to the square root of lambda. Thus, unlike the case with the MLE, the standard error of this estimator remains roughly constant with respect to sample size and varies with the square root of the true goal scoring rate.

#### Python Code:
```python
import numpy as np
import matplotlib.pyplot as plt

# lam: goals per game                                       
# returns a sample estimate of lam
def game(lam):
  time_ints = list()
  while sum(time_ints) <= 1:
    time_ints.append(np.random.exponential(scale=1.0/lam))
  return len(time_ints) + 1

def sim(n, lam=10):
  results = list()
  for i in range(n):
    results.append(game(lam))
  
  plt.hist(results)
  plt.title('Histogram for lam = %d, n = %d' % (lam, n), fontsize=18, fontweight='bold', y=1.01)
  plt.xlabel('Estimated Values of Rate')
  plt.ylabel('Frequency')
  plt.xticks(y=-.01)
  plt.yticks(x=-.01)
  plt.savfig('hist-8-3')
  
  bias = np.mean(results) - lam
  rmse = np.sqrt(np.mean([(result-lam)**2 for result in results]))
  stderror = np.std(results)
  confint = np.percentile(results, [5, 95])
  print '%.2f %.2f %.2f (%.2f, %.2f)' % (bias, rmse, stderror, confint[0], confint[1])
```
