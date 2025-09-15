from pydantic import BaseModel
from datetime import datetime
from typing import List

class PriceResponse(BaseModel):
    symbol: str
    price: float
    currency: str
    timestamp: datetime

class Candle(BaseModel):
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

class NewsArticle(BaseModel):
    headline: str
    source: str
    url: str
    published_at: datetime
