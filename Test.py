import numpy as np
from scipy.stats import norm

# Параметры нормального распределения
mu = 0  # математическое ожидание
sigma = 1  # стандартное отклонение (корень из дисперсии)

# Границы интервала
a = -1
b = 1

# Вычисление функции распределения (CDF) для границ
P_a = norm.cdf(a, mu, sigma)
P_b = norm.cdf(b, mu, sigma)

# Вероятность попадания на интервал [a, b]
probability = P_b - P_a

print(f'Вероятность попадания на интервал [{a}, {b}]: {probability:.4f}')
