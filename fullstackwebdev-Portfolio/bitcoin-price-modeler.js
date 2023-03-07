// Load the CoinGecko API library
const CoinGecko = require('coingecko-api');
const cgClient = new CoinGecko();

// Define the linear regression function
function linearRegression(x, y) {
  const n = x.length;
  let sumX = 0, sumY = 0, sumXY = 0, sumXX = 0, sumYY = 0;
  for (let i = 0; i < n; i++) {
    sumX += x[i];
    sumY += y[i];
    sumXY += x[i] * y[i];
    sumXX += x[i] * x[i];
    sumYY += y[i] * y[i];
  }
  const slope = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX);
  const intercept = (sumY - slope * sumX) / n;
  const r = (n * sumXY - sumX * sumY) / Math.sqrt((n * sumXX - sumX * sumX) * (n * sumYY - sumY * sumY));
  return { slope, intercept, r };
}

// Get the input date from the form
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const date = e.target.elements["date-input"].value;
  const unixDate = Math.floor(new Date(date).getTime() / 1000);

  // Fetch Bitcoin price and active user addresses from the CoinGecko API
  Promise.all([
    cgClient.coins.fetch('bitcoin', { tickers: false, market_data: true, community_data: true, developer_data: true }),
    cgClient.coins.fetchMarketChart('bitcoin', { vs_currency: 'usd', days: 365 })
  ]).then(([coinInfo, marketChart]) => {
    const prices = marketChart.prices;
    const activeAddresses = coinInfo.data.community_data.active_users;

    // Convert marketChart data to arrays for linear regression
    const x = [], y = [];
    for (let i = 0; i < prices.length; i++) {
      const price = prices[i][1];
      const timestamp = prices[i][0] / 1000;
      if (timestamp <= unixDate) {
        x.push(activeAddresses[i]);
        y.push(price);
      }
    }

    // Calculate the linear regression and predict the Bitcoin price
    const regression = linearRegression(x, y);
    const predictedPrice = regression.intercept + regression.slope * activeAddresses[activeAddresses.length - 1];
    const predictionResult = `Bitcoin price will be $${predictedPrice.toFixed(2)} on ${date}`;
    result.textContent = predictionResult;
  }).catch((err) => {
    console.error(err);
    result.textContent = "Error: Could not fetch Bitcoin data";
  });
});
