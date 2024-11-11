import scipy.stats as stats


def testingTheHypothesis(valuesFrom1Lab, valuesFrom3Lab):
    amountOfNumbersAtIntervals = valuesFrom1Lab['amountOfNumbersAtIntervals']
    randNumbersArray_FromFile = valuesFrom1Lab['randNumbersArray_FromFile']
    theoreticalFrequencies = valuesFrom3Lab['theoreticalFrequencies']

    criterionPearson = 0
    for i in range(len(theoreticalFrequencies)):
        criterionPearson += ((amountOfNumbersAtIntervals.get(i, 0)-len(randNumbersArray_FromFile)*theoreticalFrequencies[i])**2)/(len(randNumbersArray_FromFile)*theoreticalFrequencies[i])

    k = len(randNumbersArray_FromFile) - 1 # число степеней свободы
    alpha = 0.05  # уровень значимости

    # Табличное значение критерия Пирсона
    critical_value = stats.chi2.ppf(1 - alpha, k)

    if criterionPearson > critical_value:
        return "Гипотезу отвергаем: распределение не нормальное."
    else:
        return "Гипотезу принимаем: распределение нормальное."