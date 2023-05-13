import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import math
# ustalamy parametry symulacji
np.random.seed(seed=123)

# n = 200

# plt.hist(x, bins=10)
# plt.show()
# odsetek = 0
# for i in range(400):
#     x = stats.chi2.rvs(size=n,df=2)
#     x = stats.chi2.cdf(x,df=2)
#     y = stats.uniform.rvs(size=n)
#     # plt.plot(y)
#     # plt.show()
#     if stats.kstest(x,'uniform').pvalue<0.05: odsetek +=1 


# print(odsetek/400)

def wartosci_dla_chi2(probka,s_stopien):
    """
    Jest to funkcja która zwróci 2 zbiory: zbior zaobserwowanych wartosci(na podstawie probki przekazanej do 
    funkcji) oraz zbior wartosci oczekiwanych potrzebnych do testu Chi kwadrat. Zaczne od wylosowania probki 
    z rozkładu chi2 z parametrami takimy jakimi standaryzowałem oryginalna probke. Nastepnie podziele je 
    na przedzialy zawierajce czestotliwosci wystepowania dane. Na koniec wyrównam róznice w sumie tych tablic,
    aby uniknac pozniejszych bledow.    
    """
    # Losuje probke z rozkl chi2 o parametrach z proby
    probka_chi2_or = stats.uniform.rvs(size = len(probka))

    # Dzielenie danych na przedzialy
    probka_chi2_or, przedzialy = np.histogram(probka_chi2_or,bins='auto')
    
    # Teraz tam gdzie przedzial ma czestotliwosc 0(co prowadzi do wysypania sie testu chi kwadrat) łącze zewnetrzne
    # przedzialy w jedno
    indexes = np.nonzero(probka_chi2_or==0)[0]
    probka_chi2_or = probka_chi2_or[probka_chi2_or != 0]
    przedzialy = np.delete(przedzialy,indexes)

    #Teraz dziele na przedzialy probke pochodzaca z chi2 oryginalnej
    probka, _ = np.histogram(probka,bins=przedzialy)

    # Teraz wyrownuje roznice w sumach tych tablic dajac obserwacje ktore sie nie zmiescily w tym zasiego do ostatnich 
    # przedzialow 
    roznica = sum(probka_chi2_or) - sum(probka)
    probka[0] += math.ceil(roznica/2)
    probka[-1] += math.floor(roznica/2)
    
    # Zwracam tablice gotowe do testu
    return probka,probka_chi2_or



n =200
dfs = 10
odsetek=0
for i in range(400):
    chi = stats.chi2.rvs(size=n,df=dfs)
    chi = stats.chi2.cdf(x=chi,df=dfs)

    fob,fex = wartosci_dla_chi2(chi,dfs) 
 
    if stats.chisquare(fob,fex).pvalue <0.05: odsetek+=1 

print(odsetek/400)