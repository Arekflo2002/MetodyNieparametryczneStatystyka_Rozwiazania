import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# ustalamy parametry symulacji
np.random.seed(seed=123)

n = 200

# plt.hist(x, bins=10)
# plt.show()
odsetek = 0
for i in range(400):
    x = stats.t.rvs(size=n,df=1)
    x = stats.t.cdf(x,df=1)
    y = stats.uniform.rvs(size=n)
    # plt.plot(y)
    # plt.show()
    if stats.kstest(x,'uniform').pvalue<0.05: odsetek +=1 


print(odsetek/400)