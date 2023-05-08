import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

dfs = 3
probka = np.random.chisquare(dfs,size = 200)

# wartości punktów, w których ma zostać obliczony PDF
x = np.linspace(0, 50, 1000)

# obliczenie PDF dla rozkładu chi-kwadrat

for i in range(50):
    probka = stats.norm.rvs(size=200)
    probka_t = stats.t.rvs(size=200,df=100)

    dol = min(min(probka),min(probka_t))
    gora = max(max(probka),max(probka_t))


    # Podzielenie danych na przedzialy 

    probka_podzial, rozdz = np.histogram(probka, bins=5,range=(dol,gora))

    probka_podzial_t,rozdz_t = np.histogram(probka_t, bins=rozdz,range=(dol,gora))



    print(probka_podzial)
    pval = stats.chisquare(probka_podzial_t,probka_podzial).pvalue

    if pval == 'nan' or pval == 0.0:
        print(123)

