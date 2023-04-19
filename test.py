import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

dfs = 3
probka = np.random.chisquare(dfs,size = 200)

# wartości punktów, w których ma zostać obliczony PDF
x = np.linspace(0, 50, 1000)

# obliczenie PDF dla rozkładu chi-kwadrat

podzial,bi = np.histogram(probka,bins='auto')

expected_values = []
rv = stats.chi2
for i in range(len(bi) - 1):
    a, b = bi[i], bi[i+1]
    expected_value = rv.cdf(b, dfs) - rv.cdf(a, dfs)
    expected_value = round(expected_value,5)
    expected_values.append(expected_value)

expected_values[len(expected_values)-1] += 1-sum(expected_values) 

podzial = podzial/np.sum(podzial)


# print(expected_values,"\n")
# print(podzial)

# print(bi)
print(sum(expected_values))
print(sum(podzial))

spr = podzial - expected_values

print(spr)
pva = stats.chisquare(podzial,f_exp=expected_values).pvalue

print(pva)


