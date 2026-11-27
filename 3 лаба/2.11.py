import numpy as np
import pandas as pd


def build_df4() -> pd.DataFrame:
  return pd.DataFrame({
      "order_id": [102, 103, 104, 105],
      "client_clean": [
          "Иван Иванов",
          "Петр Петров",
          "Анна Сидорова",
          "Ольга Смирнова",
      ],
      "revenue": [52250.0, 7600.0, 1500.0, 800.0],
      "status": ["paid", "shipped", "cancelled", "new"],
      "promo_code": ["VIP", "NO_PROMO", "NO_PROMO", "SPRING10"],
  })


df4 = build_df4()
df5 = df4.copy()

bins = [0, 1000, 5000, 20000, np.inf]
labels = ["low", "medium", "high", "vip"]

df5["revenue_segment"] = pd.cut(
    df5["revenue"], bins=bins, labels=labels, right=False
)

status_translation = {
    "new": "новый",
    "paid": "оплачен",
    "shipped": "отправлен",
    "cancelled": "отменён",
    "returned": "возврат",
}
df5["status_ru"] = df5["status"].map(status_translation)

df5["promo_used"] = df5["promo_code"] != "NO_PROMO"
print(
    df5[[
        "order_id",
        "revenue",
        "revenue_segment",
        "status",
        "status_ru",
        "promo_code",
        "promo_used",
    ]]
)