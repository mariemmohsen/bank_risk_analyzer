import pandas as pd


class ReportGenerator:
    def save_flagged_transactions(self, df: pd.DataFrame, path: str):
        """
        Save suspicious transactions to CSV.
        """
        df[df["is_suspicious"]].to_csv(path, index=False)

    def save_customer_risk(self, df: pd.DataFrame, path: str):
        df.to_csv(path, index=False)

    def generate_text_report(self, customer_df: pd.DataFrame, path: str):
        """
        Generate a simple text report summarizing risky customers.
        """
        with open(path, "w") as f:
            f.write("Bank Transaction Risk Analysis Report\n")
            f.write("=" * 40 + "\n\n")

            f.write("Top High & Critical Risk Customers:\n\n")

            risky = customer_df[
                customer_df["risk_level"].isin(["High", "Critical"])
            ].sort_values("risk_score", ascending=False)

            for _, row in risky.head(10).iterrows():
                f.write(
                    f"Customer: {row['nameOrig']} | "
                    f"Risk Level: {row['risk_level']} | "
                    f"Risk Score: {row['risk_score']:.2f}\n"
                )
