from instruments_tools import get_df,filter_df_name,filter_df_date,get_instruments
import pandas as pd
from datetime import date

df = get_instruments()
df_nfo = get_df(df)
df_nifty_raw = filter_df_name(df_nfo,'NIFTY')
df_nifty = filter_df_date(df_nifty_raw)
df_nifty.to_csv('tokens/nifty_{y}_{m}_{d}.csv'.format(m = date.today().month,y = date.today().year,d = date.today().day, header=False, index=False))

df_banknifty_raw = filter_df_name(df_nfo,'BANKNIFTY')
df_banknifty = filter_df_date(df_banknifty_raw)
df_banknifty.to_csv('tokens/banknifty_{y}_{m}_{d}.csv'.format(m = date.today().month,y = date.today().year,d = date.today().day, header=False, index=False))

df_else_raw = df_nfo[(df_nfo['name'] != 'NIFTY') & (df_nfo['name'] != 'BANKNIFTY')]
df_else = filter_df_date(df_else_raw)
df_else.to_csv('tokens/else_{y}_{m}_{d}.csv'.format(m = date.today().month,y = date.today().year,d = date.today().day, header=False, index=False))

