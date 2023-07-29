from langchain.tools import BaseTool
from langchain.agents import AgentType
from typing import Optional, Type
from pydantic import BaseModel, Field
from yf_tool import get_stock_price, calculate_performance, get_price_change_percent, get_best_performing


class StockPriceCheckInput(BaseModel):
    """Input for Stock price check."""

    stockticker: str = Field(...,
                             description="Ticker symbol for stock or index")


class StockPriceTool(BaseTool):
    name = "get_stock_ticker_price"
    description = "Useful for when you need to find out the price of stock. You should input the stock ticker used on the yfinance API"

    def _run(self, stockticker: str):
        print("\n\n\n正在查詢 " + stockticker + " 的股價...")
        price_response = get_stock_price(stockticker)
        print("\n" + stockticker + " 的股價是 " + str(price_response) + " 元")

        return price_response

    def _arun(self, stockticker: str):
        raise NotImplementedError("This tool does not support async")

    args_schema: Optional[Type[BaseModel]] = StockPriceCheckInput
