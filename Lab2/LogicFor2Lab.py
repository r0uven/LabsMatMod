from Lab1 import LogicFor1Lab  # Импорт логики для лабораторной 1


# Функция вычисления коэффициента асимметрии
def eval_of_asymmetry_coefficient(randNumbersArray_FromFile, sampleMean, standardDeviation):
    """
    Вычисляет коэффициент асимметрии для массива случайных чисел.
    """
    res = []

    for i in range(len(randNumbersArray_FromFile)):
        # Отклонение от среднего возводим в куб
        res.append((randNumbersArray_FromFile[i] - sampleMean) ** 3)

    # Возвращаем сумму с поправкой на количество элементов
    # Умножаем на дисперсию в кубе для нормализации
    return sum(res) / ((len(randNumbersArray_FromFile) - 1) * (
                standardDeviation ** 3))


# Функция вычисления эксцесса
def eval_of_excess(randNumbersArray_FromFile, sampleMean, standardDeviation):
    """
    Вычисляет эксцесс для массива случайных чисел.
    """
    res = []

    for i in range(len(randNumbersArray_FromFile)):
        # Отклонение от среднего возводим в четвертую степень
        res.append((randNumbersArray_FromFile[i] - sampleMean) ** 4)

    # Вычисляем эксцесс с поправкой на количество элементов
    # Вычитаем 3 для нормализации относительно нормального распределения
    return (sum(res) / ((len(randNumbersArray_FromFile) - 1) * (
                standardDeviation ** 4))) - 3


# Функция для вычисления характеристик 2 лабораторной
def calculation_of_characteristics_from_2_labs(valuesFrom1Lab):
    """
    Вычисляет коэффициент асимметрии и эксцесс на основе данных из файла output.txt
    и обновляет переданные метки на интерфейсе.
    """
    sampleMean = valuesFrom1Lab['sampleMean']
    standardDeviation = valuesFrom1Lab['standardDeviation']
    randNumbersArray_FromFile = valuesFrom1Lab['randNumbersArray_FromFile']

    # Вычисление коэффициента асимметрии
    asymmetry_coefficient = eval_of_asymmetry_coefficient(randNumbersArray_FromFile, sampleMean, standardDeviation)

    # Вычисление эксцесса
    excess = eval_of_excess(randNumbersArray_FromFile, sampleMean, standardDeviation)


    return {"asymmetry_coefficient":asymmetry_coefficient,
            "excess":excess}