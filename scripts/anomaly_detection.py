import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import IsolationForest

DB_USER = 'root'
DB_PASSWORD = 'YOUR_PASSWORD'
DB_HOST = 'localhost'
DB_NAME = 'upi_banking_db'

engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

df = pd.read_sql("SELECT * FROM transactions", engine)

X = df[['amount']]

model = IsolationForest(contamination=0.02, random_state=42)
df['is_anomaly'] = model.fit_predict(X)
df['is_anomaly'] = df['is_anomaly'].apply(lambda x: 1 if x == -1 else 0)

df[['transaction_id', 'is_anomaly']].to_sql('anomaly_results', con=engine, if_exists='replace', index=False)

print(f"[INFO] Detected anomalies: {df['is_anomaly'].sum()}")
