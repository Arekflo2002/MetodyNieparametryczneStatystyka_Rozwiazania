import numpy as np
from scipy.stats import shapiro, kstest, chisquare
import matplotlib.pyplot as plt

# Ustawienia symulacji
n_reps = 500  # Liczba powtórzeń dla każdej kombinacji parametrów
sample_sizes = [20, 50, 100, 500]  # Rozmiary próbki do wygenerowania
dfs = [3, 5, 10, 20]  # Stopnie swobody do symulacji

# Inicjalizacja tablic przechowujących wyniki testów
sw_powers = np.zeros((len(sample_sizes), len(dfs)))
ks_powers = np.zeros((len(sample_sizes), len(dfs)))
chi2_powers = np.zeros((len(sample_sizes), len(dfs)))

# Przeprowadzenie symulacji
for i, n in enumerate(sample_sizes):
    for j, df in enumerate(dfs):
        for k in range(n_reps):
            # Generowanie próbki z rozkładu t-Studenta
            data = np.random.standard_t(df, size=n)
            # Standaryzacja danych
            data = (data - np.mean(data)) / np.std(data)

            # Test Shapiro-Wilka
            stat_sw, p_sw = shapiro(data)
            if p_sw <= 0.05:
                sw_powers[i, j] += 1

            # Test Kołmogorowa
            stat_ks, p_ks = kstest(data, 'norm')
            if p_ks <= 0.05:
                ks_powers[i, j] += 1

            # Test 𝜒2
            freq, _ = np.histogram(data, bins='auto')
            stat_chi, p_chi = chisquare(freq)
            if p_chi <= 0.05:
                chi2_powers[i, j] += 1

# Normalizacja wyników jako proporcje sukcesów
sw_powers /= n_reps
ks_powers /= n_reps
chi2_powers /= n_reps

# Tworzenie wykresów
for i, n in enumerate(sample_sizes):
    plt.subplot(2, 2, i+1)
    plt.plot(dfs, sw_powers[i], label='Shapiro-Wilk')
    plt.plot(dfs, ks_powers[i], label='Kolmogorov-Smirnov')
    plt.plot(dfs, chi2_powers[i], label='Chi-square')
    plt.legend()
    plt.title(f'n={n}')
    plt.xlabel('Stopnie swobody')
    plt.ylabel('Moc testu')
    plt.ylim([0, 1])
    plt.xticks(dfs)

plt.tight_layout()
plt.show()