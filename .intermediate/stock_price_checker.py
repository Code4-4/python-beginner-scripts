# stock_price_checker.py
import requests

def get_stock_price(ticker):
    url = f"https://api.example.com/stocks/{ticker}"
    response = requests.get(url)
    data = response.json()
    
    if 'price' in data:
        return data['price']
    else:
        return None

if __name__ == "__main__":
    ticker = input("Enter stock ticker symbol: ")
    price = get_stock_price(ticker)
    if price:
        print(f"Current price of {ticker}: ${price}")
    else:
        print("Unable to fetch stock price.")
