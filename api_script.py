#API-Script and other functions
from ZerodhaAPIController.zerodhatools import connecttools
from ZerodhaAPIController.ws_zerodha import ws_zerodha
from kiteconnect import KiteConnect
from ZerodhaAPIController.config import api_key
from kiteconnect import KiteTicker
from ZerodhaAPIController.zerodhatools import datacollector
import logging

logging.basicConfig(level=logging.DEBUG)

#get login url

c_i = connecttools()
tool_i = datacollector()

k_instance,l_url = c_i.connect()

print("Your Login URL: ",l_url)
req_token = input("Enter Your REQUEST TOKEN : ")

data = c_i.establish(req_token,k_instance)
print(data)
print(data["access_token"],api_key,"Creds")

df = c_i.get_instruments(k_instance,EXCHANGE='NFO')
tool_i.store_as_csv(df)

token_list = df['instrument_token']
print('Lenght :', len(token_list))



#p = ws_zerodha(api_key=api_key,data=data,token=token_list)
Tick_List = []
kws = KiteTicker(api_key, data["access_token"])
print('GH')
def on_ticks(ws, ticks):
    # Callback to receive ticks.
    logging.debug("Ticks: {}".format(ticks))
    Tick_List.append(ticks)
    tool_i.store_as_json(Tick_List)
    print("Ticks: {}".format(ticks))

def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe(list(token_list[:100]))

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, list(token_list[:100]))


def on_close(ws, code, reason):
    # On connection close stop the main loop
    # Reconnection will not happen after executing `ws.stop()`
    ws.stop()
print('TY')
# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close
print('JJ')
# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()
print('HUJ')


