[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)


|Sample Size|Bias|RMSE|Standard Error|90% Confidence Interval|
|:---|:---:|:---:|:---:|:---:|
|10|-0.10|7.85|7.85|(87.80, 112.10)|
|100|1.47|10.46|10.35|(85.95, 118.05)|
|1000|1.62|10.16|10.03|(86.00, 118.00)|
|10000|1.88|10.15|9.97|(86.00, 118.00)|
|100000|1.99|10.17|9.97|(86.00, 119.00)|


|2.01|10.33|10.13|(85.00, 119.00)|
if lam is low, it will remain biased even for large n                         
if lam is 100, large n 10000 will make the mean 100                           

stderror: sqrt(lambda), constant in n                                         
rmse: sqrt(lambda), constant in n                                             
mean error (bias): constant in n, constant in lambda = 2?                     

increasing n will make distribution more symmetric                            

for small lam, even with high n (10000), distribution will be biased          
distribution will be unbiased for lam > 80    

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
  plt.savfig('hist-8-3')
  bias = np.mean(results) - lam
  rmse = np.sqrt(np.mean([(result-lam)**2 for result in results]))
  stderror = np.std(results)
  confint = np.percentile(results, [5, 95])
  
  print '%.2f %.2f %.2f (%.2f, %.2f)' % (bias, rmse, stderror, confint[0], confint[1])

for i in range(100, 1000, 100):
  sim(10000, i)
```
