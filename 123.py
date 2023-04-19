import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

probka = stats.t.rvs(5,size = 100)

freq,bins = np.histogram(probka,bins = 'auto')


expect = []

for i in range(len(bins)-1):
    a, b = bins[i],bins[i+1]
    expects = stats.norm.cdf(b) - stats.norm.cdf(a)
    expect.append(expects)

print(sum(expect))