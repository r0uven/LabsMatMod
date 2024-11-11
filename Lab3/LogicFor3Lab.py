import numpy as np
from scipy.stats import norm



def eval_theoretical_frequencies(coordinatesOfTheResultingIntervals):

    # 1. Рассчитаем выборочную среднюю и стандартное отклонение
    mean = np.mean(coordinatesOfTheResultingIntervals)
    std_dev = np.std(coordinatesOfTheResultingIntervals, ddof=1)

    # 2. Вычисляем вероятности для интервалов
    probabilitiesForTable = []
    probabilities = []
    probabilitiesForTable.append("Теоретические частоты") # заголовок данных
    for i in range(len(coordinatesOfTheResultingIntervals) - 1):
        z_i = (coordinatesOfTheResultingIntervals[i] - mean) / std_dev
        z_next = (coordinatesOfTheResultingIntervals[i + 1] - mean) / std_dev
        # Вычисляем вероятность попадания в интервал
        prob = norm.cdf(z_next) - norm.cdf(z_i)
        probabilitiesForTable.append("{:.5f}".format(prob))
        probabilities.append(prob)
    return probabilitiesForTable, probabilities



def calculation_of_characteristics_from_3_labs(valuesFrom1Lab):
    coordinatesOfTheResultingIntervals = valuesFrom1Lab['coordinatesOfTheResultingIntervals']

    theoreticalFrequenciesForTable, theoreticalFrequencies  = eval_theoretical_frequencies(coordinatesOfTheResultingIntervals)
    return {"theoreticalFrequencies":theoreticalFrequencies,
            'theoreticalFrequenciesForTable': theoreticalFrequenciesForTable}