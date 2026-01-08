import pandas as pd
class FeatureBuilder:
    def build_features(self,df:pd.DataFrame,save_path:str|None=None)->pd.DataFrame:
        ########### Statistical Features
        features=(
            df.groupby('nameOrig').agg(
                transaction_count=('amount','count'),
                total_amount=('amount','sum'),
                avg_amount=('amount','mean'),
                max_amount=('amount','max'),
            ).reset_index())
        ######## daily_counts && daily_velocity
        daily_counts=(df.groupby(['nameOrig','day']).size().reset_index(name='daily_count'))
        daily_velocity=(daily_counts.groupby('nameOrig')['daily_count'].mean().reset_index(name='daily_velocity'))
        features=features.merge(daily_velocity,on='nameOrig',how='left')
        features['daily_velocity']=features['daily_velocity'].fillna(0)
        
        ####### Rolling Features
        df_sorted=df.sort_values(['nameOrig','step'])
        df_sorted['rolling_amount']=(df_sorted.groupby('nameOrig')['amount'].rolling(window=10,min_periods=1).std().reset_index(level=0,drop=True))
        rolling_feature=(df_sorted.groupby('nameOrig')['rolling_amount'].max().reset_index(name='max_rolling_amount'))
        
        #########  Merge with other features
        features=features.merge(rolling_feature,on='nameOrig',how='left')
        features['max_rolling_amount']=features['max_rolling_amount'].fillna(0)
        
        df['invalid_balance']=((df['type']!='CASH_IN')&(abs(df['oldbalanceOrg']-df['amount']-df['newbalanceOrig'])>0.1))
        invalid_balance_rate=(df.groupby('nameOrig')['invalid_balance'].mean().reset_index(name='invalid_balance_rate'))
        features=features.merge(invalid_balance_rate,on='nameOrig',how='left')
        features['invalid_balance_rate']=(features['invalid_balance_rate'].fillna(0))
        
        return features
