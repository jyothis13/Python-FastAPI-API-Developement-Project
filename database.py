from pydantic import BaseModel, Field
from typing import List, Optional
import datetime as dt


class Trade(BaseModel):
    trade_id: str
    trader: str
    instrument_id: Optional[str]
    instrument_name: Optional[str]
    asset_class: Optional[str]
    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")
    trade_date_time: dt.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")
    buySellIndicator: str
    price: float
    quantity: int  
    


    
