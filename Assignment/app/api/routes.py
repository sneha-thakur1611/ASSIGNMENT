
from fastapi import APIRouter, HTTPException, Query
from app.data.ingestion import fetch_asset_data, fetch_all_assets
from app.data.summary1 import generate_mock_summary
from app.data.summary2 import generate_groq_summary
from app.manual.config import TRACKED_ASSETS 

router = APIRouter()

@router.get("/assets")
async def get_all_assets():
    assets_data = await fetch_all_assets()
    return {"assets": assets_data}


@router.get("/metrics/{symbol}")
async def get_asset_metrics(symbol: str):
    data = await fetch_asset_data(symbol.upper())
    if "error" in data:
        raise HTTPException(status_code=404, detail=data["error"])
    return data


@router.get("/compare")
async def compare_assets(asset1: str = Query(...), asset2: str = Query(...)):
    data1 = await fetch_asset_data(asset1.upper())
    data2 = await fetch_asset_data(asset2.upper())

    if "error" in data1:
        raise HTTPException(status_code=404, detail=f"{asset1}: {data1['error']}")
    if "error" in data2:
        raise HTTPException(status_code=404, detail=f"{asset2}: {data2['error']}")

    return {
        "asset1": data1,
        "asset2": data2
    }


@router.get("/summary1")
async def get_summary():
    summary = await generate_mock_summary()
    return {"summary": summary}


@router.get("/summary2")
async def get_summary():
    try:
        summary = await generate_groq_summary()
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}


@router.post("/ingest")
async def ingest_data():
     
    results = {}

    for symbol in TRACKED_ASSETS:
        data = await fetch_asset_data(symbol)
        results[symbol] = data

    return {
        "status": "success",
        "message": f"Ingested {len(results)} assets.",
        "data": results
    }
