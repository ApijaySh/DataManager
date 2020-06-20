#Takes the query and sends the result
import pandas as pd,os,json

from QueryMaker import querycontroller

q_i = querycontroller.QueryController()

f_list = q_i.get_file_name()
df_nfo = q_i.get_df(dir='./sample_tokens/',f_name=f_list[-1])

NAME = "ACC"
EXP_DATE = "20JUN"
OPTION = "NFO-FUT"

df_test = q_i.query(df_nfo,NAME,EXP_DATE,OPTION,f=False)
print(df_test)

search_index = df_test['instrument_token']

print(list(search_index))

obj = open('./sample_data/sample0.json')
data_json = json.load(obj)

search_res = q_i.search(data_json,list(search_index))
print(search_res)
