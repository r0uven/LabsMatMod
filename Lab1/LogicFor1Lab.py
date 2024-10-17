import tkinter as tk
import math
import matplotlib.pyplot as plt


# Функция вычисления выборочной средней
def evalSampleMean(randArr):
    return sum(randArr) / len(randArr)


# Функция вычисления оценки дисперсии
def evalEstimationOfVariance(sampleMean, randArr):
    res = []
    for i in range(len(randArr)):
        res.append((randArr[i] - sampleMean) ** 2)

    return sum(res) / (len(randArr) - 1)


# Функция вычисления координат образующихся интервалов
def evalOfCoordinatesOfTheResultingIntervals(randArr, minX, numberOfPlots_triangle):
    coordArr = []
    for i in range(len(randArr)):
        coordArr.append(minX + i * numberOfPlots_triangle)
    return coordArr


# Функция вычисления границ интервалов и эмпирических частот
def evalOf_intervalBoundaries_and_empiricalFrequencies(coordinatesOfTheResultingIntervals, randNumbersArray):
    intervalBoundaries = []
    empiricalFrequencies = []
    for i in range(len(randNumbersArray) - 1):
        intervalBoundaries.append((float('{:.3f}'.format(coordinatesOfTheResultingIntervals[i])), float('{:.3f}'.format(coordinatesOfTheResultingIntervals[i+1]))))
        empiricalFrequencies.append(i + 1 / len(randNumbersArray))
    return intervalBoundaries, empiricalFrequencies


# Функция вычисления значений статистического функции(ряда)
def evalOfvaluesOfTheStatisticalFunction(empiricalFrequencies):
    valuesOfTheStatisticalFunction = [0]
    for i in range(len(empiricalFrequencies)):
        valuesOfTheStatisticalFunction.append(
            empiricalFrequencies[i] + valuesOfTheStatisticalFunction[i])
    return valuesOfTheStatisticalFunction


# Функция для добавления данных в таблицу
def add_to_table(bound, investigating_parameter, num_columns, table):
    def reset_tableview():
        # Удаляем все строки
        for item in table.get_children():
            table.delete(item)

        # Сбрасываем столбцы к начальному состоянию (оставляем только скрытый столбец)
        table["columns"] = ("dummy",)
        table.heading("dummy", text="dummy")
        table.column("dummy", width=0, stretch=tk.NO)

    reset_tableview()

    existing_columns = table["columns"]  # Получаем существующие столбцы
    new_columns = []
    # Добавляем новые столбцы
    col_count = len(existing_columns)
    for i in range(num_columns):
        new_col = f"col{col_count + 1 + i}"
        new_columns.append(new_col)

    # Обновляем список столбцов в tableview
    table["columns"] = existing_columns + tuple(new_columns)

    # region Удаляем тот самый невидимый стобец который был нужен для инициализации таблицы
    existing_columns = list(table["columns"])  # Получаем существующие столбцы
    existing_columns.pop(0)  # Удаляем первый столбец (с индексом 1)
    table["columns"] = tuple(existing_columns)
    # endregion

    for new_col in new_columns:
        # Настройка нового столбца
        table.column(new_col, stretch=tk.NO, width=124)
        # Устанавливаем заголовки для каждого нового столбца
        table.heading(new_col, text="")
    table.column("col2", stretch=tk.NO,
                 width=140)  # Это столбец заголовков ему устанавливаем в частном порядке ширину поскольку она чуть шире других данных
    # Добавляем данные для отображения в таблицу
    table.insert("", "end", values=bound)
    table.insert("", "end", values=investigating_parameter)

def constructing_histograms(valuesOfTheStatisticalFunction):
    # Создаем фигуру и две оси (subplot)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))  # 1 ряд, 2 колонки

    # Первая гистограмма
    ax1.hist(valuesOfTheStatisticalFunction, bins=len(valuesOfTheStatisticalFunction), edgecolor='black', color='blue',
             alpha=0.7)
    ax1.set_title('Гистограмма статического распределения\n значений стат функц')

    # Вторая гистограмма
    indices = list(range(len(valuesOfTheStatisticalFunction)))
    unique_numbers = list(valuesOfTheStatisticalFunction)  # Уникальные значения чисел
    unique_numbers.sort()  # Сортируем их

    ax2.bar(indices, unique_numbers)
    ax2.set_title('Гистограмма значений стат функции')

    # Показываем график
    plt.tight_layout()  # Автоматически подгоняет отступы
    plt.get_current_fig_manager().window.wm_geometry('+1550+900')  # Задаем положение окна с гистограммами
    plt.show()


def calculation_of_characteristics_from_1_labs():
    # Чтение данных из файла и преобразование их в массив чисел
    with open("output.txt", "r") as file:
        randNumbersArray_FromFile = file.read().split(", ")  # Разбиваем строку на числа по запятой
    randNumbersArray_FromFile.pop()  # Убираем последний пустой элемент
    randNumbersArray_FromFile = list(map(float, randNumbersArray_FromFile))  # Преобразуем строковые значения в числа

    sampleMean = evalSampleMean(randNumbersArray_FromFile)  # выборочная средняя
    EstimationOfVariance = evalEstimationOfVariance(sampleMean, randNumbersArray_FromFile)  # оценка дисперсии


    numberOfPlots_triangle = (max(randNumbersArray_FromFile) - min(randNumbersArray_FromFile)) / (
            1 + 3.22 * math.log(len(randNumbersArray_FromFile)))  # буквально считаем тот самый треугольник
    coordinatesOfTheResultingIntervals = evalOfCoordinatesOfTheResultingIntervals(randNumbersArray_FromFile,
                                                                                  # координаты образующихся интервалов
                                                                                  min(randNumbersArray_FromFile),
                                                                                  numberOfPlots_triangle)
    # границы интервалов
    intervalBoundaries = evalOf_intervalBoundaries_and_empiricalFrequencies(coordinatesOfTheResultingIntervals, randNumbersArray_FromFile)[0]
    # эмпирические частоты
    empiricalFrequencies = evalOf_intervalBoundaries_and_empiricalFrequencies(coordinatesOfTheResultingIntervals, randNumbersArray_FromFile)[1]

    # добавляем в начало каждого массива(листа) заголовок данных, а также преобразуем границы интервалов в красивый для представления вид
    intervalBoundaries_ForTable = []
    intervalBoundaries_ForTable.append(f"Границы интервалов")
    for i in range(len(intervalBoundaries)):
        intervalBoundaries_ForTable.append(f"{intervalBoundaries[i][0]} -\n {intervalBoundaries[i][1]}")

    empiricalFrequencies_ForTable = empiricalFrequencies.copy()
    empiricalFrequencies_ForTable.insert(0, "Эмпирические частоты")



    valuesOfTheStatisticalFunction = evalOfvaluesOfTheStatisticalFunction(
        empiricalFrequencies)  # значения статистической функции(ряда)

    return {"sampleMean":sampleMean,
            "EstimationOfVariance":EstimationOfVariance,
            "coordinatesOfTheResultingIntervals":coordinatesOfTheResultingIntervals,
            "valuesOfTheStatisticalFunction":valuesOfTheStatisticalFunction,
            "intervalBoundaries":intervalBoundaries,
            "empiricalFrequencies":empiricalFrequencies,
            "intervalBoundaries_ForTable":intervalBoundaries_ForTable,
            "empiricalFrequencies_ForTable":empiricalFrequencies_ForTable}