import requests
import pandas as pd
from datetime import datetime, timedelta


# URL = f"https://cdn.cookielaw.org/scripttemplates/202503.2.0/assets/v2/otPcTab.json"
# r = requests.get(url=URL)
# result = r.json()
#
# if r.status_code == 200:
#     print(result)
#     print(type(result))
#     print(r.text)
#     print(r.status_code)
#     print(result.get('data'))
# else:
#     print('was error')
#     print(r.status_code)
#     print(r.text)

curr = 'EUR'
start_date = datetime(2025, 5, 1)
end_date = datetime(2025, 5, 31)

all_data = []

current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime('%Y%m%d')  # формат YYYYMMDD
    URL = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={curr}&date={date_str}&json"
    r = requests.get(url=URL)
    result = r.json()
    all_data.append(result[0])

    current_date += timedelta(days=1)

# print(result)
# print(type(result))

df1 = pd.DataFrame(all_data)
# print(df1)
# print(type(df1))
df1.to_csv("usd_may_2025", index=False)
# df2 = pd.read_csv("usd_may_2025.csv")
print(df1)
# print(type(df2))