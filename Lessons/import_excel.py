import pandas as pd

# Если файл в той же папке, что твой скрипт
# df = pd.read_excel('C:\\Users\\madri\\Downloads\\111.xlsx')
df = pd.read_excel('Data/111.xlsx')
df['1'] = df['1']+10
# df['1'] = df['1'].int.replace(21,13)
df['NewColumn'] = 'Test'
df = df[df['3'] > 10]


# Посмотрим первые строки
print(df.head())
