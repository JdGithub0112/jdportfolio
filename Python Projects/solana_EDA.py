import requests
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Define the endpoints and headers
solana_users_endpoint = "https://api.solana.fm/v0/stats/active-users"
coingecko_endpoint = "https://api.coingecko.com/api/v3/coins/solana/market_chart/range"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Fetch data from January 1, 2022 to today
end_date = datetime.now()
start_date = datetime(2022, 1, 1)

dates = []
dau_counts = []
prices = []

# Fetch Solana's historical price data from CoinGecko
response_price = requests.get(coingecko_endpoint, params={
    "vs_currency": "usd",
    "from": int(start_date.timestamp()),
    "to": int(end_date.timestamp())
}, headers=headers)
data_price = response_price.json()
for item in data_price['prices']:
    date_obj = datetime.utcfromtimestamp(item[0] / 1000)
    dates.append(date_obj.strftime('%Y-%m-%d'))
    prices.append(item[1])

# Fetch DAU data for the same dates
for date_str in dates:
    response_dau = requests.get(f"{solana_users_endpoint}?date={datetime.strptime(date_str, '%Y-%m-%d').strftime('%d-%m-%Y')}", headers=headers)
    data_dau = response_dau.json()
    if data_dau['status'] == 'Success':
        dau_counts.append(data_dau['result']['activeUsers'])

# Calculate 7-day moving average
moving_avg = [sum(dau_counts[max(0, i-6):i+1])/len(dau_counts[max(0, i-6):i+1]) for i in range(len(dau_counts))]

# Plotting the Data using Plotly

# Create the plot
fig = go.Figure()

# Add moving average to the plot
fig.add_trace(go.Scatter(x=dates, y=moving_avg, mode='lines', name='7-Day Moving Average', line=dict(color='purple')))

# Add Solana price to the plot
fig.add_trace(go.Scatter(x=dates, y=prices, mode='lines', name='Solana Price', line=dict(color='teal'), yaxis='y2'))

# Set the title, labels, and secondary y-axis for price
fig.update_layout(title='Solana Daily Active User Count (7DMA) & Price - 2022 to Present',
                  xaxis_title='Date',
                  yaxis_title='DAU Count',
                  yaxis2=dict(title='Price (USD)', overlaying='y', side='right'))

# Show the plot
fig.show()
