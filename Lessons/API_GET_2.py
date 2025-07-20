import requests
import pandas as pd
from datetime import datetime, timedelta

# Настройки
curr = 'EUR'
start_date = datetime(2025, 5, 1)
end_date = datetime(2025, 5, 31)

# Список для хранения результатов
all_data = []

# Цикл по дням
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime('%Y%m%d')  # формат YYYYMMDD
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={curr}&date={date_str}&json"

    response = requests.get(url=url)
    if response.status_code == 200:
        day_data = response.json()
        if day_data:  # проверка, что есть данные
            all_data.append(day_data[0])  # в ответе список с одним словарем
    else:
        print(f"Ошибка запроса на {date_str}: {response.status_code}")

    current_date += timedelta(days=1)

# Преобразуем в DataFrame и сохраняем
df = pd.DataFrame(all_data)
df.to_csv("eur_may_2025.csv", index=False)
print(df)
