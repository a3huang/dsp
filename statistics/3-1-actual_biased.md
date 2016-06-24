[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

The unbiased histogram gives us the distribution of the number of children under 18 in each household. The important point to note is that the units of data we are considering are entire housholds and not individual people. If we go out and survey random people, we would end up with an estimated histogram similar in shape to the biased histogram shown below. This is because we are surveying individual people now, rather than households as a whole. If the surveying procedure was truly random, then the more children under 18 a certain household has, the more likely we are to approach multiple children from that same household. In other words, households with more children are more likely to be overcounted. This creates bias since we are essentially drawing from a histogram weighted by the number of children, rather than from the original histogram.

Note that in the biased histogram, we find 0 households with 0 children under 18. This is of course an artifact of our sampling procedure, since we can't ask a person that doesn't exist! This presents a severe limitation of our procedure since we are only asking children who are under 18 and that automatically rules out households who don't have any. 

![alt text](https://github.com/a3huang/dsp/blob/master/img/figure_1.png "Figure 1")

We calculate that the mean of the unbiased distribution is about 1.02 and the mean of the biased distribution is about 2.40. Thus, the seemingly harmless procedure of interviewing random individuals has given us a mean more than two times larger than the true mean! Ignoring this subtlety is what seems to produce the so called "class size paradox".

#### Python Code:
```python
import chap01soln
import matplotlib.pyplot as plt
import numpy as np

data = chap01soln.ReadFemResp()

plt.subplot(1,2,1)
ax1 = data.numkdhh.hist(bins=range(7), normed=True)
ax1.set_title("Unbiased Histogram")
ax1.set_xlabel("Number of Children Under 18")

plt.subplot(1,2,2)
ax2 = data.numkdhh.hist(bins=range(7), normed=True, weights=data.numkdhh)
ax2.set_title("Biased Histogram")
ax2.set_xlabel("Number of Children Under 18")

plt.show()

print data.numkdhh.mean() # 1.024205155043831                                   
print np.average(data.numkdhh, weights=data.numkdhh) # 2.4036791006642821  
```
