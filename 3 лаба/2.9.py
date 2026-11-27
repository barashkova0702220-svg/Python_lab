import pandas as pd


def build_df2() -> pd.DataFrame:
  df_base = pd.DataFrame({
      "order_id": [101, 102, 103, 104],
      "client_clean": [
          "Иван Иванов",
          "Петр Петров",
          "Анна Сидорова",
          "Ольга Смирнова",
      ],
      "revenue": [45000.0, 22500.0, 7600.0, 1500.0],
      "order_date": ["2026-05-01", "2026-05-02", "2026-05-03", "2026-05-31"],
      "delivery_days": [2, 5, 4, 3],
  })
  df_base["revenue_rank"] = (
      df_base["revenue"].rank(method="dense", ascending=False).astype(int)
  )
  return df_base.sort_values(
      by=["revenue", "order_date"], ascending=[False, True]
  ).reset_index(drop=True)


df2 = build_df2()
df3 = df2.copy()

df3["order_date"] = pd.to_datetime(df3["order_date"])
df3["order_year"] = df3["order_date"].dt.year
df3["order_month"] = df3["order_date"].dt.month
df3["order_quarter"] = df3["order_date"].dt.quarter
df3["order_weekday"] = df3["order_date"].dt.day_name()
df3["is_weekend"] = df3["order_date"].dt.dayofweek.isin([5, 6])
df3["delivery_date"] = df3["order_date"] + pd.to_timedelta(
    df3["delivery_days"], unit="D"
)

df3["days_to_month_end"] = (
    df3["order_date"] + pd.offsets.MonthEnd(0) - df3["order_date"]
).dt.days

print(
    df3[[
        "order_id",
        "order_date",
        "order_year",
        "order_month",
        "order_quarter",
        "order_weekday",
        "is_weekend",
        "delivery_date",
        "days_to_month_end",
    ]]
)