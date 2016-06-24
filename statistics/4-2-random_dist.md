[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

We can see that the histogram looks roughly like the PDF of a uniform distribution on [0, 1]. The empirical "binned" CDF looks roughly like the graph of the function defined by f(x) = x on [0, 1]. Thus, the distribution of the 1000 numbers drawn from random.random seem to be approximately uniformly distributed.

![alt-text] (https://github.com/a3huang/dsp/blob/master/img/figure_2.png)

#### Python Code:
```python
import random
import matplotlib.pyplot as plt
import numpy as np

sample = list()
for i in range(1000):
  sample.append(random.random())

plt.subplot(2,1,1)
height, bins, patches = plt.hist(sample, normed=True)
plt.title("PDF")

plt.subplot(2,1,2)
width = bins[1] - bins[0]
cdf = np.append(0, np.cumsum(height*width))
plt.step(bins, cdf)
plt.title("CDF")

plt.show()
```
