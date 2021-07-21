import yfinance as yf
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import streamlit as st
import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


Symbol = ["AAPL", "MSFT","AMZN", "FB","GOOG", "GOOGL", "TSLA", "NVDA", "PYPL", "ASML","INTC","CMCSA","NFLX","ADBE","CSCO","PEP","AVGO","TXN","PDD","TMUS","BABA","CSIQ", "XWD.TO", "EEM","HBLK.TO","BND","HTWO.MI"]
Names = ["APPLE","MICROSOFT","AMAZON","FACEBOOK","GOOGLE A","GOOGLE C","TESLA","NVIDIA","PAYPAL","ASML HOLDINGS","INTEL","COMCAST","NETFLIX","ADOBE","CISCO","PEPSI","BROADCOM","TEXAS INSTRUMENTS","PINDUODO","T-MOBILE US","ALIBABA","CANADIAN SOLAR", "ETF WORLD", "ETF EMERGENTI","ETF BLOCKCHAIN", "ETF BOND","ETF IDROGENO"]
#TITLE OF THE WEB APP
st.write("""
# Portfolio App
This app returns the average P/E of your Portfolio!
""")

st.sidebar.header('Build your Portfolio')

#SIDEBAR OF THE WEB APP. THIS TAKES THE INPUT OF THE USER(ETF AND WEIGHTS)
First_etf = st.sidebar.selectbox(
    'Select a stock',
    (Names)
)

First_etf_money = st.sidebar.slider(First_etf, 0, 5000, 1)


Second_etf = st.sidebar.selectbox(
    'Select a stock',
    (Names[1:])
)
Second_etf_money = st.sidebar.slider(Second_etf, 0, 5000, 0)

Third_etf = st.sidebar.selectbox(
    'Select a stock',
    Names[2:]
)
Third_etf_money = st.sidebar.slider(Third_etf, 0, 5000, 0)

Fourth_etf = st.sidebar.selectbox(
    'Select a stock',
    Names[3:]
    )

Fourth_etf_money = st.sidebar.slider(Fourth_etf, 0, 5000, 0)

Fifth_etf = st.sidebar.selectbox(
    'Select a stock',
    Names[4:]
    )

Fifth_etf_money = st.sidebar.slider(Fifth_etf, 0, 5000, 0)

Sixth_etf = st.sidebar.selectbox(
    'Select a stock',
    Names[5:]
    )

Sixth_etf_money = st.sidebar.slider(Sixth_etf, 0, 5000, 0)

Seventh_etf = st.sidebar.selectbox(
    'Select a stock',
    Names[6:]
    )

Seventh_etf_money = st.sidebar.slider(Seventh_etf, 0, 5000, 0)

Eight_etf = st.sidebar.selectbox(
    'Select a stock',
    Names[7:]
    )

Eight_etf_money = st.sidebar.slider(Eight_etf, 0, 5000, 0)

Ninth_etf = st.sidebar.selectbox(
    'Select a stock',
    Names[8:]
    )

Ninth_etf_money = st.sidebar.slider(Ninth_etf, 0, 5000, 0)

Tenth_etf = st.sidebar.selectbox(
    'Select a stock',
    Names[9:]
    )

Tenth_etf_money = st.sidebar.slider(Tenth_etf, 0, 5000, 0)


Total_portfolio = First_etf_money+Second_etf_money+Third_etf_money+Fourth_etf_money+Fifth_etf_money+Sixth_etf_money+Seventh_etf_money+Eight_etf_money+Ninth_etf_money+Tenth_etf_money
First_weight = First_etf_money/Total_portfolio*100
Second_weight = Second_etf_money/Total_portfolio*100
Third_weight = Third_etf_money/Total_portfolio*100
Fourth_weight = Fourth_etf_money/Total_portfolio*100
Fifth_weight = Fifth_etf_money/Total_portfolio*100
Sixth_weight = Sixth_etf_money/Total_portfolio*100
Seventh_weight = Seventh_etf_money/Total_portfolio*100
Eight_weight = Eight_etf_money/Total_portfolio*100
Ninth_weight = Ninth_etf_money/Total_portfolio*100
Tenth_weight = Tenth_etf_money/Total_portfolio*100

res = {}
for key in Names:
    for value in Symbol:
        res[key] = value
        Symbol.remove(value)
        break

Portfolio = [First_etf,Second_etf,Third_etf,Fourth_etf,Fifth_etf,Sixth_etf,Seventh_etf,Eight_etf,Ninth_etf,Tenth_etf]


sizes = [First_weight,Second_weight,Third_weight,Fourth_weight,Fifth_weight,Sixth_weight,Seventh_weight,Eight_weight,Ninth_weight,Tenth_weight]


fig = plt.figure(figsize =(10, 7))
plt.pie(sizes, labels = Portfolio)
st.pyplot(fig)





A1 = yf.Ticker(res[First_etf])
PE1 = (A1.info['trailingPE'])

A2 = yf.Ticker(res[Second_etf])
PE2 = (A2.info['trailingPE'])

A3 = yf.Ticker(res[Third_etf])
PE3 = (A3.info['trailingPE'])

A4 = yf.Ticker(res[Fourth_etf])
PE4 = (A4.info['trailingPE'])

A5 = yf.Ticker(res[Fifth_etf])
PE5 = (A5.info['trailingPE'])

A6 = yf.Ticker(res[Sixth_etf])
PE6 = (A6.info['trailingPE'])

A7 = yf.Ticker(res[Seventh_etf])
PE7 = (A7.info['trailingPE'])

A8 = yf.Ticker(res[Eight_etf])
PE8 = (A8.info['trailingPE'])

A9 = yf.Ticker(res[Ninth_etf])
PE9 = (A9.info['trailingPE'])

A10 = yf.Ticker(res[Tenth_etf])
PE10 = (A10.info['trailingPE'])


Average_PE = (PE1 * First_weight/100) +(PE2*Second_weight/100) +(PE3 * Third_weight/100) + (PE4*Fourth_weight/100) +(PE5*Fifth_weight/100) + (PE6*Sixth_weight/100) + (PE7*Seventh_weight/100) + (PE8*Eight_weight/100) + (PE9*Ninth_weight/100) + (PE10*Tenth_weight/100)

st.write("Your average P/E is " + str(Average_PE))
st.write("The P/E of the SP500 is 15.98 ")

st.write(PE1,PE2,PE3,PE4,PE5,PE6,PE7,PE8,PE9,PE10)



