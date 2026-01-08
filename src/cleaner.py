import pandas as pd
class TransactionCleaner:
    def remove_invalid_amounts(self,df:pd.DataFrame)->pd.DataFrame:
        return df[df["amount"]>0]
    
    def remove_duplicates(self,df:pd.DataFrame)->pd.DataFrame:
        return df.drop_duplicates()

    def missing_values(self,df: pd.DataFrame)->pd.DataFrame:
        return df.dropna()

    def data_types(self,df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        df["step"] =pd.to_numeric(df["step"],errors="coerce")
        df["amount"]=pd.to_numeric(df["amount"],errors="coerce")
        return df
    
    def convert_time_step(self,df:pd.DataFrame,step_col:str="step", base_time: str="2025-1-1",unit:str="h") -> pd.DataFrame:
        df=df.copy()
        base_time=pd.to_datetime(base_time)
        df["datetime"]=base_time+pd.to_timedelta(df[step_col],unit=unit)
        df["day"]=df["datetime"].dt.day
        return df

    def clean(self,df: pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        df=self.missing_values(df)
        df=self.data_types(df)
        df=self.remove_invalid_amounts(df)
        df=self.remove_duplicates(df)

        return df
