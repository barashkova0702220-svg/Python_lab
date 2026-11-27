import numpy as np
import pandas as pd
import os

np.random.seed(42)
n_rows = 100_000
df = pd.DataFrame({
    "id": np.arange(1, n_rows + 1),
    "name": [f"Employee_{i}" for i in range(1, n_rows + 1)],
    "age": np.random.randint(20, 65, size=n_rows),
    "salary": np.round(np.random.uniform(40_000, 250_000, size=n_rows), 2),
    "department": np.random.choice(["IT", "HR", "Sales", "Marketing", "Finance"], size=n_rows),
    "hiredate": pd.to_datetime("2015-01-01") + pd.to_timedelta(np.random.randint(0, 3650, size=n_rows), unit="D"),
    "is_active": np.random.choice([True, False], size=n_rows),
})

df.to_csv("employees_with_index.csv", index=True)
df.to_csv("employees_no_index.csv", index=False)

df_read_default = pd.read_csv("employees_no_index.csv")
print("Типы при обычном чтении:")
print(df_read_default.dtypes)

size_with_idx = os.path.getsize("employees_with_index.csv") / (1024 * 1024)
size_no_idx = os.path.getsize("employees_no_index.csv") / (1024 * 1024)
print(f"\nРазмер с индексом: {size_with_idx:.2f} МБ | без индекса: {size_no_idx:.2f} МБ")


df_read_fast = pd.read_csv(
    "employees_no_index.csv",
    usecols=["id", "age", "salary", "department", "hiredate", "is_active"],
    dtype={
        "id": "int32",
        "age": "int8",
        "salary": "float32",
        "department": "category",
        "is_active": "bool",
    },
    parse_dates=["hiredate"],
)
print("\nТипы при оптимизированном чтении:")
print(df_read_fast.dtypes)