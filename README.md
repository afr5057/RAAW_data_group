# RAAW_data_group
Names: 
Vien Vo
Wilson Aliaga
Angel Alejandro
Amy Reynolds

Sources:
Yahoo Finance
FRED (Federal Reserve Economic Data)
 
1. Extraction
Type – Full Extraction, Partial Extraction w/ update notifications, Partial Extraction w/o update notifications
Stock Data – Yahoo Finance – API - library
Market Data – flat files downloaded from FRED.org

2. Transform
Raw Data placed into staging server
Clean
Yahoo file – need to add Ticker column. Keep column date, close price, keep volume. Drop the rest.
Market Data – normalize as needed
Map
Yahoo quarterly averages to market data by quarter
Transform
Yahoo - Group date by quarter, Get average price and volume

3. Load
Into mySQL database using at least 4 tables
Stock information
GDP
CPI
Unemployment

4. Questions to answer:
Do GDP, CPI, or Unemployment affect stock price?

