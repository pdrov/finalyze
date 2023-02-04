import pandas as pd

CSV_FILE = pd.read_csv("nasdaq_screener.csv", sep=',')
DF = pd.DataFrame(data=CSV_FILE)
DF = DF.drop(["Last Sale", "Net Change", "% Change", "Market Cap", "Volume"], axis=1)
DF = DF.fillna(value="NaN")


def get_all_symbols():
    return DF['Symbol']


def get_all_names():
    return DF['Name']


def get_all_countries():
    return DF['Country']


def get_all_ipo_years():
    return DF['IPO Year']


def get_all_sectors():
    return DF['Sector']


def get_all_industries():
    return DF['Industry']


def filter_by_industry(industry):
    return [DF['Symbol'][i] for i in DF.index if industry in DF["Industry"][i]]


def get_symbol_info(symbol):
    for i in DF.index:
        if symbol == DF["Symbol"][i]:
            idx = i
            return DF.loc[i] # Symbol, Name, Country, IPO Year, Sector, Industry
    return "Symbol was entered incorrectly or does not exist."


print(filter_by_industry("Biotech"))