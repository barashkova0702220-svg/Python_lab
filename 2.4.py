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

cr_zp = df.groupby('department')['zarplata'].mean()
print("4.1 Средняя зарплата по отделам")
print(cr_zp, "\n")

status = df.groupby('department').agg(
    avg_zarplata=('zarplata', 'mean'),
    max_bonus=('bonus', 'max'),
    emp_count=('name', 'count')
)
print("4.2 Агрегированная статистика по отделам")
print(status, "\n")

table = df.pivot_table(index='department', values='zarplata', aggfunc='mean')
print("4.3 Сводная таблица")
print(table, "\n")

otsortir = cr_zp.sort_values(ascending=False)
print("4.4 Отделы, отсортированные по средней зарплате по убывание")
print(otsortir)