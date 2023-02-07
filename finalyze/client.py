import time
import polygon.exceptions
from polygon import RESTClient
from polygon.rest import models
import os
import parse_desc
import screener_database
import datehandler as dh


class PolygonClient:

    def __init__(self):
        # self.client = RESTClient()
        # self.symbols = screener_database.get_all_symbols()
        self.resources_path = "./resources"
        self.news_file = "data_"

    def is_data_file_created(self):
        if self.news_file in os.listdir(self.resources_path):
            return True
        else:
            return False


    def get_news(self, n=5):
        days = dh.is_trading_day(n)
        for day in days:
            for symbol in self.symbols:
                news = self.client.list_ticker_news(
                    ticker=symbol,
                    published_utc=day,
                    raw=True,
                )
                parsed_news = parse_desc.parse(news.data.decode('utf-8'))


p = PolygonClient()
print(p.is_data_file_created())
