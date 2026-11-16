import numpy as np
from scipy.sparse import random as sparse_random
import timeit

np.random.seed(42)
a_sparse = sparse_random(5, 5, density=0.2, format='csr', random_state=42)
print("Разреженная матрица 5x5:")
print(a_sparse.toarray())
print(f"Количество ненулевых элементов: {a_sparse.nnz}\n")

a_kor = a_sparse.tocoo()
a_csc = a_sparse.tocsc()
print("Формат координаты и значения:")
print(f"Строки:  {a_kor.row}")
print(f"Столбцы: {a_kor.col}")
print(f"Значения:{a_kor.data}\n")
print("Формат сжатие по столбцам:")
print(f"Указатели: {a_csc.indptr}")
print(f"Индексы:   {a_csc.indices}")
print(f"Значения:  {a_csc.data}\n")

v_small = np.random.rand(5)
res_small = a_sparse.dot(v_small)
print("Результат умножения разреженной матрицы на плотный вектор:")
print(res_small, "\n")


n = 1000
d = 0.01
A_sp = sparse_random(n, n, density=d, format='csr', random_state=0)
v = np.random.rand(n)
A_dense = A_sp.toarray()
print("Замер времени умножения матрицы 1000x1000 на вектор:")
time_sp = timeit.timeit(lambda: A_sp.dot(v), number=10)
time_dense = timeit.timeit(lambda: A_dense.dot(v), number=10)
print(f"Время для разряженной матрицы матрицы: {time_sp:.6f} сек.")
print(f"Время для плотной матрицы:     {time_dense:.6f} сек.")
print(f"Разреженная матрица быстрее в {time_dense / time_sp:.1f} раз(а)")