import numpy as np

print("6.1.")
mass = np.arange(20)
print("Исходный массив:", mass)
elem_3 = mass[1::3]
print("Каждый третий элемент с индекса 1:", elem_3)

elem_5_15 = mass[5:15][::-1]
print("Элементы с 5 по 15 в обратном порядке:", elem_5_15)

posl_5 = mass[-5:][::-1]
print("Последние 5 элементов в обратном порядке:", posl_5)
print()

print("6.2.")
matrix = np.random.randint(0, 10, size=(6, 6))
print("Матрица 6x6:\n", matrix)

pod_matrix = matrix[2:5, 1:4]
print("\nПодматрица строки 2-4, столбцы 1-3:\n", pod_matrix)

diag = np.diagonal(matrix)
print("\nГлавная диагональ:", diag)

str_ind, stolb_ind = np.indices(matrix.shape)
okras = (str_ind + stolb_ind) % 2 == 0
okras_el = matrix[okras]
print("\nЭлементы на четных позициях:\n", okras_el.reshape(3, 6))
print()

print("6.3.")
vec_a = np.array([10, 20, 30, 40, 50, 60])
mat_m = np.arange(12).reshape(3, 4)
print("Массив a:", vec_a)
print("Матрица m:\n", mat_m)

vib_el = vec_a[[0, 2, 4]]
print("\nЭлементы a по индексам [0, 2, 4]:", vib_el)

str_el = [0, 1, 2]
stolb_el = [1, 3, 0]
vibor_par = mat_m[str_el, stolb_el]
print("Элементы матрицы m по парам (0,1), (1,3), (2,0):", vibor_par)

vibor_block = mat_m[np.ix_([0, 2], [1, 3])]
print("\nБлок 2x2 (строки 0, 2 и столбцы 1, 3):\n", vibor_block)
print()

print("6.4.")
random_ch = np.random.randn(1000)
col_el = np.sum(random_ch > 1)
print(f"Количество элементов > 1: {col_el}")


zam = random_ch.copy()
zam[zam < 0] = 0
print(f"Минимум после замены отрицательных (должен быть 0): {zam.min()}")


ochis = random_ch.copy()
zamena = np.where((random_ch[:-2] * random_ch[2:]) < 0)[0] + 1
ochis[zamena] = 0
print(f"Количество обнуленных элементов из-за смены знака у соседей: {len(zamena)}")