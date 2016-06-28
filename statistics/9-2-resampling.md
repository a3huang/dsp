[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

Running 100 hypothesis tests each on pregnancy length and birth weight, we get p-values of 0.21 and 0.0 respectively. Thus, it seems like there is no significant difference in pregnancy length between first babies and others. However, there does seem to be a significant difference in birth weight between the two groups. These results are the same as what we would have gotten had we used permutations to simulate the null hypothesis instead.

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
