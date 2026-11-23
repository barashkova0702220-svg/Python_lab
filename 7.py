import numpy as np
import os
import time

print("7.1.")
file_name = "file.dat"
str, kol = 50000, 200
data_type = np.float32

filee = np.memmap(file_name, dtype=data_type, mode='w+', shape=(str, kol))
print("Заполнение файла случайными числами")
cl_chisla = 5000
for start_str in range(0, str, cl_chisla):
    end_str = min(start_str + cl_chisla, str)
    filee[start_str:end_str, :] = np.random.rand(end_str - start_str, kol)

filee.flush()
file_size = os.path.getsize(file_name)
razmer_file = str * kol * 4
print(f"Размер файла: {file_size} байт. Ожидаемый: {razmer_file} байт. Совпадает: {file_size == razmer_file}")
del filee
print()

print("7.2.")
read_file = np.memmap(file_name, dtype=data_type, mode='r', shape=(str, kol))

global_min = np.inf
global_max = -np.inf
total_sum = 0.0
total_el = 0

# Читаем по 1000 строк за раз, не загружая массив целиком
for start_str in range(0, str, 1000):
    end_str = min(start_str + 1000, str)
    batch = read_file[start_str:end_str, :]

    tek_min = batch.min()
    tek_max = batch.max()
    tek_sum = batch.sum()
    tek_c = batch.size

    if tek_min < global_min: global_min = tek_min
    if tek_max > global_max: global_max = tek_max
    total_sum += tek_sum
    total_el += tek_c

global_mean = total_sum / total_el
print(f"Глобальный MIN: {global_min}")
print(f"Глобальный MAX: {global_max}")
print(f"Глобальное MEAN: {global_mean}")
del read_file
print()

print("7.3.")
n = 3000
matrix_c = np.random.rand(n, n).astype(np.float64)
matrix_f = np.asfortranarray(matrix_c)


def sum_rows_python(mat):
    c = 0.0
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            c += mat[i, j]
    return c


def sum_cols_python(mat):
    c = 0.0
    for j in range(mat.shape[1]):
        for i in range(mat.shape[0]):
            c += mat[i, j]
    return c


print(f"Замер для матрицы {n}x{n}")
start = time.perf_counter()
sum_rows_python(matrix_c)
time_c_row_major = time.perf_counter() - start

start = time.perf_counter()
sum_cols_python(matrix_c)
time_c_col_major = time.perf_counter() - start

start = time.perf_counter()
sum_rows_python(matrix_f)
time_f_row_major = time.perf_counter() - start

start = time.perf_counter()
sum_cols_python(matrix_f)
time_f_col_major = time.perf_counter() - start

print(f"C-порядок: время обхода по строкам {time_c_row_major:.4f} с, по столбцам {time_c_col_major:.4f} с")
print(f"F-порядок: время обхода по строкам {time_f_row_major:.4f} с, по столбцам {time_f_col_major:.4f} с")
print("Вывод: обход, совпадающий с физическим расположением в памяти, происходит быстрее.")
print()

print("7.4. Сравнение скорости вычислений (10 млн элементов)")
razmer = 10 ** 7
vec_a = np.random.rand(razmer)
vec_b = np.random.rand(razmer)

list_a = vec_a.tolist()
list_b = vec_b.tolist()
start = time.perf_counter()
res_py = [(x + y) / (x - y + 1) for x, y in zip(list_a, list_b)]
time_py_loop = time.perf_counter() - start
print(f"Python-цикл:      {time_py_loop:.3f} с")

start = time.perf_counter()
res_np = (vec_a + vec_b) / (vec_a - vec_b + 1)
time_np_expr = time.perf_counter() - start
print(f"NumPy в одну строку:     {time_np_expr:.3f} с")

res_buffer = np.empty_like(vec_a)
start = time.perf_counter()
np.add(vec_a, vec_b, out=res_buffer)
np.subtract(vec_a, vec_b, out=res_buffer)
np.add(res_buffer, 1, out=res_buffer)
np.divide(vec_a + vec_b, res_buffer, out=res_buffer)
time_np_out = time.perf_counter() - start
print(f"NumPy с out= (буфер):    {time_np_out:.3f} с")