import numpy as np
from scipy.stats import chi2, kstest, chisquare
import matplotlib.pyplot as plt

# liczba danych
n = [100, 500, 1000]

# liczba stopni swobody
k = [2, 5, 10]

# poziom istotności
alpha = 0.05

# generowanie danych i przeprowadzenie testów
for i in range(len(n)):
    for j in range(len(k)):
        # generowanie danych z rozkładu chi-squared
        data = np.random.chisquare(k[j], size=n[i])
        
        # test Kołmogorowa
        ks_stat, ks_pvalue = kstest(data, 'chi2', args=(k[j],))
        ks_reject = ks_pvalue < alpha
        
        # test chi-square
        chi2_stat, chi2_pvalue = chisquare(data)
        chi2_reject = chi2_pvalue < alpha
        
        # test PIT
        norm_data = np.sqrt(2*k[j]) * np.sin(np.pi*data/(2*k[j]))
        pit_ks_stat, pit_ks_pvalue = kstest(norm_data, 'norm')
        pit_ks_reject = pit_ks_pvalue < alpha
        pit_chi2_stat, pit_chi2_pvalue = chisquare(norm_data)
        pit_chi2_reject = pit_chi2_pvalue < alpha
        
        # wykresy
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
        
        # histogram danych
        ax = axes[0, 0]
        ax.hist(data, bins=20, density=True)
        ax.set_title('Histogram danych')
        ax.set_xlabel('Wartości')
        ax.set_ylabel('Częstość')
        
        # dystrybuanta i funkcja gęstości teoretycznej rozkładu chi-kwadrat
        ax = axes[0, 1]
        x = np.linspace(chi2.ppf(0.01, k[j]), chi2.ppf(0.99, k[j]), 100)
        ax.plot(x, chi2.pdf(x, k[j]), 'r-', lw=2, alpha=0.6, label='Rozkład teoretyczny')
        ax.hist(data, bins=20, density=True, cumulative=True, histtype='step', label='Dystrybuanta empiryczna')
        ax.set_title('Test Kołmogorowa')
        ax.set_xlabel('Wartości')
        ax.set_ylabel('Prawdopodobieństwo')
        ax.legend(loc='best')
        ax.annotate('p = {:.3f}'.format(ks_pvalue), xy=(0.05, 0.95), xycoords='axes fraction', fontsize=12, ha='left', va='top', bbox=dict(facecolor='white', alpha=0.8))
         # histogram przekształconych danych
        ax = axes[1, 0]
        ax.hist(norm_data, bins=20, density=True)
        ax.set_title('Histogram przekształconych danych')
        ax.set_xlabel('Wartości')
        ax.set_ylabel('Częstość')
        
        # dystrybuanta i funkcja gęstości teoretycznej rozkładu normalnego
        ax = axes[1, 1]
        x = np.linspace(-5, 5, 100)
        ax.plot(x, chi2.pdf(np.arcsin(x/np.sqrt(2*k[j]))*2*k[j]/np.pi, k[j]), 'r-', lw=2, alpha=0.6, label='Rozkład teoretyczny')
        ax.hist(norm_data, bins=20, density=True, cumulative=True, histtype='step', label='Dystrybuanta empiryczna')
        ax.set_title('Test Kołmogorowa z wykorzystaniem PIT')
        ax.set_xlabel('Wartości')
        ax.set_ylabel('Prawdopodobieństwo')
        ax.legend(loc='best')
        ax.annotate('p = {:.3f}'.format(pit_ks_pvalue), xy=(0.05, 0.95), xycoords='axes fraction', fontsize=12, ha='left', va='top', bbox=dict(facecolor='white', alpha=0.8))

        # tytuł i zapisanie wykresów
        fig.suptitle('n = {}, k = {}'.format(n[i], k[j]))
        fig.tight_layout(rect=[0, 0, 1, 0.95])
        plt.savefig('n{}_k{}.png'.format(n[i], k[j]))