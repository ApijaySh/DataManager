import pandas as pd,json,os
from datetime import datetime
from kiteconnect import KiteConnect
from .config import api_key,api_secret

class connecttools:

    def __init__(self):
        self.api_key = api_key
        self.api_secret = api_secret

    def connect(self):
        k_instance = KiteConnect(api_key=self.api_key)
        return k_instance,k_instance.login_url()
    
    def establish(self,req_token,k_instance):
        data = k_instance.generate_session(req_token,api_secret=self.api_secret)
        k_instance.set_access_token(data['access_token'])
        return data
    
    def get_instruments(self,k_instance,EXCHANGE):
        instruments = k_instance.instruments(exchange=EXCHANGE)
        df = pd.DataFrame(instruments)
        return df
    

class datacollector:

    def __init__(self):   
        pass

    def store_as_json(self,data):

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()

        json_object = json.dumps(data, indent = 4, default=str)
        num = len([name for name in os.listdir('/sample_data/') if os.path.isfile(name)])
        with open("sample_data/sample{num}.json".format(num = num), "w") as outfile: 
            outfile.write(json_object)
    
    def store_as_csv(self,data):
        time_now = datetime.datetime.now()
        formated_time = time_now.strftime('%y-%m-%d-%H-%M-%S')
        data.to_csv('sample_tokens/od_csv_{date}.csv'.format(date = formated_time))

        

    

    
    