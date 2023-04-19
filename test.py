import numpy as np
import scipy.stats as stats

probka = stats.chi2.rvs(5,size = 1000)

# Pewna strona sugeruje zeby uzyc 2*n^(2/5) przedzialow 
podzial,bins = np.histogram(probka,bins='fd')
print(podzial,"\n",bins)