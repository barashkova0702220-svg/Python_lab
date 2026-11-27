import numpy as np
import pandas as pd
import json
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

df_skills = pd.DataFrame({
    "emp_id": [1, 2, 3],
    "name": ["Елена", "Алексей", "Ирина"],
    "skills": [
        ["Python", "SQL"],
        ["Excel", "PowerBI", "SQL"],
        ["Python", "Docker"],
    ],
    "meta": [
        {"level": "middle", "remote": True},
        {"level": "senior", "remote": False},
        {"level": "junior", "remote": True},
    ],
})

for orient in ["records", "columns", "index", "split"]:
    filename = f"skills_{orient}.json"
    df_skills.to_json(filename, orient=orient, force_ascii=False, indent=2)
    print(f"orient={orient:<8} -> размер: {os.path.getsize(filename)} байт")

with open("skills_records.json", "r", encoding="utf-8") as f:
    data_json = json.load(f)

df_norm = pd.json_normalize(
    data_json, record_path=["skills"], meta=["emp_id", "name", ["meta", "level"]]
)
df_norm.rename(columns={0: "skill", "meta.level": "level"}, inplace=True)
print("\nРазвёрнутая таблица:")
print(df_norm)