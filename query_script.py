#Takes the query and sends the result
#import pandas as pd,os
import os
from QueryMaker import querycontroller

q_i = querycontroller.QueryController()

num = len([name for name in os.listdir('./sample_tokens') if os.path.isfile(name)])
#token_list = pd.read_csv('sample_tokens/')
print(num)
print(q_i.get_file_name())

