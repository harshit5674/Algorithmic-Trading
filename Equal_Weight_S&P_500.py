import xlsxwriter
import numpy as np
import requests
import pandas as pd
import math
from IPython.display import display, HTML


dp=pd.read_csv('sp_500_stocks.csv')

from secrets import IEX_CLOUD_API_TOKEN
stock='AAPL'


api_url=f'https://sandbox.iexapis.com/stable/stock/{stock}/quote/?token={IEX_CLOUD_API_TOKEN}'

#executing a http request

data=requests.get(api_url).json()

price=data['latestPrice']
market_cap=data['marketCap']

col=['Ticker','Stock Price','Market Capitalization','Number of Shares to Buy']
final_dp=pd.DataFrame(columns=col)


#adding a row to a pandas dataframe
m={}
m['Ticker']=[stock]
m['Stock Price']=[price]
m['Market Capitalization']=[market_cap]
m['Number of Shares to Buy']=['N/A']

dp_temp=pd.DataFrame(m)
final_dp=pd.concat([final_dp,dp_temp],ignore_index=True)
final_dp.reset_index()

final_dp=pd.DataFrame(columns=col)

count=0

for stock in dp['Ticker'][:5]:
	api_url=f'https://sandbox.iexapis.com/stable/stock/{stock}/quote/?token={IEX_CLOUD_API_TOKEN}'
	data=requests.get(api_url).json()
	m={}
	m['Ticker']=[stock]
	m['Stock Price']=[price]
	m['Market Capitalization']=[market_cap]
	m['Number of Shares to Buy']=['N/A']
	dp_temp=pd.DataFrame(m)
	final_dp=pd.concat([final_dp,dp_temp],ignore_index=True)
	final_dp.reset_index()

display(final_dp)
