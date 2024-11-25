import math

import numpy as np
from Lab1.LogicFor1Lab import evalSampleMean, evalEstimationOfVariance


# Генерация случайных данных для n выборок
def generate_random_samples(*params):
    """
    Генерирует несколько выборок случайных значений, подчиняющихся нормальному закону распределения.

    :param params: Параметры для каждой выборки, представленные в виде кортежей (mean, std, size).
                   Например: (mean1, std1, size1), (mean2, std2, size2), ...
    :return: Список массивов numpy, содержащих выборки.
    """
    samples = []
    for mean, std, size in params:
        sample = np.random.normal(mean, std, size)
        samples.append(sample)
    return samples

# Функция для формирования выводов о зависимости
def dependency_comment(r):
    if abs(r) == 1:
        return "Между переменными существует строгая функциональная связь."
    elif r == 0:
        return "Переменные статистически независимы."
    else:
        return f"Степень зависимости: {r:.2f}."

# Функция для вычисления коэффициента корреляции между двумя переменными
def correlation_coefficient(x, y):
    n = len(x)
    mean_x = evalSampleMean(x)
    mean_y = evalSampleMean(y)

    covariance = np.sum((x - mean_x) * (y - mean_y)) / (n - 1)
    std_x = math.sqrt(evalEstimationOfVariance(x))
    std_y = math.sqrt(evalEstimationOfVariance(y))

    return covariance / (std_x * std_y)

def correlationAnalysis():

    # Пример использования
    mean1, std1, size1 = 10, 2, 30
    mean2, std2, size2 = 12, 3, 30
    mean3, std3, size3 = 14, 1.5, 30

    # Генерация трёх выборок
    x, y, z = generate_random_samples((mean1, std1, size1), (mean2, std2, size2), (mean3, std3, size3))

    # Вычисление коэффициентов корреляции
    r_xy = correlation_coefficient(x, y)
    r_xz = correlation_coefficient(x, z)
    r_yz = correlation_coefficient(y, z)

    # Матрица корреляций
    correlation_matrix = np.array([
        [1, r_xy, r_xz],
        [r_xy, 1, r_yz],
        [r_xz, r_yz, 1]
    ])

    # Формирование вывода в строковую переменную
    output = ""

    # Добавляем матрицу корреляций в вывод
    output += "\nМатрица коэффициентов парных корреляций:\n"

    # Форматируем матрицу с точностью до 3 знаков после запятой для всех, кроме диагонали
    for i, row in enumerate(correlation_matrix):
        formatted_row = []
        for j, value in enumerate(row):
            if i == j:
                formatted_row.append(f"{int(value):>11d}")  # Для диагональных элементов (1) - целое число
            else:
                formatted_row.append(f"{value:>8.3f}")  # Для остальных элементов - число с тремя знаками
        output += " | ".join(formatted_row) + "\n"

    # Добавляем выводы в строку
    output += "\nВыводы:\n"
    output += f"Корреляция X и Y: {dependency_comment(r_xy)}\n"
    output += f"Корреляция X и Z: {dependency_comment(r_xz)}\n"
    output += f"Корреляция Y и Z: {dependency_comment(r_yz)}\n"

    return output
