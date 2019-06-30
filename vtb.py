import pandas as pd
df = pd.read_csv('details.csv', encoding='ANSI', sep=';', skiprows=11)

df.drop(columns=['Дата обработки',
                 'Валюта операции',
                 'Номер карты/счета/договора',
                 'Сумма пересчитанная в валюту счета',
                 'Валюта счета'],
        inplace=True)
df.rename(columns={'Дата операции': 'transaction_date',
                   'Сумма операции': 'amount',
                   'Основание': 'cause',
                   'Статус': 'status'
                   }, inplace=True)

df['amount'] = [x.replace(',', '.') for x in df['amount']]
df.query("status == 'Исполнено'", inplace=True)
df['transaction_date'] = df['transaction_date'].apply(pd.to_datetime)
pd.to_numeric(df['amount'], errors='ignore')

df = df[df['cause'].str.startswith('PYATEROCHKA', na=False)]
df0619 = df.query("transaction_date >= '2019-06-01'")
# df = df[df['transaction_date'].date()]
print(df0619)
print(df0619.dtypes)
print(df0619.shape)

# df0619.to_excel('det.xlsx', header = True, index = False)