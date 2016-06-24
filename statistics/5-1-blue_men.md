[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Assuming the distribution of male heights is approximately normal, the percentage of the male population that have heights between 5'10'' and 6'1'' is about 34%.

#### Python Code:
```python
import scipy.stats

mu = 178
sigma = 7.7
norm = scipy.stats.norm(loc=mu, scale=sigma)

# 1 in = 2.54 cm                                                                
# 5'10'' = 70 * 2.54 = 177.8 cm                                                 
# 6'1'' = 73 * 2.54 = 185.4 cm                                                  

print norm.cdf(185.4) - norm.cdf(177.8) # 0.342094682946   
```
