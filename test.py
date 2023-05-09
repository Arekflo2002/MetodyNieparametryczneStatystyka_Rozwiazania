import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt 
import math

# wartości punktów, w których ma zostać obliczony PDF
x = np.linspace(0, 50, 1000)
np.random.seed(1234)

# obliczenie PDF dla rozkładu chi-kwadrat
odsetek = 0
n=200
for i in range(50):
    probka = stats.norm.rvs(size=n)
    probka_t = stats.t.rvs(size=n,df=200)



    # Podzielenie danych na przedzialy 
    
    probka_podzial, rozdz = np.histogram(probka, bins='auto')

    id = np.nonzero(probka_podzial==0)[0]
    probka_podzial = probka_podzial[probka_podzial!=0]

    rozdz = np.delete(rozdz,id)

    probka_podzial_t,rozdz_t = np.histogram(probka_t, bins=rozdz)
    roznica = sum(probka_podzial) - sum(probka_podzial_t)
    

    probka_podzial_t[0] += math.ceil(roznica/2)
    probka_podzial_t[-1] += math.floor(roznica/2)

    if sum(probka_podzial) != sum(probka_podzial_t):
        print(probka_podzial_t)

    pval = stats.chisquare(probka_podzial_t,probka_podzial).pvalue
    print(pval)
    if pval < 0.05:
        odsetek +=1 
    
print(odsetek/50)
