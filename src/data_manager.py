import pandas as pd


class DataManager:
    def load_csv(self, file_path: str) -> pd.DataFrame:
        """
        Load transaction dataset from CSV file.
        """
        try:
            df = pd.read_csv(file_path)
            return df
        except Exception as e:
            print(f"Error loading file: {e}")
            return None

