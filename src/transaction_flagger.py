import pandas as pd
from scipy import stats
class TransactionFlagger:
    def flag(self,df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        df['amount_z_score']=stats.zscore(df['amount'].fillna(0))
        df['is_suspicious']=df['amount_z_score'].abs()>3
        rule=(df['type']=='TRANSFER')&(df['amount']>200000)
        df.loc[rule,'is_suspicious']=True
        return df

