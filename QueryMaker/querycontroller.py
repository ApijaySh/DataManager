#Creates Query for Zerodha API Data
from datetime import datetime
import os

class QueryController:

    def __init__(self):
        pass

    def search(self,j_object,index_list):
        D_list = []
        for dict in j_object:
            if dict['instrument_token'] in index_list:
                D_list.append(dict)
            else:
                pass
        return D_list


    def query(self):
        pass

    def get_file_name(self):
        #time_now = datetime.datetime.now()
        #formated_time = time_now.strftime('%y-%m-%d-%H-%M-%S')
        file_list = [name for name in os.listdir('./sample_tokens/') if os.path.isfile(name)]
        return file_list