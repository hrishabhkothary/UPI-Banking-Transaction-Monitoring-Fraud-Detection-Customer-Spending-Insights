import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt

DB_USER = 'root'
DB_PASSWORD = 'YOUR_PASSWORD'
DB_HOST = 'localhost'
DB_NAME = 'upi_banking_db'

engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

df = pd.read_sql("SELECT * FROM transactions", engine)

print(f"Average transaction amount: ₹{df['amount'].mean():.2f}")
print("Top 5 payees:")
print(df['payee_vpa'].value_counts().head(5))

df['hour'] = df['timestamp'].dt.hour
sns.histplot(df['hour'], bins=24)
plt.title("Transactions by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Transactions")
plt.show()
