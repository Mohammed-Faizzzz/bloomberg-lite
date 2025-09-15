import httpx
from datetime import datetime
from backend.schemas import PriceResponse, Candle, NewsArticle
import os
from dotenv import load_dotenv

load_dotenv()

FINNHUB_KEY = os.getenv("FINNHUB_API_KEY")
BASE_URL = "https://finnhub.io/api/v1"

async def get_price(symbol: str) -> PriceResponse | None:
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{BASE_URL}/quote",
                             params={"symbol": symbol, "token": FINNHUB_KEY})
        if r.status_code != 200:
            return None
        data = r.json()
        if "c" not in data or data["c"] == 0:
            return None
        return PriceResponse(
            symbol=symbol.upper(),
            price=data["c"],
            currency="USD",
            timestamp=datetime.utcfromtimestamp(data["t"])
        )

async def get_candles(symbol: str, resolution="D", count=30):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{BASE_URL}/stock/candle",
                             params={"symbol": symbol, "resolution": resolution,
                                     "count": count, "token": FINNHUB_KEY})
        if r.status_code != 200:
            return []
        data = r.json()
        candles = []
        for i, ts in enumerate(data.get("t", [])):
            candles.append(Candle(
                timestamp=datetime.utcfromtimestamp(ts),
                open=data["o"][i],
                high=data["h"][i],
                low=data["l"][i],
                close=data["c"][i],
                volume=data["v"][i],
            ))
        return candles

async def get_news(symbol: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{BASE_URL}/company-news",
                             params={"symbol": symbol, "from":"2025-09-01",
                                     "to":"2025-09-15","token":FINNHUB_KEY})
        if r.status_code != 200:
            return []
        articles = []
        for n in r.json():
            articles.append(NewsArticle(
                headline=n["headline"],
                source=n["source"],
                url=n["url"],
                published_at=datetime.utcfromtimestamp(n["datetime"])
            ))
        return articles
