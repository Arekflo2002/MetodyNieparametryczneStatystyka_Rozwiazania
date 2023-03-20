import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Czym wieksza moc testu tym wiekszy odsetek odrzucenia H0 ---- > Tym mniej symulacji mialo rozklad normalny
# Wyniki w tabelach pokazuja w jakim % wynikow odrzucam H0, czyli w jakiej odsetku symluacji rozklad 
# byl "normalny"
np.random.seed(seed=123)

liczba_stopni = [1,2,50,200]
alfa = 0.05
n = range(10,100)
liczba_symulacji = 100
moce_testow = []
 
# Zebranie danych z rozkladu t - studenta

for stopien in liczba_stopni:
    print(stopien)
    moc_n_testu = []
    for nka in n:
        odrzucenie_H0 = 0
        for K in range(liczba_symulacji):
            probka = stats.t.rvs(stopien,size=nka)
            # Standaryzacja danych i guess
            stand_probka = (probka - np.mean(probka))/np.std(probka)
            # Bede badal odse       tek odrzucenia H0 przy 1000 symulacji 
            # Jezeli pvalue jest < 0.05 to sa podstawy do orzucenia H0 wiec =+ zmienna 
            if stats.shapiro(stand_probka).pvalue < alfa : 
                odrzucenie_H0 += 1
        
           # Obliczamy ostateczny odsetek odrzucenia H0
        moc_n_testu.append((odrzucenie_H0/liczba_symulacji))

    moce_testow.append(moc_n_testu)


# Etap Tworzenia wykresu 

plt.figure()

plt.plot(n,moce_testow[0])
plt.plot(n,moce_testow[1])
plt.plot(n,moce_testow[2])
plt.plot(n,moce_testow[3])

plt.show()