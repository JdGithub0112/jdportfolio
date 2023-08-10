#This python file is going to be leveraged to webscrape various metrics from the Solana blockchain. 

import requests
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Step 1: Web Scraping Solana Daily Active User Count

# Define the endpoint and headers
endpoint = "https://api.solana.fm/v0/stats/active-users"
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Fetch data for this year and last year
end_date = datetime.now()
start_date = end_date - timedelta(days=365*2)  # 2 years back

response = requests.get(endpoint, headers=headers)
data = response.json()

# Extracting dates and DAU count
dates = [item['date'] for item in data if start_date <= datetime.strptime(item['date'], '%Y-%m-%d') <= end_date]
dau_counts = [item['count'] for item in data if start_date <= datetime.strptime(item['date'], '%Y-%m-%d') <= end_date]

# Step 2: Plotting the Data using Plotly

# Create the plot
fig = go.Figure(data=go.Scatter(x=dates, y=dau_counts, mode='lines+markers'))

# Set the title and labels
fig.update_layout(title='Solana Daily Active User Count',
                  xaxis_title='Date',
                  yaxis_title='DAU Count')

# Show the plot
fig.show()
