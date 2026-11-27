import numpy as np
import pandas as pd
import os
import time

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

df.to_csv("employees_no_index.csv", index=False)

for comp in ["snappy", "gzip", "brotli"]:
    df.to_parquet(f"employees_{comp}.parquet", compression=comp, index=False)

csv_size = os.path.getsize("employees_no_index.csv") / (1024 * 1024)
print(f"CSV:             {csv_size:.2f} МБ")
for comp in ["snappy", "gzip", "brotli"]:
    p_size = os.path.getsize(f"employees_{comp}.parquet") / (1024 * 1024)
    print(f"Parquet ({comp}): {p_size:.2f} МБ")

t0 = time.perf_counter()
_ = pd.read_csv("employees_no_index.csv")
t_csv = time.perf_counter() - t0

t0 = time.perf_counter()
df_parquet = pd.read_parquet("employees_snappy.parquet")
t_parquet = time.perf_counter() - t0
print(f"\nЧтение CSV: {t_csv:.4f} с | Parquet (snappy): {t_parquet:.4f} с")

df_ctolb = pd.read_parquet(
    "employees_snappy.parquet", columns=["id", "salary", "department"]
)
print("\nВыборочные столбцы:\n", df_ctolb.head(3))

print("\nТипы данных из Parquet:\n", df_parquet.dtypes)