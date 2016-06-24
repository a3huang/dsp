[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

We find that Cohen's *d* for the total weight between first babies and others is about -0.089. Based on how we defined the difference (see code), it seems like first babies tend to be slightly lighter. However, the "standardized" mean difference between the two groups has a magnitude of much less than 1 standard deviation. This suggests that there is no practical difference in mean total weight between first babies and others.

We have also seen that Cohen's *d* for the pregnancy length between the two groups is 0.029. Thus, while mean pregnancy length of first babies may be slightly longer, it seems that there is no practical difference between the two groups either.

##Python Code:
```python
import nsfg, math

data = nsfg.ReadFemPreg()
data = data[data.outcome == 1] # only consider live births                      
group1 = data[data.birthord == 1] # first babies                                
group2 = data[data.birthord != 1] # non first babies                            

def cohen_d(group1, group2):
    """ Calculate Cohen's d for two groups                                      
                                                                                
    Args:                                                                       
        group1: column from group 1                                             
        group2: column from group 2                                             
                                                                                
    """
    mean1 = group1.mean()
    mean2 = group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1 = len(group1)
    n2 = len(group2)
    s = math.sqrt((n1 * var1 + n2 * var2) / (n1 + n2))
    return (mean1 - mean2)/s

print cohen_d(group1.prglngth, group2.prglngth) # 0.0288790446544               
print cohen_d(group1.totalwgt_lb, group2.totalwgt_lb) # -0.0886729270726 
```
