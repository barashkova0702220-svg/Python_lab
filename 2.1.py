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

my_index= pd.Series([100, 200, 300], index=['Первый', 'Второй', 'Третий'])
print("1.1")
print(my_index, "\n")

print("1.2")
print(df, "\n")

print("1.3 Первые 3 строки")
print(df.head(3))

print("\n1.3 Последние 3 строки")
print(df.tail(3))

print("\n1.3 Информация о типах данных")
df.info()
print("\n1.3 Статистика (описательные статистики по числовым столбцам)")
print(df.describe())