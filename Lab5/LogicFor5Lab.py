import numpy as np
from scipy.stats import f
from Lab1.LogicFor1Lab import evalEstimationOfVariance
# np.random.seed(42)


# Генерация случайных данных для двух выборок
def generate_random_samples(mean1 = 10, std1 = 2, size1 = 30, mean2 = 12, std2 = 3, size2 = 30):
    """
    Генерирует две выборки случайных значений, подчиняющихся нормальному закону распределения.

    :param mean1: Среднее первой выборки
    :param std1: Стандартное отклонение первой выборки
    :param size1: Размер первой выборки
    :param mean2: Среднее второй выборки
    :param std2: Стандартное отклонение второй выборки
    :param size2: Размер второй выборки
    :return: Две выборки в виде массивов numpy
    """
    sample1 = np.random.normal(mean1, std1, size1)
    sample2 = np.random.normal(mean2, std2, size2)
    return sample1, sample2




def calculate_variance_ratio(sample1, sample2):
    """Вычисление отношения дисперсий."""
    s1, s2 = evalEstimationOfVariance(sample1), evalEstimationOfVariance(sample2)  # Выборочные дисперсии
    if s1 > s2:
        f_ratio = s1 / s2
    else:
        f_ratio = s2 / s1
    return f_ratio, s1, s2


def fisher_test(f_ratio, n1, n2, alpha):
    """Проверка гипотезы с использованием критерия Фишера."""
    dfn = n1 - 1  # Число степеней свободы в числителе
    dfd = n2 - 1  # Число степеней свободы в знаменателе
    critical_value = f.ppf(1 - alpha / 2, dfn, dfd)  # Критическое значение
    return critical_value


def testingHypothesisOfVariancesEquality():

    mean1, std1, size1 = 10, 2, 30  # Среднее, стандартное отклонение и размер первой выборки
    mean2, std2, size2 = 12, 3, 30  # Для второй выборки

    sample1, sample2 = generate_random_samples(mean1, std1, size1, mean2, std2, size2)

    if len(sample1) < 2 or len(sample2) < 2:
        print("Размер каждой выборки должен быть не меньше 2!")
        return

    # Уровень значимости
    alpha = 0.05

    # Вычисление отношения дисперсий
    f_ratio, s1, s2 = calculate_variance_ratio(sample1, sample2)
    sampleVarianceOfTheFirstSample = f"\nВыборочная дисперсия первой выборки: {s1:.4f}"
    sampleVarianceOfTheSecondSample = f"\nВыборочная дисперсия второй выборки: {s2:.4f}"
    varianceRatio = f"\nОтношение дисперсий (F-статистика): {f_ratio:.4f}"

    # Проверка гипотезы
    critical_value = fisher_test(f_ratio, len(sample1), len(sample2), alpha)
    criticalValueF = f"\nКритическое значение F: {critical_value:.4f}"

    # Принятие или отклонение гипотезы
    if f_ratio > critical_value:
        res  = "\n\nГипотеза о равенстве дисперсий отвергается (дисперсии не равны)."
    else:
        res = "\n\nГипотеза о равенстве дисперсий не отвергается (дисперсии равны)."

    return sampleVarianceOfTheFirstSample+sampleVarianceOfTheSecondSample+varianceRatio+criticalValueF+res