import pandas as pd,requests,datetime,csv
from datetime import date

def get_df(dframe,EXCHANGE = 'NFO',DIR=None,is_df=True):
    if is_df:
        df = dframe
    else:
        df = pd.read_csv(DIR)
    df['expiry'] = pd.to_datetime(df['expiry'])
    df_ex = df[df['exchange'] == EXCHANGE]
    return df_ex

def filter_df_name(df,name):
    df_name = df[df['name'] == name]
    return df_name

def filter_df_date(df):
    y,m = date.today().year,date.today().month
    df_y = df[df['expiry'].dt.year == y]
    df_m = df_y[
        (df_y['expiry'].dt.month == m)
        | (df_y['expiry'].dt.month == m+1) 
        | (df_y['expiry'].dt.month == m+2)
    ]
    return df_m  

def get_instruments():
    headers = {
        'Content-type': 'application/json',
        'X-Kite-Version':'3',
    }
    response = requests.get('https://api.kite.trade/instruments', headers=headers)
    if response.status_code == 200:
        data = response.content.decode('utf-8')
        filename = "tokens/instruments_{y}_{m}_{d}.csv".format(m = date.today().month,y = date.today().year,d = date.today().day)
        with open(filename, 'w') as csvfile:
            cr = csv.reader(data.splitlines(), delimiter=',')
            csvwriter = csv.writer(csvfile) 
            data_list = list(cr)
            csvwriter.writerows(data_list)
        df = pd.read_csv("tokens/instruments_{y}_{m}_{d}.csv".format(m = date.today().month,y = date.today().year,d = date.today().day))
        return df 
    else:
        return "error"
    

    