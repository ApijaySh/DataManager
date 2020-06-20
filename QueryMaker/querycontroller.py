#Creates Query for Zerodha API Data
from datetime import datetime
import os,pandas as pd

class QueryController:

    def __init__(self):
        pass

    def search(self,j_object,index_list):
        D_list = []
        for dict in j_object:
            for dict_i in dict:
                if dict_i['instrument_token'] in index_list:
                    D_list.append(dict_i)
                else:
                    pass
        return D_list
    
    def get_df(self,dir,f_name):
        ADDR = dir + f_name
        df = pd.read_csv(ADDR)
        return df

    def query(self,df,symbol=None,exp_date=None,segment=None,f=True):
        if symbol:
            df_init = df[df['name'] == symbol]
            if exp_date:
                df_exp = df_init[df_init['tradingsymbol'].str.contains(exp_date)]
                if segment:
                    if f:
                        df_seg = df_exp[df_exp['segment'] == segment]
                        return df_seg
                    else:
                        df_seg = df_exp[df_exp['segment'] != segment]
                        return df_seg                    
                else:
                    return df_exp
            else:
                return df_init
        else:
            return df
            
    def get_file_name(self):
        #time_now = datetime.datetime.now()
        #formated_time = time_now.strftime('%y-%m-%d-%H-%M-%S')
        file_list = os.listdir('./sample_tokens/')
        return file_list

        