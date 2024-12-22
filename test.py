import numpy as np
import time

# Функция для нахождения минимального элемента в строках и поиска максимума из них
def find_row_min(matrix):
    row_mins = []
    for row in matrix:
        row_mins.append(min(row))
    return max(row_mins)

# Функция для выполнения задачи и замера времени
def run_task(matrix):
    result = find_row_min(matrix)
    return result

# Основная часть программы
start_time = time.time()
N, M = 20000, 20000
matrix = np.random.randint(1, 100, size=(N, M))

result = run_task(matrix)

end_time = time.time()
execution_time = end_time - start_time
print(f"Максимальное значение среди минимальных элементов строк: {result}")
print(f"\nВремя выполнения: {execution_time:.4f} секунд, на одном ядре")
