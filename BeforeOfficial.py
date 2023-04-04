import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Czym wieksza moc testu tym wiekszy odsetek    odrzucenia H0 ---- > Tym mniej symulacji mialo rozklad normalny
# Wyniki w tabelach pokazuja w jakim % wynikow odrzucam H0, czyli w jakiej odsetku symluacji rozklad 
# byl "normalny"
np.random.seed(seed=321)

stopnie_swobody = range(1,50)
poziom_istotnosci = 0.05 
liczba_danych = [10,20,50,100,200]
liczba_symulacji = 100
moce_testow = []
 
# Zebranie danych z rozkladu t - studenta
def symulacja_testu(test):
    # Tablica, która zbierze mi moce testów
    moce_testow = []

    # Zaczynamy symulacje
    # Dla każdej liczby danych
    for l_danych in liczba_danych:
        # Tworzę nową tablicę która będzie przechowywała
        # moce testu dla n-tej liczby danych
        moce_n_testu = []
        # Dla każdego stopnia swobody
        for stopien_s in stopnie_swobody:
            # W tej zmiennej będę sumował liczbę razy, gdy dla danego zestawu
            # danych odrzuciłem hipotezę zerową
            suma_odrzucenia_H0 = 0
            # Symulacja, dla danego zestawu danych
            for k in range(liczba_symulacji):
                # Tworzę próbkę danych z rozkładu t-Studenta
                # o l_danych wielkości i stopien_s stopni swobody
                probka = stats.t.rvs(stopien_s, size=l_danych)
                # Standaryzacja danych
                stand_probka = (probka-np.mean(probka))/np.std(probka)

                # Tutaj jest moment decyzyjny, gdzie decyduje jaki test
                # jest teraz symulowany

                # Test Chi-kwadrat
                if test == "chi":
                    # Jeżeli pvalue z danego testu jest mniejsze niż wczesniej
                    # ustalony poziom istotnotnosci to odrucamy Hipoteze zerowa
                    # co znaczy ze zwiekszamy zmienna sumujaca odrzucenie H0 o 1
                    if stats.chisquare(stand_probka).pvalue < poziom_istotnosci:
                        suma_odrzucenia_H0 += 1

                # Test Shapiro-Wilka
                elif test == "shapiro":
                    if stats.shapiro(stand_probka).pvalue < poziom_istotnosci:
                        suma_odrzucenia_H0 += 1

                # Test Kołgomorova
                elif test == "kolmog":
                    if stats.kstest(stand_probka, 'norm').pvalue < poziom_istotnosci:
                        suma_odrzucenia_H0 += 1

            # Teraz podliczamy odsetek w jakim odrzucilismy H0 w całej symulacji
            moce_n_testu.append((suma_odrzucenia_H0/liczba_symulacji))
        # Teraz dodajemy moce n-tego testu do głownej tablicy przechowującej moce testu
        moce_testow.append(moce_n_testu)

    # Symulacja zakonczona

    return moce_testow

moc_shapiro = symulacja_testu("shapiro")

# Tworzę podstawkę do wykresu 
wykres_shapiro = plt.figure()

# Dodaje dane do wykresu 
for i,moc in enumerate(moc_shapiro):
    plt.plot(stopnie_swobody,moc,label= str(liczba_danych[i]))

# Czcionka dla tytulu
font_title = {'family' :'serif','size':17}
# Dodaje opisy do wykresu 
plt.xlabel("Stopnie swobody")
plt.ylabel("Moc Testu")
plt.title("Test Shapiro-Wilka",fontdict=font_title)
plt.legend(title="Liczba danych")
plt.show()