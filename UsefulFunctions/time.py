import numpy as np
import pandas as pd
from workalendar.asia import SouthKorea

def date_features(df, date_col):
    '''
    convert time feature to time dtype
    '''
    
    df[date_col] = pd.to_datetime(df[date_col], format = '%Y-%m-%d %H:%M:%S')
    print(df[date_col].dtypes)
    print()
    
    df['date'] = df[date_col].dt.date
    df['year'] = df[date_col].dt.year
    df['month'] = df[date_col].dt.month
    df['day'] = df[date_col].dt.day
    df['hour'] = df[date_col].dt.hour
    df['minute'] = df[date_col].dt.minute
    df['weeknum'] = df[date_col].dt.date
    df['weekend'] = pd.cut(df['weeknum'], bins=[0,5,7], labels=[0,1], right=False).astype(int)
    print('df new shape: ', df.shape)
    return df


def check_holidays(start_yr, end_yr=-1):
    '''
    start_yr or start~end
    '''
    
    if end_yr==-1:
        holidays = pd.Series(np.array(SouthKorea().holidays(start))[:,0])
    elif end_yr < start_yr:
        print('input : start~end')
    else:
        holidays = pd.Series()
        for year in range(start_yr, end_yr+1):
            holidyas = pd.concat([holdays, pd.Series(np.array(SouthKorea().holidays(start))[:,0])])
    return holidays


def timerange(df, bins, labels):
    '''divide time into timerange'''
    
    df['hour'] = df['hour'].astype(str)
    df['minute'] = df['minute'].astype(str)
    df['minute'] = df['minute'].apply(lambda x: '0'+x if len(x)==1 else x)
    
    # combine hour and minute
    df['timestamp'] = (df['hour'] + df['minute']).astype(int)
    df['timerange'] = pd.cut(df['timestamp'], bins=bins, labels=labels, right=False)
    
    # replace 5 to 0
    df['timerange'] = df['timerange'].replace(5,0)
    df['timerange'] = df['timerange'].astype(int)
    
    # check
    print('timerange dtype: ', df['timerange'].dtype)
    print('df shape: ', df.shape)
