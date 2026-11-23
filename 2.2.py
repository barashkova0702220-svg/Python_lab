import pandas as pd
import numpy as np

data = {
    'name': ['Elena', 'Irina', 'Olga', 'Dmitry', 'Alexey', 'Ksenia', 'Yulia', 'Svetlana'],
    'department': ['IT', 'HR', 'IT', 'Sales', 'HR', 'Sales', 'IT', 'HR'],
    'zarplata': [80000, 60000, np.nan, 75000, 65000, 90000, 85000, np.nan],
    'bonus': [5000, np.nan, 3000, 4000, np.nan, 6000, np.nan, 2000],
    'data_naima': pd.to_datetime(['2020-01-01', '2019-05-15', '2021-03-10', '2018-11-20',
                                   '2020-08-01', '2017-02-01', '2022-07-01', '2021-12-15'])
}
df = pd.DataFrame(data)

rabotniki = df[df['department'] == 'IT'][['name', 'zarplata']]
print("2.1 Имена и зарплаты сотрудников IT отдела")
print(rabotniki, "\n")

c = df.iloc[:3, :2]
print("2.2 Первые 3 строки и 2 столбца")
print(c, "\n")

a = df[df['zarplata'] > 70000]
print("2.3 Сотрудники с зарплатой > 70000")
print(a, "\n")

df['total_comp'] = df['zarplata'] + df['bonus'].fillna(0)
print("2.4 Добавлен столбец total_comp")
print(df[['name', 'zarplata', 'bonus', 'total_comp']], "\n")


df = df.drop(columns=['data_naima'])
print("2.5 Столбец data_naima удалён")
print("Оставшиеся столбцы:", df.columns.tolist(), "\n")