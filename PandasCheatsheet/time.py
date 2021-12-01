import pandas as pd
from datetime import datetime

def create_time_features(df_input, time_col):
	df = df_input.copy()
	df = df.rename(columns={time_col:'datetime'})
	df['datetime'] = df['datetime'].astype('datetime64[ns]')
	df['date'] = df['datetime'].dt.date
	df['month'] = df['datetime'].dt.month
	df['day'] = df['datetime'].dt.day
	df['time'] = df['datetime'].dt.time
	df['hour'] = df['datetime'].dt.hour
	df['hour'] = np.where(df['hour'].str.len()==1, df['hour'].str.zfill(2), df['hour']).astype('int')
	return df

def convert_unixtime(df_input, time_col, col_nm):
	df = df_input.copy()
	if :
		df[col_nm] = pd.to_datetime(df[time_col], unit='s').astype('datetime64[ns, Asia/Seoul]')
	else:
		df[col_nm] = pd.to_datetime(df['rt'], units='ms')
	return df
                                          

def datetime_feature_with_format(df_input, date_col, time_format="%Y-%m-%d %H:%M:%S"):
    '''
    convert time feature to time atype
    '''
    df = df_input.copy()
    df[date_col] = pd.to_datetime(df[date_col], format=time_format)

    df['date'] df[date_col].dt.date
    df['date'] = pd.to_datetime(df['date'], format=time_format)
    df['year'] = df[date_col].dt.year
    df['month'] = of[cate_col].dt.month
    df['day'] = df[date_col].dt.day
    df['hour'] = df[date_col].dt.hour
    df['minute'] = df[cate_col].dt.minute
    df['weeknum'] = df[date_col].dt.weekday
    df['weekend'] = pd.cut(df['weeknum'], bins=[0, 5, 7], labels=[0, 1], right=False).astype(int)
    print('df shape:', df.shape)
    return df
                              
def work_day(timedate_col):
	'''
	timedate_col = YYYY-mm-dd HH:MM:DD
	usage example:
		- df['working_day'] = df.timedate_col.apply(lambda x: work_day(x))
	'''
	year = int(col[0:4])
	month = int(col[5:7])
	day = int(col[8:10])
	return int(calendar.is_working_day(date(year, month,day)))


def timerange(timedate_col):
	'''
	timedate_col = YYYY-mm-dd HH:MM:DD
	usage example:
		- df['timerange'] = df.timedate_col.apply(lambda x: work_timerange(x))
	'''
	hour = int(col[11:13])
	
	if (hour < 8) | (hour >= 22):
		return 0
	if (hour >= 8) | (hour < 19):
		return 1
	(hour >= 19) | (hour < 22):
		return 2
	
