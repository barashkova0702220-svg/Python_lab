import numpy as np
from scipy.sparse import coo_matrix, csr_matrix, random as sparse_random
import time
import sys

print("8.1.")
np.random.seed(42)
dlina = 10000
str_list = np.random.randint(0, 5000, size=dlina)
stolb_list = np.random.randint(0, 5000, size=dlina)
data_list = np.random.rand(dlina)

coo_mat = coo_matrix((data_list, (str_list, stolb_list)), shape=(5000, 5000))
print(f"Исходное количество элементов в списках: {dlina}")
print(f"Количество ненулевых в COO до слияния дубликатов: {coo_mat.nnz}")

coo_mat.sum_duplicates()
print(f"Количество nnz в COO после слияния дубликатов: {coo_mat.nnz}")

csr_mat = coo_mat.tocsr()
print(f"Количество nnz в CSR: {csr_mat.nnz}")
print("Данные конвертированы корректно.\n")

print("8.2.")
n_razmer = 4000
plotn = 0.005

raz_mat = sparse_random(n_razmer, n_razmer, density=plotn, format='csr', random_state=0)
plotn_mat = raz_mat.toarray()

memory_plotn = plotn_mat.nbytes
memory_sparse = raz_mat.data.nbytes + raz_mat.indices.nbytes + raz_mat.indptr.nbytes

print(f"Память для Dense: {memory_plotn / (1024 ** 2):.2f} МБ")
print(f"Память для CSR:   {memory_sparse / (1024 ** 2):.2f} МБ")
print(f"Экономия памяти:  в {memory_plotn / memory_sparse:.1f} раз(а)")

vec_x = np.random.rand(n_razmer)

start = time.perf_counter()
for _ in range(10):
    raz_mat.dot(vec_x)
time_sparse = (time.perf_counter() - start) / 10
start = time.perf_counter()
for _ in range(10):
    plotn_mat.dot(vec_x)
time_dense = (time.perf_counter() - start) / 10

print(f"\nВремя умножения Dense  x: {time_dense:.6f} с")
print(f"Время умножения CSR  x:   {time_sparse:.6f} с")
print(f"CSR быстрее в {time_dense / time_sparse:.1f} раз(а)\n")

print("8.3.")
n_fixed = 2000
densities = [0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0]
vec_fixed = np.random.rand(n_fixed)

print(f"{'Плотность':<12} | {'Sparse (сек)':<15} | {'Dense (сек)':<15} | {'Кто быстрее'}")

for d in densities:
    mat_sp = sparse_random(n_fixed, n_fixed, density=d, format='csr', random_state=1)
    mat_dn = mat_sp.toarray()

    start = time.perf_counter()
    mat_sp.dot(vec_fixed)
    t_sp = time.perf_counter() - start

    start = time.perf_counter()
    mat_dn.dot(vec_fixed)
    t_dn = time.perf_counter() - start

    winner = "Sparse" if t_sp < t_dn else "Dense"
    print(f"{d:<12.3f} | {t_sp:<15.6f} | {t_dn:<15.6f} | {winner}")

