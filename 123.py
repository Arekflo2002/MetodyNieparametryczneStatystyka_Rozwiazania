import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

liczba_stopni = [1,20,100,1000,100000]
alfa = 0.05
n = [10, 30, 50, 100, 300, 500, 1000]
liczba_symulacji = 1000
moce_testow = []

# Zebranie danych z rozkladu t - studenta

for stopien in liczba_stopni:
    for nka in n:
        odrzucenie_H0 = 0
        moc_n_testu = []
        for K in range(liczba_symulacji):
            probka = stats.t.rvs(stopien,size=nka)
            # Standaryzacja danych i guess
            stand_probka = (probka - np.mean(probka))/np.std(probka)
            # Bede badal odsetek odrzucenia H0 przy 1000 symulacji 
            # Jezeli pvalue jest < 0.05 to sa podstawy do orzucenia H0 wiec =+ zmienna 
            if stats.shapiro(stand_probka).pvalue < alfa : 
                odrzucenie_H0 += 1
        
        # Obliczamy ostateczny odsetek odrzucenia H0
        moc_n_testu.append(odrzucenie_H0/nka)

    moce_testow.append(moc_n_testu)


for moce in moce_testow:
    print(moce)
