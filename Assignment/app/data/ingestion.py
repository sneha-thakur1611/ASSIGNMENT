# app/data/ingestion.py

import yfinance as yf
from typing import Dict, List, Any
import datetime

# Static list of assets to track
tracked_assets = ["BTC-USD", "ETH-USD", "TSLA"]

async def fetch_asset_data(symbol: str) -> Dict[str, Any]:
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="7d", interval="1h")  # last 7 days hourly

        if hist.empty:
            raise ValueError("No data available for symbol")

        latest_price = hist["Close"].iloc[-1]
        change_24h = ((hist["Close"].iloc[-1] - hist["Close"].iloc[-25]) / hist["Close"].iloc[-25]) * 100
        average_7d = hist["Close"].mean()

        return {
            "symbol": symbol,
            "latest_price": round(latest_price, 2),
            "change_percent_24h": round(change_24h, 2),
            "average_price_7d": round(average_7d, 2)
        }

    except Exception as e:
        return {"error": str(e), "symbol": symbol}

# Fetch all assets' data
async def fetch_all_assets() -> List[Dict[str, Any]]:
    return [await fetch_asset_data(symbol) for symbol in tracked_assets]
