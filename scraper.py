import requests
import pandas as pd
from datetime import datetime

# Official CoinGecko API URL
URL = "https://api.coingecko.com/api/v3/coins/markets"

# Request parameters
params = {
    "vs_currency": "usd",            # Currency for prices
    "order": "market_cap_desc",      # Sorted by market capitalization
    "per_page": 10,                  # Top 10 cryptocurrencies
    "page": 1,
    "sparkline": False
}

def get_crypto_prices():
    """Fetch cryptocurrency prices from the CoinGecko API."""
    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def run_scraper():
    """Run the scraper, save data to CSV, and return the file name."""
    data = get_crypto_prices()
    if data:
        df = pd.DataFrame(data)[["id", "symbol", "current_price", "market_cap", "total_volume"]]
        filename = f"data/crypto_prices_{datetime.now().date()}.csv"
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
        return filename
    else:
        print("No data retrieved.")
        return None

# Run scraper directly if executed as main script
if __name__ == "__main__":
    run_scraper()
