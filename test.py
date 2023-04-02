import numpy as np
from scipy.stats import chisquare

# observed data
observed_data = np.array([10, 20, 30, 25, 15])

# expected data assuming a uniform distribution
n = len(observed_data)
expected_data = np.array([n/5] * 5)

print(expected_data)