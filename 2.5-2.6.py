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


managers_data = {
    'department': ['IT', 'HR', 'Sales'],
    'manager_name': ['Kozlov', 'Smirnova', 'Volkov']
}
managers = pd.DataFrame(managers_data)
print("5.1 Отдел менеджеров")
print(managers, "\n")

df_merged = pd.merge(df, managers, on='department', how='left')
print("5.2 Объекдинение")
print(df_merged[['name', 'department', 'manager_name']], "\n")

new_str = pd.DataFrame([{
    'name': 'Marina',
    'department': 'Sales',
    'zarplata': 71000,
    'bonus': 3500,
    'data_naima': pd.to_datetime('2023-06-01'),
    'manager_name': 'Волков'
}])

df_extended = pd.concat([df_merged, new_str], ignore_index=True)
print("5.3 Новая строка")
print(df_extended.tail(3), "\n")

df_extended = df_extended.reset_index(drop=True)
print("5.4 Индекс сброшен")
print("Текущие индексы:", df_extended.index.tolist())

df_extended['bonus'] = df_extended['bonus'].fillna(0)
df_extended['total_comp'] = df_extended['zarplata'] + df_extended['bonus']

top_3 = df_extended.nlargest(3, 'total_comp')[['name', 'department', 'total_comp']]
print("6.1 Топ-3 сотрудника")
print(top_3, "\n")


cr_zp = df_extended.groupby('department')[['zarplata', 'bonus']].mean()
print("6.2 Средняя зарплата и бонус по отделам")
print(cr_zp, "\n")

df_extended['zarplata'] = df_extended.groupby('department')['zarplata'].transform(lambda x: x.fillna(x.mean()))


zp_75 = df_extended.groupby('department').apply(
    lambda group: (group['zarplata'] > 75000).mean()
)
print("6.3 Доля сотрудников с зарплатой > 75000")
print(zp_75)