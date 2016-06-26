[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

From the scatter plot below, it seems like birth weight and mother's age are not correlated. There doesn't seem to be any obvious sign of a positive or negative correlation between the two. Furthermore, we find the Pearson and Spearman correlation coefficients to be 0.0688 and 0.0946 respectively. Both correlation coefficients are very small, which supports our visual observation that the two variables are not correlated.

![alt-text](https://github.com/a3huang/dsp/blob/master/img/Scatter-7-1.png)

From the quantile plots below, it seems like birth weight is very slightly increasing with mothers' age. We see that there is a noticeably large dip in birth weight at around age 39. However, it seems strange that almost all ages besides 39 have similar birth weights, while 39 alone seems to have much lower birth weights than the others. Because of this, we should investigate further to see why the lower quartile of birth weights for 39 year old pregnant women is so low. Once thing to consider is that we don't have the same number of pregnant mothers of each age. In particular, there are relatively fewer 39 year old mothers than those in the 15 to 35 year old range. There are even fewer mothers who are 40 years or older, so we may not be able to trust the values of the sample quartiles near the extremes of our range. Overall, the middle section of each quantile plot seems to confirm what we have suspected above. That is, there appears to be little relationship between a mother's age and the birth weight of her child.

![alt-text](https://github.com/a3huang/dsp/blob/master/img/Quantiles-7-1.png)

#### Python Code:
```python
import nsfg
import matplotlib.pyplot as plt
import numpy as np

data = nsfg.ReadFemPreg()
data = data[data.outcome == 1] # only consider live births                      

### scatterplot of birth weight and mother's age ###                            
ax = data.plot(kind='scatter', x='agepreg', y='totalwgt_lb', alpha=0.2)
ax.set_title("Scatterplot of Birth Weight v.s. Mother's Age", fontsize=18, fontweight='bold', y=1.01)
ax.set_xlabel('Age at Pregnancy (years)')
ax.set_ylabel('Birth Weight (lbs)')
plt.xticks(y=-.01)
plt.yticks(np.arange(-2, 20, 2), x=-.01)
plt.axis([5, 50, -2, 20])
plt.savefig('Scatter-7-1')

### group birth weight according to integer part of mother's age ###            
data['int_age'] = data.agepreg.fillna(0).astype(int)
data = data[data.int_age > 0]
age_groups = data.groupby('int_age')['totalwgt_lb']

### calculate 25th, 50th, and 75th quantiles of birth weight for each age ###   
# build up quantile matrix where each column represents single curve  
quantiles = np.zeros((len(age_groups), 3))
for i, (val, grp) in enumerate(age_groups):
  quantiles[i, :] = grp.quantile(np.arange(.25, 1, .25), interpolation='nearest')

# ignore ages which had too few observations                                    
# corresponds to ages in [13, 41] inclusive                                     
quantiles = quantiles[3:-3]

### plot the 25th, 50th, and 75th quantile curves ###                           
plt.figure(2)

for i in range(3):
  plt.plot(np.arange(13, 42) , quantiles[:, i], label="%dth" % ((i+1)*25))

plt.legend(loc=2)
plt.title("Quartiles of Birth Weight", fontsize=18, fontweight='bold', y=1.01)
plt.xlabel("Age at Pregnancy (years)")
plt.ylabel("Birth Weight (lbs)")
plt.xticks(y=-.01)
plt.yticks(np.arange(6, 9, .5), x=-.01)
plt.axis([10, 45, 6, 9])
plt.savefig('Quantiles-7-1')

print data[["agepreg", "totalwgt_lb"]].corr(method='pearson').ix[0,1]
# 0.0688339703541                                                               

print data[["agepreg", "totalwgt_lb"]].corr(method='spearman').ix[0,1]
# 0.0946100410966
```
