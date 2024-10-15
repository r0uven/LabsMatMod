from Lab1 import LogicFor1Lab  # Импорт логики для лабораторной 1


# Функция вычисления коэффициента асимметрии
def eval_of_asymmetry_coefficient(randNumbersArray_FromFile):
    """
    Вычисляет коэффициент асимметрии для массива случайных чисел.
    """
    res = []
    sampleMean = LogicFor1Lab.evalSampleMean(randNumbersArray_FromFile)  # Среднее выборки
    for i in range(len(randNumbersArray_FromFile)):
        # Отклонение от среднего возводим в куб
        res.append((randNumbersArray_FromFile[i] - sampleMean) ** 3)

    # Возвращаем сумму с поправкой на количество элементов
    # Умножаем на дисперсию в кубе для нормализации
    return sum(res) / ((len(randNumbersArray_FromFile) - 1) * (
                LogicFor1Lab.evalEstimationOfVariance(sampleMean, randNumbersArray_FromFile) ** 3))


# Функция вычисления эксцесса
def eval_of_excess(randNumbersArray_FromFile):
    """
    Вычисляет эксцесс для массива случайных чисел.
    """
    res = []
    sampleMean = LogicFor1Lab.evalSampleMean(randNumbersArray_FromFile)  # Среднее выборки
    for i in range(len(randNumbersArray_FromFile)):
        # Отклонение от среднего возводим в четвертую степень
        res.append((randNumbersArray_FromFile[i] - sampleMean) ** 4)

    # Вычисляем эксцесс с поправкой на количество элементов
    # Вычитаем 3 для нормализации относительно нормального распределения
    return (sum(res) / ((len(randNumbersArray_FromFile) - 1) * (
                LogicFor1Lab.evalEstimationOfVariance(sampleMean, randNumbersArray_FromFile) ** 4))) - 3


# Функция для вычисления характеристик из двух лабораторных
def calculation_of_characteristics_from_2_labs(asymmetry_coefficient_label, excess_label):
    """
    Вычисляет коэффициент асимметрии и эксцесс на основе данных из файла output.txt
    и обновляет переданные метки на интерфейсе.
    """
    # Чтение данных из файла и преобразование их в массив чисел
    with open("output.txt", "r") as file:
        randNumbersArray_FromFile = file.read().split(", ")  # Разбиваем строку на числа по запятой

    randNumbersArray_FromFile.pop()  # Убираем последний пустой элемент, если он есть
    randNumbersArray_FromFile = list(map(float, randNumbersArray_FromFile))  # Преобразуем строковые значения в числа

    # Вычисление коэффициента асимметрии
    asymmetry_coefficient = eval_of_asymmetry_coefficient(randNumbersArray_FromFile)

    # Вычисление эксцесса
    excess = eval_of_excess(randNumbersArray_FromFile)

    # Обновляем метки на интерфейсе с новыми значениями
    asymmetry_coefficient_label.config(text=f"Коэффициент асимметрии(A) = {asymmetry_coefficient:.5f}")
    excess_label.config(text=f"Эксцесс(E) =  {excess:.5f}")
