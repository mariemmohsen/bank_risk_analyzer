# Bank Transaction Risk Analyzer

## Project Overview

The Bank Transaction Risk Analyzer is a Python-based application designed to analyze large-scale banking transaction data and identify potentially risky customers and suspicious transactions.  
The project follows Object-Oriented Programming (OOP) principles and applies statistical techniques to detect abnormal financial behavior without relying on predefined fraud labels.

---

## Project Objectives

- Clean and preprocess raw transaction data
- Engineer meaningful behavioral features for each customer
- Compute statistical risk scores using transaction volume and activity velocity
- Flag suspicious transactions based on anomaly detection rules
- Generate analytical reports for further inspection

---

## Project Structure

bank_risk_analyzer/
│
├── main.py
│   Entry point of the application. Starts the console-based interface.
│
├── src/
│   Contains the core application logic.
│
│   ├── data_manager.py
│   Responsible for loading and validating the transaction dataset.
│
│   ├── cleaner.py
│   Handles data cleaning tasks such as missing values, data type conversion,
│   duplicate removal, and time feature creation.
│
│   ├── feature_builder.py
│   Generates customer-level behavioral features including transaction
│   statistics, velocity metrics, and rolling statistics.
│
│   ├── risk_scorer.py
│   Computes statistical risk scores and assigns categorical risk levels
│   (Low, Medium, High, Critical) for each customer.
│
│   ├── transaction_flagger.py
│   Identifies suspicious transactions using anomaly detection rules.
│
│   ├── report_generator.py
│   Exports analysis results and generates CSV and text-based reports.
│
│   └── console_app.py
│   Acts as the application controller and manages user interaction
│   through a command-line menu.
│
├── data/
│   Stores the input transaction dataset.
│
│   └── PS_20174392719_1491204439457_log.csv
│   Raw transaction data file.
│
├── reports/
│   Contains generated output files.
│
│   ├── flagged_transactions.csv
│   List of transactions identified as suspicious.
│
│   ├── customer_risk_summary.csv
│   Summary of customer risk scores and risk levels.
│
│   └── report.txt
│   Textual analysis report highlighting high and critical risk customers.
│
└── README.md
    Project documentation and usage instructions.
