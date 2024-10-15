import os
import tkinter as tk
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from Lab2 import LogicFor2Lab  # Импорт логики для лабораторной 2


# Класс обработчика событий изменения файла
class WatcherHandler(FileSystemEventHandler):
    def __init__(self, labclass):
        """
        Конструктор для передачи ссылки на класс lab2ClassInterface.
        Это позволит обновлять интерфейс при изменении файла.
        """
        self.labclass = labclass  # Сохраняем ссылку на экземпляр интерфейса

    def on_modified(self, event):
        """
        Метод вызывается при изменении файла.
        Если это не директория, обновляем данные в метках интерфейса.
        """
        if not event.is_directory:
            print(f"Файл изменён: {event.src_path}")
            # Вызываем пересчет характеристик и обновление меток
            LogicFor2Lab.calculation_of_characteristics_from_2_labs(
                self.labclass.asymmetry_coefficient_label,
                self.labclass.excess_label
            )


# Функция для запуска наблюдателя в отдельном потоке
def start_file_monitoring(file_path, labclass):
    """
    Функция для мониторинга изменений файла.
    Она запускается в отдельном потоке, чтобы основное приложение не зависало.
    """
    # Преобразуем путь к файлу в абсолютный
    file_path_absolute = os.path.abspath(file_path)

    # Получаем директорию файла для наблюдателя
    file_dir = os.path.dirname(file_path_absolute)

    # Создаем обработчик событий и передаем ему ссылку на интерфейс
    event_handler = WatcherHandler(labclass)

    # Создаем наблюдателя и прикрепляем к нему обработчик
    observer = Observer()
    observer.schedule(event_handler, path=file_dir, recursive=False)

    # Запускаем наблюдателя
    observer.start()

    # Бесконечный цикл для поддержания работы наблюдателя
    try:
        while True:
            time.sleep(1)  # Задержка для снижения нагрузки на процессор
    except KeyboardInterrupt:
        # Останавливаем наблюдателя при завершении программы
        observer.stop()

    observer.join()  # Ждем завершения потока наблюдателя


# Класс интерфейса для лабораторной 2
class lab2ClassInterface(tk.Frame):
    def __init__(self, parent, controller):
        """
        Конструктор класса интерфейса для лабораторной 2.
        Создает метки для отображения коэффициентов и вызывает функцию для расчета.
        """
        super().__init__(parent)

        # Контейнер для центрирования элементов интерфейса
        container = tk.Frame(self)
        container.pack(anchor=tk.CENTER, expand=True, pady=20)

        # Метка для отображения коэффициента асимметрии
        self.asymmetry_coefficient_label = tk.Label(container, font=("Arial", 21))
        self.asymmetry_coefficient_label.pack(pady=20)

        # Метка для отображения коэффициента эксцесса
        self.excess_label = tk.Label(container, font=("Arial", 21))
        self.excess_label.pack(pady=20)

        # Инициализируем расчет характеристик сразу при создании интерфейса
        LogicFor2Lab.calculation_of_characteristics_from_2_labs(
            self.asymmetry_coefficient_label,
            self.excess_label
        )
