import pandas as pd 
from scipy import stats
class riskscorer:
    def score(self, df:pd.DataFrame)->pd.DataFrame:
        df=df.copy()
        df["amount_z"]=stats.zscore(df['total_amount'])
        df['velocity_z']=stats.zscore(df['daily_velocity'])
        df['rolling_z']=stats.zscore(df['max_rolling_amount'])
        df[['amount_z','velocity_z','rolling_z']]=(df[['amount_z','velocity_z','rolling_z']].fillna(0))
        df['risk_score']=(
            df['amount_z'].abs()+df['velocity_z'].abs()+df['rolling_z'].abs()*0.5+df['invalid_balance_rate']*2
        )
        df['risk_level']=df['risk_score'].apply(self._risk_band)
        return df
    
    def _risk_band(self,score:float)->str:
        if score <2:
            return 'Low'
        elif score <4:
            return 'Medium'
        elif score <6:
            return 'High'
        else:
            return 'Critical'
        
        
        
