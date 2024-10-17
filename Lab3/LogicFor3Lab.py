import numpy as np
from scipy.stats import norm
from Lab1.LogicFor1Lab import add_to_table


def eval_theoretical_frequencies(intervalBoundaries):


    # 1. Рассчитаем выборочную среднюю и стандартное отклонение
    mean = np.mean(intervalBoundaries)
    std_dev = np.std(intervalBoundaries, ddof=1)

    # 2. Вычисляем вероятности для интервалов
    probabilities = []
    probabilities.append("Теоретические частоты") # заголовок данных
    for i in range(len(intervalBoundaries) - 1):
        z_i = (intervalBoundaries[i][0] - mean) / std_dev
        z_next = (intervalBoundaries[i][1] - mean) / std_dev
        # Вычисляем вероятность попадания в интервал
        prob = norm.cdf(z_next) - norm.cdf(z_i)
        probabilities.append("{:.5f}".format(prob))
    return probabilities



def calculation_of_characteristics_from_3_labs(intervalBoundaries_ForTable,intervalBoundaries, table):

    theoreticalFrequencies = eval_theoretical_frequencies(intervalBoundaries)

    add_to_table(intervalBoundaries_ForTable, theoreticalFrequencies, len(theoreticalFrequencies), table)


