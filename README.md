# 📊 UPI & Banking Transaction Monitoring, Fraud Detection & Customer Spending Insights


## 🚀 Overview

This project is an **industrial-grade pipeline** for monitoring, analyzing, and detecting fraud in large-scale **electronic banking and UPI transactions**.  
It demonstrates **end-to-end data engineering**, **machine learning for anomaly detection**, and **customer spending insights** using **Python**, **MySQL**, and powerful open-source libraries.

---

## 🎯 **Key Features**

- ✅ **Large-scale synthetic data generation:** Simulates 50,000 realistic UPI & banking transactions using `Faker` for user behavior, locations, amounts, devices, and VPA IDs.
- ✅ **ETL Pipeline:** Cleans raw transaction data, adds unique IDs, validates timestamps, and loads clean records into a structured **MySQL** database.
- ✅ **Anomaly/Fraud Detection:** Uses an **Isolation Forest** ML algorithm to detect unusual high-value transactions — helping financial institutions flag suspicious activity.
- ✅ **Customer Insights & Reporting:** Provides average spend analysis, top payees, and visual time-based spending trends.
- ✅ **Automated Testing:** Unit tests for data integrity, timestamp checks, and ML output sanity checks to ensure reliability.
- ✅ **Fully Modular:** Cleanly separated scripts for ETL, ML, and reporting, ready for production or integration with real-time systems.

---

## 🛠️ Tech Stack:

| Layer | Tools & Libraries |
|-------|--------------------|
| **Language** | Python 3 |
| **Data Generation** | `Faker` |
| **Data Processing** | `pandas` |
| **Database** | MySQL |
| **ORM/Connection** | `SQLAlchemy` + `mysql-connector-python` |
| **Machine Learning** | `scikit-learn` (Isolation Forest) |
| **Visualization** | `matplotlib`, `seaborn` |
| **Testing** | `pytest` |

---


