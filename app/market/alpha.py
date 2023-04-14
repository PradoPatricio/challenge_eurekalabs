import decimal

import requests


def get_market_data(symbol="META"):
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "outputsize": "compact",
        "apikey": "X86NOH6II01P7R24",
    }
    resp = requests.get("https://www.alphavantage.co/query", params=params)
    meta_data = resp.json().get("Meta Data")
    data = resp.json().get("Time Series (Daily)")
    dates = list(data)[:2]
    payload = {
        "symbol": meta_data.get("2. Symbol"),
        "open": data.get(dates[0]).get("1. open"),
        "higher": data.get(dates[0]).get("2. high"),
        "lower": data.get(dates[0]).get("3. low"),
        "variation": str(
            (
                decimal.Decimal(data.get(dates[0]).get("4. close"))
                - decimal.Decimal(data.get(dates[1]).get("4. close"))
            )
        ),
    }
    return payload
