import pandas as pd


def build_df5() -> pd.DataFrame:
  return pd.DataFrame({
      "order_id": [102, 103, 104, 105],
      "client_clean": [
          "Иван Иванов",
          "Петр Петров",
          "Анна Сидорова",
          "Ольга Смирнова",
      ],
      "revenue": [52250.0, 7600.0, 1500.0, 800.0],
      "delivery_days": [2, 5, 4, 3],
      "status": ["paid", "shipped", "cancelled", "new"],
      "revenue_segment": pd.Categorical(
          ["vip", "high", "medium", "low"],
          categories=["low", "medium", "high", "vip"],
      ),
      "manager": [
          "Алексей Смирнов",
          "Мария Иванова",
          "Елена Попова",
          "Игорь Соколов",
      ],
  })


df5 = build_df5()
df6 = df5.copy()


def assign_priority(row: pd.Series) -> str:
  if row["status"] in ("cancelled", "returned"):
    return "archive"
  if row["revenue"] >= 20000 and row["delivery_days"] <= 3:
    return "A"
  if row["revenue"] >= 5000:
    return "B"
  return "C"

df6["priority"] = df6.apply(assign_priority, axis=1)
df6["manager_email"] = (
    df6["manager"].astype(str).str.strip().str.lower().str.replace(" ", ".")
    + "@shop.ru"
)

df6["final_comment"] = df6.apply(
    lambda row: (
        f"{row['client_clean']}: {row['priority']}, {row['revenue_segment']}"
    ),
    axis=1,
)

df6.to_csv("orders_final.csv", index=False)
print(
    df6[[
        "order_id",
        "client_clean",
        "priority",
        "manager_email",
        "final_comment",
    ]]
)