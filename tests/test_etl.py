import pandas as pd

def test_csv_not_empty():
    df = pd.read_csv('data/transactions.csv')
    assert not df.empty, "CSV must not be empty"

def test_timestamp_valid():
    df = pd.read_csv('data/transactions.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    assert df['timestamp'].isnull().sum() == 0, "All timestamps must be valid"
