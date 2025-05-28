import os
import time
from kucoin.client import Client

api_key = os.getenv("KUCOIN_API_KEY")
api_secret = os.getenv("KUCOIN_API_SECRET")
api_passphrase = os.getenv("KUCOIN_API_PASSPHRASE")

client = Client(api_key, api_secret, api_passphrase)

def print_balances():
    try:
        accounts = client.get_accounts()
        print("---- Account balances ----")
        for acc in accounts:
            if float(acc['balance']) > 0:
                print(f"{acc['currency']}: {acc['balance']} ({acc['type']})")
    except Exception as e:
        print(f"Error fetching balances: {e}")

if __name__ == "__main__":
    print("🚀 KuCoin bot started")
    while True:
        print_balances()
        time.sleep(60)
