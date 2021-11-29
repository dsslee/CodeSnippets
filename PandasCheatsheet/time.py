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

def convert_unixtime(df_input, time_col):
	df = df_input.copy()
	pass
	return df


	
