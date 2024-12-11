
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Функция для генерации случайных данных и выполнения линейной регрессии
def generate_and_fit_model(n_columns = 3, n_rows = 30):
    # # Генерация случайных данных для X (факторные признаки) и Y (функциональный признак) нормального распределения
    # X = np.random.randn(n_rows, n_columns) * 10  # Значения факторных признаков
    # Y = np.random.randn(n_rows) * 10  # Значения функционального признака

    # Генерация данных для X (факторные признаки) с линейным распределением
    X = np.random.rand(n_rows, n_columns) * 10  # Факторные признаки равномерно распределены

    # Генерация линейной зависимости с добавлением шума
    true_coefficients = np.random.randn(n_columns)  # Истинные коэффициенты для линейной зависимости
    Y = X @ true_coefficients + np.random.randn(n_rows) * 0  # Линейная зависимость с шумом



    # Создание модели линейной регрессии
    model = LinearRegression()
    model.fit(X, Y)

    # Коэффициенты модели
    b0 = model.intercept_  # Свободный коэффициент
    b = model.coef_  # Коэффициенты при факторных признаках

    # Вывод коэффициентов в красивом виде
    coefficient_str = f"b0 = {b0:.2f}"
    for i, coeff in enumerate(b, start=1):
        coefficient_str += f", b{i} = {coeff:.2f}"

    # Предсказания модели
    Y_pred = model.predict(X)

    for i in range(n_columns):
        plt.figure(figsize=(10, 6))
        # Построение графика для первого столбца X
        plt.scatter(X[:, i], Y, color='blue', label='Фактические данные')  # Корреляционное поле
        plt.plot(X[:, i], Y_pred, color='red', label='Аппроксимирующая кривая')  # Линия аппроксимации
        plt.title('Корреляционное поле и аппроксимирующая кривая')
        plt.xlabel('Факторный признак X1')
        plt.ylabel('Функциональный признак Y')
        plt.legend()
        plt.grid(True)
        plt.show()

    return coefficient_str


