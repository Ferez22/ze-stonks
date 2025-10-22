from fastapi import APIRouter
from twelvedata import TDClient
import os
from dotenv import load_dotenv

router = APIRouter(prefix="/api")
load_dotenv()

# Initialize client with your API key
td = TDClient(apikey=os.getenv("TWELVE_DATA_API_KEY"))

@router.get("/ping")
def ping():
    return {"status": "ok"}

@router.get("/stock/price")
def get_stock_price(symbol: str):
    price = td.price(symbol=symbol).as_json()
    return price