import pandas as pd


def build_df3() -> pd.DataFrame:
  data = pd.DataFrame({
      "order_id": [101, 102, 103, 104],
      "client_clean": [
          "Иван Иванов",
          "Степан Сорокин",
          "Петр Петров",
          "Анна Сидорова",
      ],
      "product_clean": ["НОУТБУК", "НОУТБУК", "КУРТКА", "РОМАН"],
      "order_date": pd.to_datetime(
          ["2026-05-01", "2026-05-01", "2026-05-02", "2026-05-03"]
      ),
      "revenue": [45000.0, 52250.0, 7600.0, 1500.0],
  })
  return data


df3 = build_df3()
df4 = df3.copy()

dup_keys = ["client_clean", "order_date", "product_clean"]
df4["duplicate_group_flag"] = df4.groupby(dup_keys)["order_id"].transform(
    lambda s: len(s) > 1
)
df4 = df4.sort_values(by="revenue", ascending=False)
df4 = df4.drop_duplicates(subset=dup_keys, keep="first")
df4 = df4.sort_values(by="order_id", ascending=True).reset_index(drop=True)

print(
    df4[[
        "order_id",
        "client_clean",
        "product_clean",
        "order_date",
        "revenue",
        "duplicate_group_flag",
    ]]
)