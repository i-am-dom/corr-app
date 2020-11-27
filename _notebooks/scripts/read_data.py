import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import requests

def read():
    df1 = pd.read_csv("CSV/ETH_BTC_USD_2015-08-09_2020-04-04-CoinDesk.csv")
    df1.columns = ['date', 'ETH', 'BTC']
    df1.date = pd.to_datetime(df1.date, dayfirst=True)
    df1.set_index('date', inplace=True)
    
    EOS = pd.read_csv("ICO_coins/EOS_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    IOTA = pd.read_csv("ICO_coins/IOTA_USD_2018-06-06_2020-04-02-CoinDesk.csv") 
    LSK = pd.read_csv("ICO_coins/LSK_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    NEO = pd.read_csv("ICO_coins/NEO_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    TRX = pd.read_csv("ICO_coins/tron/TRX_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    ADA = pd.read_csv("ICO_coins/cardano/ADA_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    GOLD = pd.read_csv("CSV/XAU-GOLD_USD_Historical Data_2018-06-06--2020-04-04.csv")
    SP500 = pd.read_csv("CSV/S_P_500_Historical Data_2018-06-06--2020-04-04.csv")
    
    GOLD['Currency'] = GOLD.apply(lambda row:'XAU', axis=1)
    SP500['Currency'] = SP500.apply(lambda row:'SP500', axis=1)
    
    df = EOS.append(IOTA).append(LSK).append(NEO).append(TRX).append(ADA).append(GOLD).append(SP500)
    df.Date = pd.to_datetime(df.Date, dayfirst=True)

    df['Closing Price (USD)'] = df.apply(lambda row: str(row['Closing Price (USD)']).replace(',', ''), axis=1 )
    df['Closing Price (USD)'] = df['Closing Price (USD)'].astype(float)

    tbl = df.pivot_table('Closing Price (USD)', ['Date'], 'Currency')
    tbl=tbl.dropna()
    
    df_all = pd.concat([df1,tbl], join='inner', axis=1)
    
    return df_all







def read_json():
    
    BTChistory_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    EOShistory_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=EOS&tsym=USD&limit=2000&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    LSKhistory_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=LSK&tsym=USD&limit=2000&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    
    BTChistory = requests.get(BTChistory_url).json() 
    pd_BTC = pd.read_json(BTChistory_url, typ='series')['Data']['Data'] 
    
    
    
    '''
    df1 = pd.read_csv("CSV/ETH_BTC_USD_2015-08-09_2020-04-04-CoinDesk.csv")
    df1.columns = ['date', 'ETH', 'BTC']
    df1.date = pd.to_datetime(df1.date, dayfirst=True)
    df1.set_index('date', inplace=True)
    
    EOS = pd.read_csv("ICO_coins/EOS_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    IOTA = pd.read_csv("ICO_coins/IOTA_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    LSK = pd.read_csv("ICO_coins/LSK_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    NEO = pd.read_csv("ICO_coins/NEO_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    TRX = pd.read_csv("ICO_coins/tron/TRX_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    ADA = pd.read_csv("ICO_coins/cardano/ADA_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    GOLD = pd.read_csv("CSV/XAU-GOLD_USD_Historical Data_2018-06-06--2020-04-04.csv")
    SP500 = pd.read_csv("CSV/S_P_500_Historical Data_2018-06-06--2020-04-04.csv")
    
    GOLD['Currency'] = GOLD.apply(lambda row:'XAU', axis=1)
    SP500['Currency'] = SP500.apply(lambda row:'SP500', axis=1)
    
    df = EOS.append(IOTA).append(LSK).append(NEO).append(TRX).append(ADA).append(GOLD).append(SP500)
    df.Date = pd.to_datetime(df.Date, dayfirst=True)

    df['Closing Price (USD)'] = df.apply(lambda row: str(row['Closing Price (USD)']).replace(',', ''), axis=1 )
    df['Closing Price (USD)'] = df['Closing Price (USD)'].astype(float)

    tbl = df.pivot_table('Closing Price (USD)', ['Date'], 'Currency')
    tbl=tbl.dropna()
    
    df_all = pd.concat([df1,tbl], join='inner', axis=1)'''
    
    return df_all


def read_crypto():
    df1 = pd.read_csv("CSV/ETH_BTC_USD_2015-08-09_2020-04-04-CoinDesk.csv")
    df1.columns = ['date', 'ETH', 'BTC']
    df1.date = pd.to_datetime(df1.date, dayfirst=True)
    df1.set_index('date', inplace=True)
    
    EOS = pd.read_csv("ICO_coins/EOS_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    IOTA = pd.read_csv("ICO_coins/IOTA_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    LSK = pd.read_csv("ICO_coins/LSK_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    NEO = pd.read_csv("ICO_coins/NEO_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    TRX = pd.read_csv("ICO_coins/tron/TRX_USD_2018-06-06_2020-04-02-CoinDesk.csv")
    ADA = pd.read_csv("ICO_coins/cardano/ADA_USD_2018-06-06_2020-04-02-CoinDesk.csv")


    
    df = EOS.append(IOTA).append(LSK).append(NEO).append(TRX).append(ADA)
    df.Date = pd.to_datetime(df.Date, dayfirst=True)

    df['Closing Price (USD)'] = df.apply(lambda row: str(row['Closing Price (USD)']).replace(',', ''), axis=1 )
    df['Closing Price (USD)'] = df['Closing Price (USD)'].astype(float)

    tbl = df.pivot_table('Closing Price (USD)', ['Date'], 'Currency')
    tbl=tbl.dropna()
    
    df_all = pd.concat([df1,tbl], join='inner', axis=1)
    
    return df_all

def read_api(): 
    BTChistory_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    EOShistory_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=EOS&tsym=USD&limit=2000&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    LSKhistory_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=LSK&tsym=USD&limit=2000&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    XAUhistory_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=XAU&tsym=USD&limit=2000&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    ETHhistory_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=ETH&tsym=USD&limit=2000&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    ADAhistory_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=ADA&tsym=USD&limit=2000&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    
    XRPhistory_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=XRP&tsym=USD&limit=2000&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    
    NEOhistory_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=NEO&tsym=USD&limit=2000&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    TRXhistory_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=TRX&tsym=USD&limit=2000&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    SP500history_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=US500.CUR&tsym=USD&e=currency&limit=2000&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    
    BTC = format_response(BTChistory_url, 'BTC') 
    EOS = format_response(EOShistory_url, 'EOS') 
    LSK = format_response(LSKhistory_url, 'LSK') 
    XAU = format_response(XAUhistory_url, 'XAU') 
    ETH = format_response(ETHhistory_url, 'ETH')
    ADA = format_response(ADAhistory_url, 'ADA')
    
    XRP = format_response(XRPhistory_url, 'XRP')

    NEO = format_response(NEOhistory_url, 'NEO')
    TRX = format_response(TRXhistory_url, 'TRX')
    SP500 = format_response(SP500history_url, 'SP500')

    df = BTC.append(EOS).append(LSK).append(XAU).append(ETH).append(ADA).append(NEO).append(TRX).append(XRP).append(SP500) 
    tbl = df.pivot_table('close', ['date'], 'currency')
    tbl = tbl.dropna() 
    return tbl

def read_news(category): 
    url1 = 'https://min-api.cryptocompare.com/data/v2/news/?categories='
    url2 = '&api_key=c96436b332e3c9f1b6784db0ec59cb81b161eb5853ecfa81cc025366512d6594'
    url = url1 + category + url2    
    response = format_news(url, category)
    #df = BTC.append(EOS).append(LSK).append(XAU).append(ETH).append(ADA).append(NEO).append(TRX).append(XRP) 
    #tbl = df.pivot_table(['date'], ['imageurl'], ['title'], ['url'], ['category'])
    #tbl = tbl.dropna() 
    return response

def read_covid(): 
    url = 'https://newsapi.org/v2/everything?q=covid&sources=bbc-news%2Cassociated-press&apiKey=1c5ca7e1e5c349cdb7ec5d1a40dc66fa&fbclid=IwAR3K8zO7eGe-Y6VFCzyyxwIrw68ktKmU-er-IOsTN9BuGfNIpK1ulo-IGzA'
    pd_resp = pd.read_json(url, typ='series')['articles'][0] 
    df_resp = pd.DataFrame(pd_resp) 
    df_final = df_resp[['title', 'description', 'url']]
    return df_final.iloc[0]
    
    
def format_response(url, fsym): 
    pd_resp = pd.read_json(url, typ='series')['Data']['Data']
    df_resp = pd.DataFrame(pd_resp)
    df_resp['date'] = pd.to_datetime(df_resp.time, unit='s')
    df_final = df_resp[['close', 'date']]
    df_final['currency'] = df_final.apply(lambda row: fsym, axis=1) 
    return df_final

def format_news(url, category):  
    pd_resp = pd.read_json(url, typ='series')['Data'][0]  
    df_resp = pd.DataFrame(pd_resp)
    df_resp['date'] = pd.to_datetime(df_resp.published_on, unit='s')
    df_final = df_resp[['date', 'imageurl', 'title', 'body', 'url']]
    df_final['category'] = df_final.apply(lambda row: category, axis=1)    
    return df_final.iloc[0]

