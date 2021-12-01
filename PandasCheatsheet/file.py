import pandas as pd

df['file_extension'] = df['filename'].astype('str').apply(lambda x: x.split('.')[-1] if '.' in x else 'unknown')
