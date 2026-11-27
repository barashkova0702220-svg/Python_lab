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

df_dept_agg = (
    df.groupby("department", as_index=False)["salary"]
    .agg(avg_salary="mean", headcount="count")
    .round(2)
)

df.to_hdf("storage_fixed.h5", key="raw_employees", mode="w", format="fixed")
df_dept_agg.to_hdf("storage_fixed.h5", key="dept_summary", mode="a", format="fixed")

only_summary = pd.read_hdf("storage_fixed.h5", key="dept_summary")
print("Сводка по отделам:\n", only_summary)

df_for_query = df.copy()
df_for_query["name"] = df_for_query["name"].astype(str)
df_for_query["department"] = df_for_query["department"].astype(str)

df_for_query.to_hdf(
    "storage_table.h5",
    key="employees_tbl",
    mode="w",
    format="table",
    data_columns=["department", "age", "salary"],
)

subset_q = pd.read_hdf(
    "storage_table.h5",
    key="employees_tbl",
    where="department == 'Finance' & age >= 50 & salary > 180000",
)
print(f"\nНайдено строк по запросу where: {len(subset_q)}")

df.to_csv("employees_no_index.csv", index=False)
print(f"HDF5 (fixed): {os.path.getsize('storage_fixed.h5') / (1024*1024):.2f} МБ")
print(f"HDF5 (table): {os.path.getsize('storage_table.h5') / (1024*1024):.2f} МБ")
print(f"CSV:          {os.path.getsize('employees_no_index.csv') / (1024*1024):.2f} МБ")