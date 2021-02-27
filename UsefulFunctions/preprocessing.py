import glob
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from workalendar.asia import SouthKorea
import matplotlib.pyplot as plt
import seaborn as sns

# ===== SAVE FUNCTIONS =====
def save_pickle(df, path, model, company, network, version, date, option=False, add=None):
    if option == True:
        filename = f'{path}{date}_{model}_{company}_{network}_{add}_{version}.pkl'
        print('저장 위치 : ', filename)

        files_present = glob.glob(filename)
        if not files_present:
            df.to_pickle(filename)
            print('Export complete!')
        else:
            print('WARNING: This pickle file already exists!')
        
    else:
        filename = f'{path}{date}_{model}_{company}_{network}_{version}.pkl'
        print('저장 위치 : ', filename)
        files_present = glob.glob(filename)
        if not files_present:
            df.to_pickle(filename)
            print('Export complete!')
        else:
            print('WARNING: This pickle file already exists!')

        
def save_csv(df, path, model, company, network, version, date):
    filename = f'{path}{date}_{model}_{company}_{network}_{version}.csv'
    print('저장 위치 : ', filename)
    
    files_present = glob.glob(filename)
    if not files_present:
        df.to_csv(filename, encoding='utf-8-sig')
        print('Export complete!')
    else:
        print('WARNING: This csv file already exists!')


def save_scale(scaler, path, model, company, network, date, method, version):
    filename = f'{path}{date}_{model}_{company}_{network}_{method}_{version}.pkl'
    print('저장 위치 : ', filename)
    
    files_present = glob.glob(filename)
    if not files_present:
        joblib.dump(scaler, filename)
        print('Export complete!')
    else:
        print('WARNING: This scale file already exists!')
        
        
def save_model(weights, path, model, company, network, version, date):
    filename = f'{path}{date}_{model}_{company}_{network}_{version}.h5'
    print('저장 위치 : ', filename)
    
    files_present = glob.glob(filename)
    if not files_present:
        weights.save(filename)
        print('Export complete!')
    else:
        print('WARNING: This model h5 file already exists!')


# ===== Reduce memory by changing datatype =====
def reduce_mem(df, verbose=True):
    '''
    Change datatype to reduce size
    
    Args:
        df: dataframe to reduce size
    
    Returns:
        dataframe
    '''
    
    #--- Data Check: before reducing Mem ---
    print('--- Before Reducing memory ---')
    print(list(df), df.info())
    print('-'*50)
    print() 
        
    #--- Reduce Memory ---
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    start_mem = df.memory_usage().sum() / 1024**2    
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)    
    print('--- Memory Reduced ---')
    end_mem = df.memory_usage().sum() / 1024**2
    if verbose: print('  --> Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)'.format(end_mem, 100 * (start_mem - end_mem) / start_mem))
    print()    
    print('-'*50)  
    
    #--- Data Check: before reducing Mem ---
    print()
    print('--- After Reducing memory ---')
    print(list(df), df.info())
    print('-'*50)        
    return df


def read_preprocess(path,filename):
    '''
    Read Dataframe and output basic info
    
    Args:
        df: dataframe to reduce size
    
    Returns:
        shape, null, nuniques
    '''
    #--read file
    path = path
    df = pd.read_csv('{0}/{1}.csv'.format(path,filename))
    
    #--preprocess
    print('----- {}: shape -----'.format(filename))
    print(df.shape)
    print()
    print('----- {}: null % -----'.format(filename))
    print(df.isna().mean().sort_values(ascending=False))
    print()
    print('----- {}: nunique -----'.format(filename))
    print(df.nunique().sort_values(ascending=False))
    print()
    
    #--unique values
    print('----- {}: unique vals list -----'.format(filename))
    col_list = df.columns.to_list()
    for i in col_list:
        small_nunique = df[i].nunique()
        if small_nunique < 25:
            print('------------ {}: -----'.format(i))
            print('{}\n'.format(df[i].value_counts(dropna=False)))
    
    #--timeline range
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'],format = "%Y-%m-%d %H:%M:%S")
        print("----- {}: Timestamp Range -----".format(filename))
        print(df['timestamp'].min(), '~', df['timestamp'].max())
        print()
        print('----- {}: unique timestamp -----'.format(filename))
        print(df.timestamp.dt.year.unique())
    
    print()
    print('----- {}: describe -----'.format(filename))
    print(df.describe())
    print()
    return df
    

def compare_tr_te(df1,df2, col_num):
    fig, ax = plt.subplots(figsize=(20,15), nrows=3, ncols=3)
    k=1
    for i in range(3):
        for j in range(3):
            if k < col_num+1:
                sns.distplot(df1.iloc[:, k+1].dropna(), ax=ax[i][j], color='green')
                sns.distplot(df2.iloc[:, k+1].dropna(), ax=ax[i][j], color='red')
                k += 1
    fig.legend(labels=['train', 'test'])
pass


# ===== Highlight Dataframe =====
def color_ones_red(val, c1='red', c2='white'):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for ones, black otherwise.
    """
    color = c1 if val == 1 else c2
    return 'color: %s' % color



def color_negative_red(val, c1='red', c2='white'):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = c1 if val == 1 else c2
    return 'color: %s' % color


# ===== TIME RELATED =====
def date_features(df, date_col):
    '''
    Converts time feature to time dtype
    
    Args:
        date column
        
    Returns:
        date column
        
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
    df['weeknum'] = df[date_col].dt.weekday
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
    '''
    Divide time into timerange
    '''
    
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
    return df


