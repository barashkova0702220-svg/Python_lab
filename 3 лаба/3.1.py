import numpy as np
import pandas as pd

np.random.seed(42)
n_str = 100_000

df = pd.DataFrame({
    "id": np.arange(1, n_str + 1),
    "name": [f"Employee_{i}" for i in range(1, n_str + 1)],
    "age": np.random.randint(20, 65, size=n_str),
    "salary": np.round(np.random.uniform(40_000, 250_000, size=n_str), 2),
    "department": np.random.choice(
        ["IT", "HR", "Sales", "Marketing", "Finance"], size=n_str
    ),
    "hiredate": pd.to_datetime("2015-01-01")
    + pd.to_timedelta(np.random.randint(0, 3650, size=n_str), unit="D"),
    "is_active": np.random.choice([True, False], size=n_str),
})

print(df.head())
print(df.dtypes)