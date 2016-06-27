[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

#### Python Code:
```python
import numpy as np
import matplotlib.pyplot as plt

# lam: goals per game                                                           
# returns sample estimate of lam                                                
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
  #plt.show()                                                                   
  confint = np.percentile(results, [5, 95])
  stderror = np.std(results)
  mean_err = np.mean([result-lam for result in results])
  mse = np.mean([(result-lam)**2 for result in results])
  rmse = np.sqrt(mse)
  print '%.2f %.2f %.2f (%.2f, %.2f)' % (mean_err, rmse, stderror, confint[0], confint[1])

for i in range(100, 1000, 100):
  sim(10000, i)
```
