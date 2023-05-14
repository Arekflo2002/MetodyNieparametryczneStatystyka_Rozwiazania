import numpy as np
import scipy.stats as stats

import numpy as np

liczba_elementow = 100  # Liczba elementów w próbkach
stopnie_swobody = 2  # Liczba stopni swobody dla próbek

# Generowanie pierwszej próbki z rozkładu 𝜒^2 o liczbie stopni swobody stopnie_swobody
probka_1 = np.random.chisquare(stopnie_swobody, size=liczba_elementow)
wartosc_oczekiwana = np.mean(probka_1)

# Generowanie drugiej próbki z rozkładu 𝜒^2 o liczbie stopni swobody stopnie_swobody, o takiej samej wartości oczekiwanej
np.random.seed(42)  # Ustawienie seed'a dla powtarzalności wyników
probka_2 = np.random.chisquare(stopnie_swobody, size=liczba_elementow)
probka_2 = + probka_2 + (wartosc_oczekiwana - np.mean(probka_2))

# Wyświetlanie wyników

print("Wartość oczekiwana pierwszej próbki:", wartosc_oczekiwana)
print("Wartość oczekiwana drugiej próbki:", np.mean(probka_2))

