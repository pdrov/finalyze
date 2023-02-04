import time
import polygon.exceptions
from polygon import RESTClient
from polygon.rest import models

import parse_desc
import screener_database

client = RESTClient()

symbols = screener_database.get_all_symbols()

"""
for symbol in symbols:
    try:
        news_summary = client.list_ticker_news(
            ticker=symbol,
            published_utc_gt="2023-01-23",
            raw=True,
        )
        
        
        
    except polygon.exceptions.BadResponse:
        with open(file="test.txt", mode='w') as f:
            f.write(news_summary.data.decode(encoding='UTF-8'))
        time.sleep(60)
        news_summary = client.list_ticker_news(
            ticker=symbol,
            published_utc_gt="2022-10-01",
            raw=True,
        )
"""

news_summary = client.list_ticker_news(
    ticker="AAPL",
    published_utc="2023-01-23",
    raw=True,
)
#print(news_summary.data.decode(encoding='UTF-8'))
parsed_data = parse_desc.parse(news_summary.data.decode('utf-8'))
print(parsed_data)


