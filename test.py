import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt 
import math

# wartości punktów, w których ma zostać obliczony PDF
x = np.linspace(0, 50, 1000)

# obliczenie PDF dla rozkładu chi-kwadrat
odsetek = 0
for i in range(4):
    probka = stats.norm.rvs(size=100)
    probka_t = stats.t.rvs(size=100,df=100)



    # Podzielenie danych na przedzialy 
    
    probka_podzial, rozdz = np.histogram(probka, bins='auto')
    print(rozdz,"\n:",probka_podzial)

    probka_podzial_te = probka_podzial
    rozdz_te = rozdz

    print(np.array_split(probka_podzial,2))

    # probka_podzial_t,rozdz_t = np.histogram(probka_t, bins=rozdz)
    # roznica = sum(probka_podzial) - sum(probka_podzial_t)
    

    # probka_podzial_t[0] += math.ceil(roznica/2)
    # probka_podzial_t[-1] += math.floor(roznica/2)

    # pval = stats.chisquare(probka_podzial_t,probka_podzial).pvalue
    # print(pval)
    # if pval < 0.05:
    #     odsetek +=1 
    

