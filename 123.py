import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Czym wieksza moc testu tym wiekszy odsetek odrzucenia H0 ---- > Tym mniej symulacji mialo rozklad normalny
# Wyniki w tabelach pokazuja w jakim % wynikow odrzucam H0, czyli w jakiej odsetku symluacji rozklad 
# byl "normalny"
np.random.seed(seed=123)

liczba_stopni = range(1,50,1)
alfa = 0.05
n = [10,20,50,100,500]
liczba_symulacji = 100
moce_testow = []
 
# Zebranie danych z rozkladu t - studenta

for stopien in liczba_stopni:
    moc_n_testu = []
    for nka in n:
        odrzucenie_H0 = 0
        for K in range(liczba_symulacji):
            probka = stats.t.rvs(stopien,size=nka)
            # Standaryzacja danych i guess
            stand_probka = (probka - np.mean(probka))/np.std(probka)
            # Bede badal odsetek odrzucenia H0 przy 1000 symulacji 
            # Jezeli pvalue jest < 0.05 to sa podstawy do orzucenia H0 wiec =+ zmienna 
            if stats.shapiro(stand_probka).pvalue < alfa: 
                odrzucenie_H0 += 1
        
           # Obliczamy ostateczny odsetek odrzucenia H0
        moc_n_testu.append((odrzucenie_H0/liczba_symulacji))

    moce_testow.append(moc_n_testu)


# Etap Tworzenia wykresu 
print(len(moce_testow))
plt.figure()
plt.plot(moce_testow[0])
plt.plot(moce_testow[1])
plt.plot(moce_testow[2])
plt.plot(moce_testow[3])
plt.plot(moce_testow[4])

plt.show()