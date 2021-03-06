[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

From the scatterplot below, it seems like birth weight and mother's age are not correlated since there doesn't seem to be any obvious sign of a positive or negative correlation between the two. Furthermore, we find the Pearson and Spearman correlation coefficients to be 0.0688 and 0.0946 respectively. Both correlation coefficients are small, which supports our conclusion from looking at the scatterplot that the two variables are not correlated.

![alt-text](https://github.com/a3huang/dsp/blob/master/img/Scatter-7-1.png)

To produce the plots of the 25th, 50th, and 75th quantiles, we group birth weights in the data set based on the integer part of the mother's age. We chose to plot the quantiles for mothers in the age range between 13 and 41, as ages outside of this range had less than 3 observations each. From the quantile plots below, it seems like birth weight is very slightly increasing with mothers' age. We also see a noticeable dip in birth weight at around age 39. However, it seems strange that there would be a sudden dip at age 39 only to rebound again at age 40. We would expect that women 40 and older would continue the downward trend of birth weight since fertility decreases with age, but for some reason birth weight reverses its trend and increases back up starting at age 40. One possible reason for this discrepancy is that there are differing numbers of pregnant mothers within each age level. In particular, the number of 39 year old mothers is much smaller than the number of mothers in each of the age levels between 15 and 35. The number of mothers in the age levels 40 and older are even smaller. The unusual pattern in the plots tells us that we shouldn't trust the values of the sample quantiles near the extremes of our designated age range. In order to properly estimate the quantiles, we need to somehow obtain more data near the endpoints of our range so that all age levels contain roughly the same number of mothers. In any case, the middle section of each quantile plot seems to suggest that birth weight does increase with mother's age. However, we should be skeptical of this conclusion in light of what we observed with the scatterplot and coefficients of correlation earlier.

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
