#!/usr/bin/env python
# coding: utf-8

# # Quantitative Analysis of Stock Market

# In[6]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.templates.default = "plotly_white"


# In[7]:


df=pd.read_csv('stocks.csv')


# In[8]:


df


# In[9]:


# Display the first few rows of the dataset
df.head()


# The dataset contains the following columns for stock market data:
# 
# Ticker: The stock ticker symbol.
# 
# Date: The trading date.
# 
# Open: The opening price of the stock for the day.
# 
# High: The highest price of the stock during the day.
# 
# Low: The lowest price of the stock during the day.
# 
# Close: The closing price of the stock for the day.
# 
# Adj Close: The adjusted closing price, which accounts for all corporate actions such as dividends, stock splits, etc.
# 
# Volume: The number of shares traded during the day.
# 

# # Descriptive Statistics
# 

# Descriptive Statistics will provide summary statistics for each stock in the dataset. We’ll look at measures such as mean, median, standard deviation, and more for the Close prices:
# 
# 

# In[11]:


# Descriptive Statistics for each stock
ds_stats =df.groupby('Ticker')['Close'].describe()
print(ds_stats)

Let’s break down the results for each stock:

AAPL (Apple Inc.)
Count: 62.0 (The number of observations or trading days included in the dataset for AAPL)
Mean: 158.24 (The average closing price)
Standard Deviation: 7.36 (Measures the amount of variation or dispersion of closing prices)
Minimum: 145.31 (The lowest closing price in the dataset)
25th Percentile: 152.08 (25% of the closing prices are below this value)
Median (50%): 158.06 (The middle value of the closing prices)
75th Percentile: 165.16 (75% of the closing prices are below this value)
Maximum: 173.57 (The highest closing price in the dataset)

# # Time Series Analysis
# 

# Next, we’ll proceed with the Time Series Analysis to examine trends and patterns over time, focusing on the closing prices:
# 
# 

# In[18]:


#time Series Analysis
df['Date']= pd.to_datetime(df['Date'])
pivot_data =df.pivot(index='Date',columns='Ticker',values='Close')


#Create a Subplot
fig = make_subplots(rows=1,cols=1)

#Add trace for each stocks ticker
for column in pivot_data.columns:
    fig.add_trace(
        go.Scatter(x=pivot_data.index, y=pivot_data[column],name=column),
        row=1,col=1
    )
    
    
fig.update_layout(
    title_text='Time Series for CLosing Prices',
    xaxis_title='Date',
    yaxis_title='Closing Price',
    legend_title='Ticker',  # Corrected property name
    showlegend=True
)


#Show the plot
fig.show()


# # Volatility Analysis
# Next, let’s focus on Volatility Analysis. We’ll calculate and compare the volatility (standard deviation) of the closing prices for each stock. It will give us an insight into how much the stock prices fluctuated over the period:

# In[22]:


#Volatility Analysis
volatility =pivot_data.std().sort_values(ascending=False)

fig = px.bar(volatility,
          x= volatility.index,
          y=volatility.values,
          labels={'y':'Standard Deviation','x':'Ticker'},
          title ='Volatility of CLosing Prices (Standard Deviations)')

#Show the Figure
fig.show()


# The bar chart and the accompanying data show the volatility (measured as standard deviation) of the closing prices for each stock. Here’s how they rank in terms of volatility:
# 
# 

# # Correlation Analysis
# Next, we’ll perform a Correlation Analysis to understand how the stock prices of these companies are related to each other:
# 
# 

# In[23]:


#Correlation Analysis
correlation_matrix =pivot_data.corr()

fig = go.Figure(data=go.Heatmap(
                    z=correlation_matrix,
                    x=correlation_matrix.columns,
                    y=correlation_matrix.columns,
                    colorscale='blues',
                    colorbar=dict(title='Correlation'),
))


# In[24]:


#Update Layout
fig.update_layout(
    title='Correlation Matrix of CLosing Prices',
    xaxis_title='Ticker',
    yaxis_title='Ticker'

)

#Show the Figure

fig.show()


# # Comparative Analysis
# Now, let’s move on to Comparative Analysis. In this step, we’ll compare the performance of different stocks based on their returns over the period. We’ll calculate the percentage change in closing prices from the start to the end of the period for each stock:

# In[25]:


# Calculating the percentage change in closing prices
percentage_change =((pivot_data.iloc[-1]-pivot_data.iloc[0])/pivot_data.iloc[0] *100)


# In[26]:


#Figure 

fig= px.bar(percentage_change,
            x=percentage_change.index,
            y=percentage_change.index,
            labels={'y':'Percentage Change(%)', 'x':'Ticker'},
            title ='Percentage Change in Closing Prices')

#Show figure
fig.show()


# # Daily Risk Vs. Return Analysis
# To perform a Risk vs. Return Analysis, we will calculate the average daily return and the standard deviation of daily returns for each stock. The standard deviation will serve as a proxy for risk, while the average daily return represents the expected return.
# 
# We will then plot these values to visually assess the risk-return profile of each stock. Stocks with higher average returns and lower risk (standard deviation) are generally more desirable, but investment decisions often depend on the investor’s risk tolerance:
# 
# 

# In[29]:


daily_returns =pivot_data.pct_change().dropna()

#Recalculating average daily returns and Standard Deviation(risk)
avg_daily_return =daily_returns.mean()
risk= daily_returns.std()


#Creating a Dataframe for ploting

risk_retuns_df=pd.DataFrame({'Risk':risk, 'Average Daily Return':avg_daily_return})


fig= go.Figure()



#Add scatter plot points
fig.add_trace(go.Scatter(
    x=risk_retuns_df['Risk'],
    y=risk_retuns_df['Average Daily Return'],
    mode='markers+text',
    text=risk_retuns_df.index,
    textposition="top center",
    marker =dict(size=10)
    
))


# show figure 

fig.show()


# So, AAPL shows the lowest risk combined with a positive average daily return, suggesting a more stable investment with consistent returns. GOOG has higher volatility than AAPL and, on average, a slightly negative daily return, indicating a riskier and less rewarding investment during this period.
# 
# 

# # Summary
# So, this is how you can perform a Quantitative Analysis of the Stock Market using Python. Quantitative Analysis in the stock market is a financial methodology that utilizes mathematical and statistical techniques to analyze stocks and financial markets. I hope you liked this article on Quantitative Analysis of Stock Market using Python. Feel free to ask valuable questions in the comments section below.
# 
# 

# In[ ]:




