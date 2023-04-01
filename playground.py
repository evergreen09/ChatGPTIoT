import ccxt
import pandas as pd
import datetime
import os

BITGET_API_KEY = 'your_api_key'
BITGET_SECRET_KEY = 'your_secret_key'

def get_balance() -> dict:
    bitget = ccxt.bitget({
        'apiKey': BITGET_API_KEY,
        'secret': BITGET_SECRET_KEY,
    })

    balance = bitget.fetch_balance()
    return balance['total']

def log_trade_journal(initial_balance: float, daily_balance: float, profit_dollars: float, profit_percentage: float, withdrawal: float):
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    trade_journal = pd.DataFrame(columns=['Date', 'Initial Balance', 'Daily Balance', 'Profit ($)', 'Profit (%)', 'Withdrawal'])

    if not os.path.exists('trade_journal.csv'):
        trade_journal.to_csv('trade_journal.csv', index=False)

    new_entry = pd.DataFrame([[today, initial_balance, daily_balance, profit_dollars, profit_percentage, withdrawal]],
                             columns=['Date', 'Initial Balance', 'Daily Balance', 'Profit ($)', 'Profit (%)', 'Withdrawal'])

    trade_journal = pd.read_csv('trade_journal.csv')
    trade_journal = trade_journal.append(new_entry, ignore_index=True)
    trade_journal.to_csv('trade_journal.csv', index=False)
    print("New entry added to the trade journal.")

if __name__ == '__main__':
    # Retrieve initial balance from Bitget API
    balance_data = get_balance()
    initial_balance = balance_data.get("USDT", 0)

    # Set these values based on your trading information
    daily_balance = 1050  # Replace with your daily balance after trading
    profit_dollars = 50   # Replace with your profit in dollars
    profit_percentage = 5 # Replace with your profit in percentage
    withdrawal = 0        # Replace with your withdrawal amount

    log_trade_journal(initial_balance, daily_balance, profit_dollars, profit_percentage, withdrawal)
