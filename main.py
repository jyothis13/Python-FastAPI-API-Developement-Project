from http.client import HTTPException
from typing import List, Optional
from fastapi import FastAPI
import datetime as dt
from database import Trade
import sys

app = FastAPI()

db: List[Trade] = [
    Trade(
        trade_id= "12sjdh",
        trader= "elon",
        instrument_id= "TSLA",
        instrument_name= 'TESLA MOTORS',
        asset_class= "Bond",
        counterparty= 'none',
        tradeDateTime= 644,
        price= 25,
        quantity= 15,
        buySellIndicator= "BUY" 
    ),
    Trade(
        trade_id= "kj2sj4",
        trader= "jeff",
        instrument_id= "AMZN",
        instrument_name= 'AMAZON',
        asset_class= "FX",
        counterparty= 'none',
        tradeDateTime= 806,
        price= 30,
        quantity= 10,
        buySellIndicator= "SELL" 
    ),
    Trade(
        trade_id= "26xhdk",
        trader= "bob smith",
        instrument_id= "BLO",
        instrument_name= 'BLUE ORIGIN',
        asset_class= "Share",
        counterparty= 'none',
        tradeDateTime= 360,
        price= 1,
        quantity= 10,
        buySellIndicator= "SELL" 
    ),
    Trade(
        trade_id= "4v5sfv",
        trader= "tim",
        instrument_id= "AAPL",
        instrument_name= 'APPLE',
        asset_class= "Equity",
        counterparty= 'none',
        tradeDateTime= 57,
        price= 10,
        quantity= 5,
        buySellIndicator= "BUY"

    ),
    Trade(
        trade_id= "9v3d8v",
        trader= "sundar",
        instrument_id= "GOOGL",
        instrument_name= 'ALBHABET',
        asset_class= "Share",
        counterparty= 'none',
        tradeDateTime= 125,
        price= 15,
        quantity= 8,
        buySellIndicator= "BUY"
        
    )
]

@app.get("/")
async def dashboard():
    return {
        'Dashboard':'GO TO localhost:8000/api/v1/trades to see the list of trades or localhost:8000/docs to perform fuctions'} 


@app.get("/api/v1/trades")
async def LIST_of_TRADES():
    return db; 

@app.get("/api/v1/trades/{trade_id}")
async def FETCH_TRADE_BY_ID(trade_id: str):
     for Trade in db:
        if Trade.trade_id == trade_id:
            return (Trade)

@app.get("/api/v1/trades/")
async def ADVANCED_SEARCH_USING_MULTIPLE_ENDPOINTS (counterparty: Optional [str] = None, instrument_id: Optional[str] = None, instrument_name: Optional[str] = None, trader: Optional[str] | None = None):
     for Trade in db:
        if Trade.counterparty == counterparty or Trade.instrument_id == instrument_id or Trade.instrument_name == instrument_name or Trade.trader == trader:
            return (Trade) 


@app.get("/api/v1/tradeS/")
async def Advanced_Filtering_using_ASSET_CLASS (asset_class:Optional[str] = None):
    Assets: List[Trade]=[]
    for Trade in db:
        if Trade.asset_class == asset_class:
            Assets.append(Trade)
    return Assets

@app.get("/api/v1/Trades/")
async def Advanced_filtering_using_tradeType(buySellIndicator: Optional[str] = None):
    Tradetype: List[Trade]=[]
    for Trade in db:
        if buySellIndicator == Trade.buySellIndicator:
            Tradetype.append(Trade)
    return Tradetype



@app.get("/api/v1/trAdes/")
async def Advanced_Filtering_using_Maximum_Price ():
    maxPrice=0
    for Trade in db:
        if Trade.price > maxPrice:
            maxPrice=Trade.price
            MaxP=Trade
    return MaxP


@app.get("/api/v1/tRAdes/")
async def Advanced_Filtering_using_Minimum_Price ():
    minPrice=sys.maxsize
    for Trade in db:
        if Trade.price < minPrice:
            minPrice=Trade.price
            MinP=Trade
    return MinP

@app.get("/api/v1/TraDeS/")
async def Advanced_Filtering_using_END ():
    temp=Trade(trade_id= "",
        trader= "",
        instrument_id= "",
        instrument_name= '',
        asset_class= "",
        counterparty= '',
        tradeDateTime= 0,
        price= 0,
        quantity= 0,
        buySellIndicator= "BUY")
    for x in db:
        if x.trade_date_time > temp.trade_date_time:
            temp=x
    return temp

@app.get("/api/v1/TraDEs/")
async def Advanced_Filtering_using_START ():
    temp=Trade(trade_id= "",
        trader= "",
        instrument_id= "",
        instrument_name= '',
        asset_class= "",
        counterparty= '',
        tradeDateTime= sys.maxsize,
        price= 0,
        quantity= 0,
        buySellIndicator= "BUY")
    for x in db:
        if x.trade_date_time < temp.trade_date_time:
            temp=x
    return temp
