
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np



# Zakres stopni swobody, jakie zaprezentuję na wykresie
stopnie_swobody = range(10, 50, 1)  # Zakres od 1-50 co 1
# Ustalam poziom istotności
poziom_istotnosci = 0.05
# Liczba danych dla jakich wykonam symulacje
liczby_danych = [50, 100, 200]
# Liczba symulacji na jakich będę bazować
liczba_symulacji = 100


def symulacja_testu(test):
    # Tablica, która zbierze mi moce testów
    moce_testow = []

    # Zaczynamy symulacje
    # Dla każdej liczby danych
    for l_danych in liczby_danych:
        print(l_danych)
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

                # Test Shapiro-Wilka
                if test == "shapiro":
                    # Jeżeli pvalue z danego testu jest mniejsze niż wczesniej
                    # ustalony poziom istotnotnosci to odrucamy Hipoteze zerowa
                    # co znaczy ze zwiekszamy zmienna sumujaca odrzucenie H0 o 1
                    if stats.shapiro(stand_probka).pvalue < poziom_istotnosci:
                        suma_odrzucenia_H0 += 1

                # Test Chi-kwadrat
                elif test == "chi":
                    ratios = stand_probka/len()
                    if stats.chisquare(stand_probka).pvalue < poziom_istotnosci:
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


sym = symulacja_testu("chi")

wy = plt.figure()
i = 0
for moc in sym:
    plt.plot(moc,label=str(liczby_danych[i]))
    i += 1
plt.legend()

plt.show()