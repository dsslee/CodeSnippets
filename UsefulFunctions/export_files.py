import glob
import pandas as pd
from sklearn.externals import joblib

def save_pickle(df, path, model, company, network, date, version):
    filename = f'{path}{model}_{company}_{network}_{date}_{version}.pkl'
    print('저장 위치 : ', filename)
    
    files_present = glob.glob(filename)
    if not files_present:
        df.to_pickle(filename)
        print('Export complete!')
    else:
        print('WARNING: This pickle file already exists!')

        
def save_csv(df, path, model, company, network, date, version):
    filename = f'{path}{model}_{company}_{network}_{date}_{version}.csv'
    print('저장 위치 : ', filename)
    
    files_present = glob.glob(filename)
    if not files_present:
        df.to_csv(filename)
        print('Export complete!')
    else:
        print('WARNING: This csv file already exists!')


def save_scale(scaler, path, model, company, network, date, version, method):
    filename = f'{path}{model}_{company}_{network}_{date}_{version}_{method}.pkl'
    print('저장 위치 : ', filename)
    
    files_present = glob.glob(filename)
    if not files_present:
        joblib.dump(scaler, filename)
        print('Export complete!')
    else:
        print('WARNING: This scale file already exists!')
        
        
def save_weights(weights, path, model, company, network, date, version):
    filename = f'{path}{model}_{company}_{network}_{date}_{version}.h5'
    print('저장 위치 : ', filename)
    
    files_present = glob.glob(filename)
    if not files_present:
        weights.save_weights(filename)
        print('Export complete!')
    else:
        print('WARNING: This h5 file already exists!')
