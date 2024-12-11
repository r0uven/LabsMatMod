# Импорт необходимых библиотек
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Функция для генерации случайных данных и выполнения линейной регрессии
def generate_and_fit_model(n_columns, n_rows):
    # # Генерация случайных данных для X (факторные признаки) и Y (функциональный признак)
    # X = np.random.randn(n_rows, n_columns) * 10  # Значения факторных признаков
    # Y = np.random.randn(n_rows) * 10  # Значения функционального признака

    # Генерация данных для X (факторные признаки) с равномерным распределением
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

    # Предсказания модели
    Y_pred = model.predict(X)
    for i in range(n_columns):

        # Построение графика для первого столбца X
        plt.scatter(X[:, i], Y, color='blue', label='Фактические данные')  # Корреляционное поле
        plt.plot(X[:, i], Y_pred, color='red', label='Аппроксимирующая кривая')  # Линия аппроксимации
        plt.title('Корреляционное поле и аппроксимирующая кривая')
        plt.xlabel('Факторный признак X1')
        plt.ylabel('Функциональный признак Y')
        plt.legend()
        plt.grid(True)
        plt.show()

    return b0, b


# Пример: количество столбцов и строк, введённых пользователем
n_columns = 1  # Количество факторных признаков
n_rows = 100 # Количество наблюдений

# Вызов функции для генерации данных и выполнения регрессии
generate_and_fit_model(n_columns, n_rows)
