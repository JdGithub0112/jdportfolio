import requests
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

# Step 1: Web Scraping Solana and Cardano Daily Active User Count from CoinGecko

# Define the endpoint for Solana DAU count data
solana_dau_endpoint = "https://api.coingecko.com/api/v3/coins/solana/market_chart"
cardano_dau_endpoint = "https://api.coingecko.com/api/v3/coins/cardano/market_chart"

# Calculate the timestamps for the date range
end_date = int(datetime.now().timestamp())
start_date = int((datetime.now() - timedelta(days=365 * 2)).timestamp())

# Set the parameters for the API requests
params = {
    "vs_currency": "usd",
    "from": start_date,
    "to": end_date,
    "days": "730"  # You can adjust the number of days as needed for your historical data range.
}

# Fetch DAU count data for Solana
solana_dau_response = requests.get(solana_dau_endpoint, params=params)

# Fetch DAU count data for Cardano
cardano_dau_response = requests.get(cardano_dau_endpoint, params=params)

# Check if both responses are successful
if solana_dau_response.status_code == 200 and cardano_dau_response.status_code == 200:
    solana_dau_data = solana_dau_response.json()
    cardano_dau_data = cardano_dau_response.json()

    # Extract dates and DAU counts for Solana
    solana_dau_timestamps = [timestamp for timestamp, _ in solana_dau_data['prices']]
    solana_dau_dates = [datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d') for timestamp in solana_dau_timestamps]
    solana_dau_counts = [count for _, count in solana_dau_data['market_caps']]

    # Extract dates and DAU counts for Cardano
    cardano_dau_timestamps = [timestamp for timestamp, _ in cardano_dau_data['prices']]
    cardano_dau_dates = [datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d') for timestamp in cardano_dau_timestamps]
    cardano_dau_counts = [count for _, count in cardano_dau_data['market_caps']]

    # Create a subplot with one Y-axis
    fig = make_subplots(specs=[[{"secondary_y": False}]])

    # Add the DAU count for Solana
    fig.add_trace(go.Scatter(x=solana_dau_dates, y=solana_dau_counts, name='Solana DAU Count', mode='lines'))

    # Add the DAU count for Cardano
    fig.add_trace(go.Scatter(x=cardano_dau_dates, y=cardano_dau_counts, name='Cardano DAU Count', mode='lines'))

    # Set the title and labels
    fig.update_layout(title='Cryptocurrency Daily Active User Counts',
                      xaxis_title='Date',
                      yaxis_title='DAU Count')

    # Show the plot
    fig.show()
else:
    print("Failed to fetch data. Status codes:", solana_dau_response.status_code, cardano_dau_response.status_code)
