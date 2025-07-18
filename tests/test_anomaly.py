import pandas as pd
from sklearn.ensemble import IsolationForest

def test_isolation_labels():
    df = pd.read_csv('data/transactions.csv')
    X = df[['amount']]
    model = IsolationForest(contamination=0.02)
    labels = model.fit_predict(X)
    assert set(labels).issubset({-1, 1}), "Labels must be -1 or 1 only"

def test_not_all_anomaly():
    df = pd.read_csv('data/transactions.csv')
    X = df[['amount']]
    model = IsolationForest(contamination=0.02)
    labels = model.fit_predict(X)
    assert sum(labels == -1) < len(labels), "Not all rows can be anomalies"
