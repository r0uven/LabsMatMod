import numpy as np

data = [2, 4, 6, 8]
sample_variance = np.var(data, ddof=1)
std_dev = np.var(data, ddof=0)

n = 4
print(np.sqrt(4))
print("Выборочная дисперсия:", sample_variance)
print("Обычная дисперсия:", std_dev)
