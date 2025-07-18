CREATE DATABASE IF NOT EXISTS upi_banking_db;

USE upi_banking_db;

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(50),
    timestamp DATETIME,
    amount DECIMAL(12,2),
    payee_vpa VARCHAR(150),
    location VARCHAR(100),
    device_id VARCHAR(100),
    is_fraud BOOLEAN
);

CREATE TABLE IF NOT EXISTS anomaly_results (
    transaction_id VARCHAR(36),
    is_anomaly BOOLEAN
);