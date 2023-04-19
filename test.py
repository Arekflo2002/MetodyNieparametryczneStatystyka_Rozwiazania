import numpy as np
import scipy.stats as stats

probka = stats.chi2.rvs(5,size = 1000)

podzial,bins = np.histogram(probka,bins)