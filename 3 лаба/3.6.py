import numpy as np
import pandas as pd
import os
import time

np.random.seed(42)
n_str = 100_000
df = pd.DataFrame({
    "id": np.arange(1, n_str + 1),
    "name": [f"Employee_{i}" for i in range(1, n_str + 1)],
    "age": np.random.randint(20, 65, size=n_str),
    "salary": np.round(np.random.uniform(40_000, 250_000, size=n_str), 2),
    "department": np.random.choice(["IT", "HR", "Sales", "Marketing", "Finance"], size=n_str),
    "hiredate": pd.to_datetime("2015-01-01") + pd.to_timedelta(np.random.randint(0, 3650, size=n_str), unit="D"),
    "is_active": np.random.choice([True, False], size=n_str),
})

metrics = []
def mer(label, path, write_fn, read_fn):
    t_start = time.perf_counter()
    write_fn()
    write_sec = time.perf_counter() - t_start

    t_start = time.perf_counter()
    _ = read_fn()
    read_sec = time.perf_counter() - t_start

    raz_mb = os.path.getsize(path) / (1024 * 1024)

    metrics.append({
        "Format": label,
        "Size_MB": round(raz_mb, 3),
        "Write_sec": round(write_sec, 4),
        "Read_sec": round(read_sec, 4),
    })


mer(
    "CSV",
    "cmp.csv",
    lambda: df.to_csv("cmp.csv", index=False),
    lambda: pd.read_csv("cmp.csv"),
)

mer(
    "JSON",
    "cmp.json",
    lambda: df.to_json("cmp.json", orient="records", date_format="iso"),
    lambda: pd.read_json("cmp.json", orient="records"),
)

mer(
    "Parquet (snappy)",
    "cmp.parquet",
    lambda: df.to_parquet("cmp.parquet", compression="snappy", index=False),
    lambda: pd.read_parquet("cmp.parquet"),
)

mer(
    "HDF5 (fixed)",
    "cmp.h5",
    lambda: df.to_hdf("cmp.h5", key="df", mode="w", format="fixed"),
    lambda: pd.read_hdf("cmp.h5", key="df"),
)

res = pd.DataFrame(metrics)
print(res.to_string(index=False))