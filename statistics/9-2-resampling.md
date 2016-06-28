[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

prglngth p-value = 0.21       
totalwgt_lb p-value = 0.0   
same results as before

#### Python Code:
```python
import nsfg
import numpy as np

data = nsfg.ReadFemPreg()
data = data[data.outcome == 1]
group1 = data[data.birthord == 1]
group2 = data[data.birthord != 1]
l1 = len(group1)
l2 = len(group2)

def hyptest(column, n):
  mean1 = group1[column].mean()
  mean2 = group2[column].mean()
  obs_diff = abs(mean1 - mean2)

  results = list()
  for i in range(n):
    g1 = np.random.choice(np.arange(l1), l1, replace=True)
    g2 = np.random.choice(np.arange(l2), l2, replace=True)
    diff = abs(data.ix[g1][column].mean() - data.ix[g2][column].mean())
    results.append(diff)
    
  return len([result for result in results if result >= obs_diff]) / float(n)

print hyptest('prglngth', 100)
print hyptest('totalwgt_lb', 100)
```
