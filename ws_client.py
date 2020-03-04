import websocket
import threading
import json
import time
from bytes_marketdata import CliMarketdataRes
        
def heartbeat_thread(clientSocket):
    while clientSocket:
        send_data = '{"a": "h", "v": [], "m": ""}'
        try:
            clientSocket.send(send_data)
        except Exception as e:
            print(e)
            print("HEARTBEAT [ERROR]: [BLITZ_HYDRA_STREAM] Connection closed.")
            break
        print("Sent Heart-Beat to Exchange")
        time.sleep(8)

        
def on_message(ws, message):
    marketdataPkt = CliMarketdataRes()

    # mode is always 0, so putting check on length also
    if marketdataPkt.mode == 0 and len(message) != 86:
        print('heartbeat')
        return

    marketdataPkt.get_CliMarketdataRes_Instruct(message)
    print('\n')
    print('exchange_code', marketdataPkt.exchange_code)
    print('instrument_token', marketdataPkt.instrument_token)
    print('last_traded_price', marketdataPkt.last_traded_price)
    print('last_traded_time', marketdataPkt.last_traded_time)
    print('last_traded_quantity', marketdataPkt.last_traded_quantity)
    print('trade_volume', marketdataPkt.trade_volume)
    print('best_bid_price', marketdataPkt.best_bid_price)
    print('best_bid_quantity', marketdataPkt.best_bid_quantity)
    print('best_ask_price', marketdataPkt.best_ask_price)
    print('best_ask_quantity', marketdataPkt.best_ask_quantity)
    print('total_buy_quantity', marketdataPkt.total_buy_quantity)
    print('total_sell_quantity', marketdataPkt.total_sell_quantity)
    print('average_trade_price', marketdataPkt.average_trade_price)
    print('exchange_timestamp', marketdataPkt.exchange_timestamp)
    print('open_price', marketdataPkt.open_price)
    print('high_price', marketdataPkt.high_price)
    print('low_price', marketdataPkt.low_price)
    print('close_price', marketdataPkt.close_price)
    print('yearly_high_price', marketdataPkt.yearly_high_price)
    print('yearly_low_price', marketdataPkt.yearly_low_price)


def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    hbThread = threading.Thread(target=heartbeat_thread, args=(ws,))
    hbThread.start()
    sub_packet = {
        "a": "subscribe",
        "v": [[1,3045], [1, 22]],
        "m": "marketdata"
    }

    ws.send(json.dumps(sub_packet))

    # for pair in sub_packet["v"]:
    #     temp_packet = {
    #         "a": "subscribe",
    #         "v": [pair],
    #         "m": "marketdata"
    #     }
    #     ws.send(json.dumps(temp_packet))


def handle_streams(access_token):
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(f"wss://ant.aliceblueonline.com/hydrasocket/v2/websocket?access_token={'access_token'}",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
