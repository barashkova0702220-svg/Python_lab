import pandas as pd

def build_df1() -> pd.DataFrame:
  from pathlib import Path

  csv_path = Path("orders.csv")
  if not csv_path.exists():
    pd.DataFrame({
        "order_id": [101, 102, 103, 104, 105],
        "client": [
            "  иван иванов ",
            "Петр Петров",
            "  Степан Сорокин ",
            "анна сидорова",
            "Ольга Смирнова",
        ],
        "city": [
            " москва ",
            "Санкт-Петербург",
            " москва",
            "казань ",
            "Екатеринбург",
        ],
        "category": [
            " Электроника ",
            "Одежда",
            " электроника",
            "Книги ",
            "Техника",
        ],
        "product": [
            " ноутбук ",
            "куртка",
            "ноутбук",
            " роман ",
            "смартфон",
        ],
        "qty": [1, 2, 1, 3, 1],
        "price": [50000.0, 4000.0, 50000.0, 500.0, 25000.0],
        "discount": [0.1, 0.05, 0.1, 0.0, 0.1],
        "order_date": [
            "2026-05-02",
            "2026-05-02",
            "2026-05-01",
            "2026-05-03",
            "2026-05-04",
        ],
        "delivery_days": [2, 5, 2, 4, 3],
        "status": ["paid", "shipped", "paid", "cancelled", "new"],
        "promo_code": ["SALE10", "NO_PROMO", "VIP", "NO_PROMO", "SPRING"],
        "manager": [
            "Алексей Смирнов",
            "Мария Иванова",
            "Алексей Смирнов",
            "Елена Попова",
            "Игорь Соколов",
        ],
    }).to_csv(csv_path, index=False)

  raw = pd.read_csv(csv_path)
  out = raw.copy()
  out["client_clean"] = out["client"].astype(str).str.strip().str.title()
  out["city_clean"] = out["city"].astype(str).str.strip().str.title()
  out["category_clean"] = out["category"].astype(str).str.strip().str.lower()
  out["product_clean"] = out["product"].astype(str).str.strip().str.upper()
  out["revenue"] = (out["qty"] * out["price"] * (1 - out["discount"])).round(2)
  return out


df1 = build_df1()
df2 = df1.copy()

df2["revenue_rank"] = (
    df2["revenue"].rank(method="dense", ascending=False).astype(int)
)

df2 = df2.sort_values(
    by=["revenue", "order_date"], ascending=[False, True]
).reset_index(drop=True)

print(df2[["order_id", "client_clean", "revenue", "revenue_rank", "order_date"]])