from fastapi import FastAPI, HTTPException
from backend import providers
from backend.schemas import PriceResponse, Candle, NewsArticle
from typing import List

app = FastAPI(title="Bloomberg Lite API")

@app.get("/price/{symbol}", response_model=PriceResponse)
async def price(symbol: str):
    data = await providers.get_price(symbol)
    if not data:
        raise HTTPException(status_code=404, detail="Symbol not found")
    return data

@app.get("/chart/{symbol}", response_model=List[Candle])
async def chart(symbol: str, resolution: str = "D", count: int = 30):
    return await providers.get_candles(symbol, resolution, count)

@app.get("/news/{symbol}", response_model=List[NewsArticle])
async def news(symbol: str):
    return await providers.get_news(symbol)
