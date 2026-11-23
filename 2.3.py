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

print("3.1 Количество пропусков по столбцам")
print(df.isna().sum(), "\n")


df['zarplata'] = df.groupby('department')['zarplata'].transform(lambda x: x.fillna(x.mean()))
print("3.2 Zarplata с заполненными пропусками")
print(df[['name', 'department', 'zarplata']], "\n")


df['bonus'] = df['bonus'].fillna(0)
print("3.3 Bonus после замены NaN на 0")
print(df['bonus'].tolist(), "\n")


df3_clean = df.dropna(subset=['zarplata'])
print("3.4 Размер до и после удаления строк с NaN в zarplata")
print(f"Было строк: {len(df)}, стало: {len(df3_clean)}")