from polygon import RESTClient
from polygon.rest import models

client = RESTClient()

news_summary = client.list_ticker_news(
    ticker="NVDA",
    published_utc_gt="2022-10-01",
    raw=True,
)

with open(file="test.txt", mode='w') as f:
    f.write(news_summary.data.decode(encoding='UTF-8'))
