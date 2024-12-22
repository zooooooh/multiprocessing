import numpy as np
import concurrent.futures
import time

# Функция для нахождения минимального элемента в строках матрицы с использованием векторизации
def find_row_min(start_idx, end_idx, matrix):
    return np.min(matrix[start_idx:end_idx], axis=1)

# Основная функция, которая выполняет параллельный поиск максимума среди минимальных элементов строк
def parallel_max_of_row_mins(matrix):
    N, M = matrix.shape  # Получаем размеры матрицы (N — количество строк, M — количество столбцов)
    p = 6  # Количество параллельных процессов (например, 6 ядер)

    # Определяем размер блока для разделения матрицы на части
    chunk_size = N // p
    futures = []  # Список для хранения задач

    # Создаем пул процессов с заданным количеством потоков (p)
    with concurrent.futures.ProcessPoolExecutor(max_workers=p) as executor:
        # Разбиваем матрицу на части и передаем на обработку
        for i in range(p):
            start_idx = i * chunk_size
            end_idx = (i + 1) * chunk_size if i < p - 1 else N
            # Добавляем задачу в пул для обработки текущего блока
            futures.append(executor.submit(find_row_min, start_idx, end_idx, matrix))

        # Собираем минимальные элементы строк для каждой части
        row_mins = np.concatenate([future.result() for future in concurrent.futures.as_completed(futures)])

    # Находим максимальное значение среди минимальных элементов строк
    return np.max(row_mins)

# Основная часть программы
if __name__ == "__main__":
    # Генерация случайной матрицы размером 20000 x 20000
    matrix = np.random.randint(1, 100, size=(20000, 20000))

    # Засекаем время начала выполнения программы
    start_time = time.time()

    # Вызываем функцию для поиска максимального значения среди минимальных элементов строк
    result = parallel_max_of_row_mins(matrix)

    # Засекаем время окончания выполнения программы
    end_time = time.time()

    # Выводим результат — максимальное значение среди минимальных элементов строк
    print(f"Максимальное значение среди минимальных элементов строк: {result}")

    # Выводим время выполнения программы
    print(f"Время выполнения: {end_time - start_time:.4f} секунд, на 6 ядрах")
