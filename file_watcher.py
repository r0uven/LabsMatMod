#region этот файл не используется поскольку принято другое решение
# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import os
#
# from Lab2.Lab2Interface import lab2ClassInterface
#
#
# # Класс обработчика событий изменения файла
# class WatcherHandler(FileSystemEventHandler):
#     def __init__(self, labclass):
#         """
#         Конструктор для передачи ссылки на класс lab2ClassInterface.
#         Это позволит обновлять интерфейс при изменении файла.
#         """
#         self.labclass = labclass
#         self.labClassName = type(self.labclass).__name__# Сохраняем ссылку на экземпляр интерфейса
#
#     def on_modified(self, event):
#         """
#         Метод вызывается при изменении файла.
#         Если это не директория, обновляем данные в метках интерфейса.
#         """
#         if not event.is_directory:
#             print(f"Файл изменён: {event.src_path}")
#             # Вызываем пересчет характеристик и обновление меток из 2 лабы
#             match self.labClassName:
#                 case 'lab2ClassInterface':
#                     lab2ClassInterface.on_initialize()
#
#
# # Функция для запуска наблюдателя в отдельном потоке
# def start_file_monitoring(file_path, labclass):
#     """
#     Функция для мониторинга изменений файла.
#     Она запускается в отдельном потоке, чтобы основное приложение не зависало.
#     """
#     # Преобразуем путь к файлу в абсолютный
#     file_path_absolute = os.path.abspath(file_path)
#
#     # Получаем директорию файла для наблюдателя
#     file_dir = os.path.dirname(file_path_absolute)
#
#     # Создаем обработчик событий и передаем ему ссылку на интерфейс
#     event_handler = WatcherHandler(labclass)
#
#     # Создаем наблюдателя и прикрепляем к нему обработчик
#     observer = Observer()
#     observer.schedule(event_handler, path=file_dir, recursive=False)
#
#     # Запускаем наблюдателя
#     observer.start()
#
#     # Бесконечный цикл для поддержания работы наблюдателя
#     try:
#         while True:
#             time.sleep(1)  # Задержка для снижения нагрузки на процессор
#     except KeyboardInterrupt:
#         # Останавливаем наблюдателя при завершении программы
#         observer.stop()
#
#     observer.join()  # Ждем завершения потока наблюдателя
#endregion
# # Функция для запуска наблюдателя в отдельном потоке
            # file_path = "output.txt"
            # # Создаем поток для мониторинга изменений файла
            # file_monitor_thread = threading.Thread(target=start_file_monitoring, args=(file_path, self.frames[frame_name]))
            # file_monitor_thread.daemon = True  # Поток будет завершен, если основной поток завершится
            # file_monitor_thread.start()