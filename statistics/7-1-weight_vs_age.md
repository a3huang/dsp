[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

age 39 seems to have quite a few low weight babies   

#### Python Code:
```python
import nsfg
import matplotlib.pyplot as plt
import numpy as np

data = nsfg.ReadFemPreg()
data = data[data.outcome == 1] # only consider live births                      

### scatterplot of birth weight and mother's age ###                            
ax = data.plot(kind='scatter', x='agepreg', y='totalwgt_lb', alpha=0.2)
ax.set_title("Scatterplot of Birth Weight v.s. Mother's Age")
ax.set_xlabel('Age at Pregnancy (years)')
ax.set_ylabel('Birth Weight (lbs)')
plt.savefig('Scatter-7-1')

### group birth weight according to integer part of mother's age ###            
data['int_age'] = data.agepreg.fillna(0).astype(int)
data = data[data.int_age > 0]
age_groups = data.groupby('int_age')['totalwgt_lb']

### calculate 25th, 50th, and 75th quantiles of birth weight for each age ###   
# build up quantile matrix where each column is single curve  
quantiles = np.zeros((len(age_groups), 3))
for i, (val, grp) in enumerate(age_groups):
  quantiles[i, :] = grp.quantile(np.arange(.25, 1, .25),
    interpolation='nearest')

# ignore ages which had too few observations                                    
# corresponds to ages in [13, 41] inclusive                                     
quantiles = quantiles[3:-3]

### plot the 25th, 50th, and 75th quantile curves ###                           
plt.figure(2)

for i in range(3):
  plt.plot(np.arange(13, 42) , quantiles[:, i],
    label="%dth" % ((i+1)*25))

plt.legend(loc=2)
plt.title("Quartiles of Birth Weight")
plt.xlabel("Age at Pregnancy (years)")
plt.ylabel("Birth Weight (lbs)")
plt.axis([10, 45, 6, 9])
plt.savefig('Quantiles-7-1')

print data[["agepreg", "totalwgt_lb"]].corr(method='pearson').ix[0,1]
# 0.0688339703541                                                               

print data[["agepreg", "totalwgt_lb"]].corr(method='spearman').ix[0,1]
# 0.0946100410966
```
