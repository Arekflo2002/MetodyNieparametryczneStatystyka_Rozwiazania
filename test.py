import numpy as np
from scipy.stats import chi2, kstest
import matplotlib.pyplot as plt

n_simulations = 500  # ilość symulacji
df_values = np.arange(1, 21)  # wartości stopni swobody do przetestowania
alpha = 0.05  # poziom istotności testu

results = np.zeros((n_simulations, len(df_values)))  # tablica wyników

for i in range(n_simulations):
    for j, df in enumerate(df_values):
        sample = chi2.rvs(df=df, size=100)  # wygeneruj próbkę z rozkładu chi-kwadrat
        ks_statistic, p_value = kstest(sample, chi2.cdf, args=(df,))  # wykonaj test Kołmogorowa
        results[i, j] = p_value < alpha  # zapisz wynik testu (czy hipoteza zostala odrzucona?)

power = 1 - np.mean(results, axis=0)  # oblicz odsetek nieodrzuconych hipotez

# wykres
plt.plot(df_values, power)
plt.xlabel('Stopnie swobody')
plt.ylabel('Odsetek nieodrzuconych hipotez')
plt.title('Błąd I rodzaju w teście Kołmogorowa dla rozkładu chi-kwadrat')
plt.show()