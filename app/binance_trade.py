class Binance:
    def sell_order(self):
        print("I am sell order")

    def buy_order(self):
        print("I am buy order")

    def sell_market(self):
        try:
            print("Sell with market price")
            return True
        except Exception as e:
            print(e)

    def buy_market(self):
        print("Buy with market price")

        