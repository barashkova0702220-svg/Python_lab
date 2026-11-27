from pathlib import Path
import pandas as pd

def get_orders_df() -> pd.DataFrame:
  csv_path = Path("orders.csv")
  if not csv_path.exists():
    sample_orders = pd.DataFrame({
        "order_id": [101, 102, 103, 104, 105, 106],
        "client": [
            "  иван иванов ",
            "Петр Петров",
            "  Степан Сорокин ",
            "анна сидорова",
            "Ольга Смирнова",
            "Дмитрий Козлов",
        ],
        "city": [
            " москва ",
            "Санкт-Петербург",
            " москва",
            "казань ",
            "Екатеринбург",
            " новосибирск ",
        ],
        "category": [
            " Электроника ",
            "Одежда",
            " электроника",
            "Книги ",
            "Техника",
            "Спорт",
        ],
        "product": [
            " ноутбук ",
            "куртка",
            "ноутбук",
            " роман ",
            "смартфон",
            "велосипед",
        ],
        "qty": [1, 2, 1, 3, 1, 1],
        "price": [50000.0, 4000.0, 55000.0, 500.0, 25000.0, 15000.0],
        "discount": [0.1, 0.05, 0.05, 0.0, 0.1, 0.2],
        "order_date": [
            "2026-05-01",
            "2026-05-02",
            "2026-05-01",
            "2026-05-03",
            "2026-05-04",
            "2026-05-05",
        ],
        "delivery_days": [2, 5, 2, 4, 3, 7],
        "status": ["paid", "shipped", "paid", "cancelled", "new", "returned"],
        "promo_code": [
            "SALE10",
            "NO_PROMO",
            "VIP",
            "NO_PROMO",
            "SPRING",
            "NO_PROMO",
        ],
        "manager": [
            "Алексей Смирнов",
            "Мария Иванова",
            "Алексей Смирнов",
            "Елена Попова",
            "Игорь Соколов",
            "Мария Иванова",
        ],
    })
    sample_orders.to_csv(csv_path, index=False)
  return pd.read_csv(csv_path)
df = get_orders_df()
df1 = df.copy()
df1["client_clean"] = df1["client"].astype(str).str.strip().str.title()

df1["city_clean"] = df1["city"].astype(str).str.strip().str.title()
df1["category_clean"] = df1["category"].astype(str).str.strip().str.lower()
df1["product_clean"] = df1["product"].astype(str).str.strip().str.upper()
df1["revenue"] = (df1["qty"] * df1["price"] * (1 - df1["discount"])).round(2)
print(
    df1[[
        "order_id",
        "client_clean",
        "city_clean",
        "category_clean",
        "product_clean",
        "revenue",
    ]]
)