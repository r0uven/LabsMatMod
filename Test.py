import numpy as np
import scipy.stats as stats
import pandas as pd

# Параметры нормального распределения
mu, sigma = 0, 1  # среднее и стандартное отклонение

# Генерация выборки
n = 1000  # размер выборки
data = np.random.normal(mu, sigma, n)

# Определение интервалов
num_bins = 10
hist, bin_edges = np.histogram(data, bins=num_bins)

# Вычисление эмпирических частот
empirical_freqs = hist / n

# Вычисление теоретических частот
bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
theoretical_freqs = stats.norm.pdf(bin_centers, mu, sigma) * n * (bin_edges[1] - bin_edges[0])

# Формирование таблицы результатов
results_table = pd.DataFrame({
    'Интервал': [f"{bin_edges[i]} - {bin_edges[i+1]}" for i in range(len(bin_edges)-1)],
    'Теоретические частоты': theoretical_freqs,
    'Эмпирические частоты': hist
})

print(results_table)

# Расчет критерия Пирсона
chi_squared_stat = np.sum((hist - theoretical_freqs) ** 2 / theoretical_freqs)
dof = num_bins - 1 - 1  # число степеней свободы (число интервалов - 1 - число параметров оцененных)
alpha = 0.05  # уровень значимости

# Табличное значение критерия Пирсона
critical_value = stats.chi2.ppf(1 - alpha, dof)

# Результаты
print(f"Статистика критерия Пирсона: {chi_squared_stat:.4f}")
print(f"Критическое значение для уровня значимости {alpha}: {critical_value:.4f}")

if chi_squared_stat > critical_value:
    print("Гипотезу отвергаем: распределение не нормальное.")
else:
    print("Гипотезу принимаем: распределение нормальное.")