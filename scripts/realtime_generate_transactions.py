# data/generate_transactions.py

import pandas as pd
from faker import Faker
import random
import time

fake = Faker()

chunk_size = 50

while True:
    records = []
    for _ in range(chunk_size):
        transaction_id = ""
        user_id = f"U{random.randint(1000, 9999)}"
        timestamp = fake.date_time_this_year()
        amount = round(random.uniform(1, 100000), 2)
        payee_vpa = fake.user_name() + "@upi"
        location = fake.city()
        device_id = fake.uuid4()
        is_fraud = random.choices([0, 1], weights=[98, 2])[0]
        records.append([transaction_id, user_id, timestamp, amount, payee_vpa, location, device_id, is_fraud])

    df = pd.DataFrame(records, columns=[
        'transaction_id', 'user_id', 'timestamp', 'amount',
        'payee_vpa', 'location', 'device_id', 'is_fraud'
    ])
    df.to_csv('transactions.csv', mode='a', header=False, index=False)
    print(f"[INFO] Added {chunk_size} new transactions.")
    time.sleep(10)  # wait for 10 seconds before next chunk
