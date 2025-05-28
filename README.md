# KuCoin Trading Bot on Render

This is a simple KuCoin bot deployed as a background worker using Python on [Render.com](https://render.com).

## ✅ Setup

1. Fork or clone this repo
2. Push it to your GitHub account
3. Go to https://render.com and create a new "Background Worker"
4. Connect your GitHub repo
5. Set the environment variables:
   - `KUCOIN_API_KEY`
   - `KUCOIN_API_SECRET`
   - `KUCOIN_API_PASSPHRASE`

## 🛠 Modify `main.py` to implement your strategy

Right now, it just prints the account balances every minute.
