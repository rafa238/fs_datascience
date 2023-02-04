# -*- coding: utf-8 -*-
"""
NamedTuples and DataClasses
"""

from collections import namedtuple

StockPrice = namedtuple('StockPrice', ['symbol', 'closing_price'])
price = StockPrice('MSFT', 106.3)

print(price.symbol)

"""
Another better option is a class
"""

from typing import NamedTuple

class StockPrice(NamedTuple):
    symbol: str
    closing_price: float
    
    def is_high_tech(self) -> bool:
        return self.symbol in ['MSFT', 'GOOG', 'FB', 'AMZN', 'APPL']
    

price = StockPrice('MSFT', 186.3)

"""
DataClasses is a similar option like namedtuple, but in this case we can
modify the attributes
"""

from dataclasses import dataclass

@dataclass
class StockPrice:
    symbol: str
    closing_price: float 
    
    def is_high_tech(self) -> bool:
        return self.symbol in ['MSFT', 'GOOG', 'FB', 'AMZN', 'APPL']
    
price = StockPrice('MSFT', 186.3)
"""
data classes give us an incovenient, we can undeseable add attributes,
named tuples doesn't have this inconvenient
price.cosing_price = 10
print(price.cosing_price)
"""
print(price.closing_price)