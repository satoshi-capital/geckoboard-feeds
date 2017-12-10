import gdax, time, json, _thread

class myWebsocketClient(gdax.WebsocketClient):
            
    def on_open(self):
        self.data_ = []
        self.url = "wss://ws-feed.gdax.com/"
        self.products = ["BTC-USD"]
        self.message_count = 0
        print("Starting...")
    def on_message(self, msg):
        #Keep track of total messages
         #dict_keys(['type', 'trade_id', 'maker_order_id', 'taker_order_id', 'side', 'size', 'price', 'product_id', 'sequence', 'time'])
        self.message_count += 1
        if 'type' in msg:
            try:
                #Feed the message into the data sorting algo
                #Start new thread
                #_thread.start_new_thread(data_parser.feed(msg),())
                #data_parser.feed(msg)
                if (sys.getsizeof(self.data_)< 900000):
                    print(sys.getsizeof(self.data_))
                    self.data_.append(msg)
                    print('PRICE: '+msg['price'] + ' SIZE: ' + msg['size'])
                    print(self.data_)
                else:
                    self.data_.pop()
                    self.data_.append(msg)
                    print(self.data_)
            except: pass
            
    def on_close(self):
        print("Finished.")

wsClient = myWebsocketClient()
wsClient.start()

#data_parser = json_parser.myFeed()

print(wsClient.url, wsClient.products)
while (wsClient.message_count < 10):
    time.sleep(1)
wsClient.close()

#https://github.com/danpaquin/gdax-python/blob/master/gdax/websocket_client.py
#https://github.com/danpaquin/gdax-python/blob/master/README.md
