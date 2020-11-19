import os 
import sys
import datetime
import time
from Robinhood import Robinhood



def get_stonk_login:
	robinhood_client = Robinhood()
	robinhood_client.login(username='yourusername@mail.com', password='yourpassword')


def buy():
	print("Buying NIO...")
	buy_order = robinhood_client.place_market_buy_order(stock_instrument['url'], 'NIO', 'GFD', 1)
	order_id = order.json()['id']


def sell():
	print("Selling NIO...")
	sell_order = robinhood_client.place_market_sell_order(stock_instrument['url'], 'DWT', 'GFD', 1)
	order_id = order.json()['id']

def get_NIO_info():
	quote = robin_stocks.stocks.get_ratings('NIO', info=None)
	quote_two = rh.print_quote("NIO")
	return quote

if '__name__' == '__main__':

	get_stonk_login()
	get_NIO_info()
	if quote > "46.70":
		sell()
	else:
		buy()
	
