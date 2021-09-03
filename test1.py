import yfinance as yf
df = yf.download('TSLA', '2021-1-1')
print(df)