import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Czym wieksza moc testu tym wiekszy odsetek    odrzucenia H0 ---- > Tym mniej symulacji mialo rozklad normalny
# Wyniki w tabelach pokazuja w jakim % wynikow odrzucam H0, czyli w jakiej odsetku symluacji rozklad 
# byl "normalny"
np.random.seed(seed=123)

stopnie_swobody = range(1,50)
alfa = 0.05 
liczba_danych = [10,20,50,100,200]
liczba_symulacji = 100
moce_testow = []
 
# Zebranie danych z rozkladu t - studenta

for n in liczba_danych:
    print(n)
    moc_n_testu = []
    for stopien in stopnie_swobody:
        odrzucenie_H0 = 0
        for K in range(liczba_symulacji):
            probka = stats.t.rvs(stopien,size=n)
            stand_probka = (probka-np.mean(probka))/np.std(probka)

            if stats.shapiro(stand_probka).pvalue < alfa:
                odrzucenie_H0 += 1
        
        moc_n_testu.append((odrzucenie_H0/liczba_symulacji))
    moce_testow.append(moc_n_testu)



# Etap Tworzenia wykresu 

plt.figure()

for i,moc in enumerate(moce_testow):
    plt.plot(stopnie_swobody,moc,label = "ggg")


plt.show()