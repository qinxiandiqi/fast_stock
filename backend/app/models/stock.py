from typing import Optional
from sqlmodel import SQLModel, Field

from enum import Enum

class SecurityType(Enum):
    STOCK = "Stock"  # 股票
    BOND = "Bond"  # 债券
    FUTURE = "Future"  # 期货合约
    OPTION = "Option"  # 期权合约
    ETF = "ETF"  # 交易所交易基金
    MUTUAL_FUND = "Mutual Fund"  # 共同基金
    FOREIGN_EXCHANGE = "Foreign Exchange"  # 外汇
    COMMODITY = "Commodity"  # 商品


class TradingProduct(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(index=True)  # 交易品类代码
    name: str  # 交易品类名称
    security_type: SecurityType  # 证券类型
    exchange: str  # 交易所