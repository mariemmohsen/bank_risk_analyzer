from src.data_manager import DataManager
from src.cleaner import TransactionCleaner
from src.feature_builder import FeatureBuilder
from src.risk_scorer import riskscorer
from src.transaction_flagger import TransactionFlagger
from src.report_generator import ReportGenerator

class ConsoleApp:
    def __init__(self):
        self.data_manager=DataManager()
        self.cleaner=TransactionCleaner()
        self.feature_builder=FeatureBuilder()
        self.risk_scorer=riskscorer()
        self.flagger=TransactionFlagger()
        self.reporter=ReportGenerator()

        self.df=None
        self.df_clean=None
        self.customer_features=None
        self.flagged_transactions=None

    def run(self):
        while True:
            self.show_menu()
            choice=input("Choose an option: ")
            if choice=="1":
                self.load_data()
            elif choice=="2":
                self.clean_data()
            elif choice=="3":
                self.build_features()
            elif choice=="4":
                self.score_customers()
            elif choice=="5":
                self.flag_transactions()
            elif choice=="6":
                self.export_reports()
            elif choice=="7":
                self.show_summary()
            elif choice=="0":
                print("Exiting.")
                break
            else:
                print("Invalid choice.")

    def show_menu(self):
        print("\n--- Bank Transaction Risk Analyzer ---")
        print("1. Load dataset")
        print("2. Clean and validate data")
        print("3. Build features")
        print("4. Score customers")
        print("5. Flag suspicious transactions")
        print("6. Export reports")
        print("7. Display summary")
        print("0. Exit")

    def load_data(self):
        try:
            path = input("Enter CSV file path: ")
            self.df = self.data_manager.load_csv(path)
            if self.df is not None:
                print("Dataset loaded successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")  
    def clean_data(self):
        if self.df is None:
            print("Load data first.")
            return
        try:
            self.df_clean = self.cleaner.clean(self.df)
            self.df_clean = self.cleaner.convert_time_step(self.df_clean)
            print("Data cleaned successfully.")
        except Exception as e:
            print(f"Error during data cleaning: {e}")

    def build_features(self):
        if self.df_clean is None:
            print("Clean data first.")
            return
        try:
            self.customer_features = self.feature_builder.build_features(self.df_clean)
            print("Features built successfully.")
        except Exception as e:
            print(f"Error building features: {e}")

    def score_customers(self):
        if self.customer_features is None:
            print("Build features first.")
            return
        try:
            self.customer_features = self.risk_scorer.score(self.customer_features)
            print("Customers scored successfully.")
        except Exception as e:
            print(f"Error scoring: {e}")

    def flag_transactions(self):
        if self.df_clean is None:
            print("Clean data first.")
            return
        try:
            self.flagged_transactions = self.flagger.flag(self.df_clean)
            print("Suspicious transactions flagged.")
        except Exception as e:
            print(f"Error flagging transaction: {e}")

    def export_reports(self):
        if self.customer_features is None or self.flagged_transactions is None:
            print("Run scoring and flagging first.")
            return
        try:
            self.reporter.save_flagged_transactions(self.flagged_transactions,"reports/flagged_transactions.csv")
            self.reporter.save_customer_risk(self.customer_features,"reports/customer_risk_summary.csv")
            self.reporter.generate_text_report(self.customer_features,"reports/report.txt")
            print("Reports exported successfully.")
        except Exception as e:
            print(f"Error Exporting files: {e}")

    def show_summary(self):
        if self.customer_features is None:
            print("No results to display.")
            return
        print("\nRisk Level Summary:")
        print(self.customer_features["risk_level"].value_counts())
