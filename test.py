import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# ustalamy parametry symulacji
n_simulations = 400
degrees_of_freedom = [1, 2, 5, 10, 20, 50, 100]

# ustalamy poziom istotności dla testu chi-kwadrat
alpha = 0.05

# tworzymy listy do przechowywania wyników symulacji
rejections = []
p_values = []

# dla każdego stopnia swobody wykonujemy symulacje i zapisujemy wyniki
for k in degrees_of_freedom:
    rejection_count = 0
    for i in range(n_simulations):
        # generujemy próbki z rozkładu chi-kwadrat o k stopniach swobody
        data = np.random.chisquare(k, size=100)
        # wykonujemy test chi-kwadrat i zapisujemy wynik
        _, p = stats.chisquare(data, f_exp=np.full_like(data, np.mean(data)))
        p_values.append(p)
        if p < alpha:
            rejection_count += 1
    rejections.append(rejection_count / n_simulations)

# rysujemy wykres
plt.plot(degrees_of_freedom, rejections)
plt.xlabel('Stopnie swobody')
plt.ylabel('Odsetek odrzuceń')
plt.title('Test chi-kwadrat dla rozkładu chi-kwadrat')
plt.show()
