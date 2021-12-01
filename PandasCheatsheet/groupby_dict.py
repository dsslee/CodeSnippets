key_lst = df.key.unique().tolist()
kv_key_dict = {key:set([i for i in g.index]) for key, g in df[['key']].groupby('key')}

for i, df_key in enumerate(key_lst):
  related_idx = kv_df_key[df_key]
  df_related = df.loc[related_idx]
  
  # ===== feature add =====
  file_cnt = (df_related['file_cnt'].sum())
  
  
  feat_lst = [file_cnt]
  
  if i == 0:
    n_features = len(feat_lst)
    df_gr = pd.DataFrame(index=range(len(key_lst)), columns = range(n_feautres+1))
    
  grouped_df.iloc[i,0] = df_key
  grouped_df.iloc[i,1:] = feat_lst
  
