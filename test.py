import numpy as np

# Definiuj stopnie swobody dla dwóch próbek
df1 = np.random.randint(1, 10)  # Losowe stopnie swobody dla próbki 1
df2 = np.random.randint(1, 10)  # Losowe stopnie swobody dla próbki 2
num_samples = 100

# Generuj dwie próbki z rozkładu chi-kwadrat
samples1 = np.random.chisquare(df1, num_samples)
samples2 = np.random.chisquare(df2, num_samples)

# Oblicz wartości oczekiwane dla obu próbek
mean1 = np.mean(samples1)
mean2 = np.mean(samples2)

# Przesuń próbki, aby miały równą wartość oczekiwaną
shifted_samples1 = samples1 - mean1 + mean2
shifted_samples2 = samples2

# Sprawdź wartości oczekiwane przesuniętych próbek
shifted_mean1 = np.mean(shifted_samples1)
shifted_mean2 = np.mean(shifted_samples2)

print("Stopnie swobody próbki 1:", df1)
print("Stopnie swobody próbki 2:", df2)
print("Wartość oczekiwana próbki 1:", mean1)
print("Wartość oczekiwana próbki 2:", mean2)
print("Przesunięta wartość oczekiwana próbki 1:", shifted_mean1)
print("Przesunięta wartość oczekiwana próbki 2:", shifted_mean2)
print("Przesunięte próbki 1:", shifted_samples1)
print("Przesunięte próbki 2:", shifted_samples2)
