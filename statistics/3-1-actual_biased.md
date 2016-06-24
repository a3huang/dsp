[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

The unbiased histogram gives us the distribution of the number of children under 18 in each household. The important point to note is that the units of data we are considering are entire housholds and not individual people. If we go out and survey random people, we would end up with the biased histogram shown below. This is because we are surveying individual people now, and not households as a whole. If the surveying procedure was truly random, then the larger number of children a certain household has, the more likely we are to approach multiple people from that same household. In other words, households with more children are more likely to be overcounted. This creates bias since we are essentially weighting the original unbiased histogram by the number of children in each household.

![alt text](https://github.com/a3huang/dsp/blob/master/img/figure_1.png "Figure 1")

We calculate that the mean of the unbiased distribution is about 1.02 and the mean of the biased distribution is about 2.40. Thus, the seemingly harmless procedure of interviewing random individuals has given us a mean more than two times larger than the original (true) mean!
