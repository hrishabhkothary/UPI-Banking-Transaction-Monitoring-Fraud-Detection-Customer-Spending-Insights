import pandas as pd
from sqlalchemy import create_engine
import uuid

DB_USER = 'root'
DB_PASSWORD = 'YOUR_PASSWORD'
DB_HOST = 'localhost'
DB_NAME = 'upi_banking_db'

engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

df = pd.read_csv('../data/transactions.csv')

df.dropna(inplace=True)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['transaction_id'] = [str(uuid.uuid4()) for _ in range(len(df))]

df.to_sql('transactions', con=engine, if_exists='append', index=False)
print(f"[INFO] Loaded {len(df)} rows to MySQL.")
