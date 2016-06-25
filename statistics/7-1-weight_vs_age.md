[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

#### Python Code:
```python
import nsfg
import matplotlib.pyplot as plt
import numpy as np

data = nsfg.ReadFemPreg()
#data.plot(kind='scatter', x='agepreg', y='totalwgt_lb')                        
#plot.show()                                                                    
data = data[data.outcome == 1]
data['int_age'] = data.agepreg.fillna(0).astype(int)
data = data[data.int_age > 0]
age_groups = data.groupby('int_age')['totalwgt_lb']

# percentiles of birth weight v.s. mother's age                                 
quantiles = np.zeros((len(age_groups), 3))
for i, (val, grp) in enumerate(age_groups):
  quantiles[i, :] = grp.quantile(np.arange(.25, 1, .25))

min_age = min(data.int_age)
max_age = max(data.int_age)
for i in range(3):
  plt.plot(np.arange(min_age, max_age + 1) , quantiles[:, i],
    label="q%d" % ((i+1)*25))
plt.legend()
plt.title("Quartiles of Birth Weight")
plt.xlabel("Age at Pregnancy")
plt.ylabel("Birth Weight")
plt.show()

data[["agepreg", "totalwgt_lb"]].corr(method='pearson').ix[0,1]
data[["agepreg", "totalwgt_lb"]].corr(method='spearman').ix[0,1]
```
