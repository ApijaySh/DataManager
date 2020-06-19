from kiteconnect import KiteTicker
from .zerodhatools import datacollector


def ws_zerodha(api_key,data,token):
    Tick_List = []
    kws = KiteTicker(api_key, data["access_token"])

    def on_ticks(ws, ticks):
        # Callback to receive ticks.
        Tick_List.append(ticks)
        datacollector.store_as_json(Tick_List)
        print("Ticks: {}".format(ticks))

    def on_connect(ws, response):
        # Callback on successful connect.
        # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
        #ws.subscribe([738561, 5633])

        # Set RELIANCE to tick in `full` mode.
        ws.set_mode(ws.MODE_FULL, token)
    

    def on_close(ws, code, reason):
        # On connection close stop the main loop
        # Reconnection will not happen after executing `ws.stop()`
        ws.stop()

    # Assign the callbacks.
    kws.on_ticks = on_ticks
    kws.on_connect = on_connect
    kws.on_close = on_close

    # Infinite loop on the main thread. Nothing after this will run.
    # You have to use the pre-defined callbacks to manage subscriptions.
    kws.connect(threaded=True)