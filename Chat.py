import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2, chisquare

# parametry rozkladu chi-kwadrat
df = 3

# zakres liczby stopni swobody
df_range = np.arange(1, 50)

# pusta tablica na wyniki
rejection_rate = np.empty_like(df_range, dtype=float)

# iteracja po liczbie stopni swobody
for i, df_val in enumerate(df_range):
    # inicjalizacja licznika odrzuceń hipotezy zerowej
    rejected = 0
    # powtórzenie testu hipotezy wielokrotnie
    for j in range(500):
        # generowanie próby z rozkładu chi-kwadrat
        sample = chi2.rvs(df_val, size=100)
        # testowanie hipotezy zerowej
        _, p = chisquare(sample, np.ones(100)*10)
        # odrzucenie hipotezy zerowej, jeśli wartość p jest mniejsza niż 0.05
        if p < 0.05:
            rejected += 1
    # obliczenie odsetka odrzuceń hipotezy zerowej
    rejection_rate[i] = rejected / 1000

# rysowanie wykresu odsetka odrzuceń
plt.plot(df_range, rejection_rate)
plt.xlabel('Stopnie swobody')
plt.ylabel('Odsetek odrzucenia H0')
plt.title('Wykres odsetka odrzucenia hipotezy zerowej')
plt.show()