#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[4]:


data =pd.read_csv("DailyDelhiClimateTrain.csv")


# In[5]:


data


# Let’s have a look at the descriptive statistics of this data before moving forward:
# 
# 

# In[7]:


data.describe()


# Now let’s have a look at the information about all the columns in the dataset:
# 
# 

# In[8]:


data.info()


# The date column in this dataset is not having a datetime data type. We will change it when required. Let’s have a look at the mean temperature in Delhi over the years:
# 
# 

# In[10]:


figure =px.line(data, x="date",
               y= "meantemp",
               title="Mean  Temprature in the Delhi Over the Years")
figure.show()


# Now let’s have a look at the humidity in Delhi over the years:
# 
# 

# In[12]:


figure =px.line(data, x= 'date',
               y= 'humidity',
               title ="Humidity in  Delhi Over the Years")
figure.show()


# Now let’s have a look at the wind speed in Delhi over the years:
# 
# 

# In[13]:


figure = px.line(data, x='date',
                y= 'wind_speed',
                title = "Wind Speed in Delhi Over Years")
figure.show()


# Till 2015, the wind speed was higher during monsoons (August & September) and retreating monsoons (December & January). After 2015, there were no anomalies in wind speed during monsoons. Now let’s have a look at the relationship between temperature and humidity:
# 
# 

# In[14]:


figure =px.scatter(data_frame =data, x='humidity',
                  y='meantemp',size ='meantemp',
                  trendline ='ols',
                  title ="Relationship between Temprature and Humidity")
figure.show()


# # Analyzing Temprature Change

# Now let’s analyze the temperature change in Delhi over the years. For this task, I will first convert the data type of the date column into datetime. Then I will add two new columns in the dataset for year and month values.
# 
# 
Here’s how we can change the data type and extract year and month data from the date column:


# In[17]:


data['date']= pd.to_datetime(data["date"],format = '%Y-%m-%d')
data['Year']=data['date'].dt.year
data['month'] =data["date"].dt.month
print(data)


# In[18]:


data.head()


# Now let’s have a look at the temperature change in Delhi over the years:
# 
# 

# In[26]:


import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
plt.figure(figsize=(15,10))
plt.title("Temprature Change in Delhi over the Years")
sns.lineplot(data = data, x ='month', y="meantemp",  hue='Year')
plt.show()


# Although 2017 was not the hottest year in the summer, we can see a rise in the average temperature of Delhi every year.

# # Forecasting Weather 

# Now let’s move to the task of weather forecasting. I will be using the Facebook prophet model for this task. The Facebook prophet model is one of the best techniques for time series forecasting. If you have never used this model before, you can install it on your system by using the command mentioned below in your command prompt or terminal:
# 
# 

# In[27]:


get_ipython().system('pip install prophet')


# The prophet model accepts time data named as “ds”, and labels as “y”. So let’s convert the data into this format:
# 
# 

# In[32]:


forecast_data =data.rename(columns ={'date':'ds',
                                   'meantemp':'y'})
print(forecast_data)


# In[33]:


forecast_data.head()


# Now below is how we can use the Facebook prophet model for weather forecasting using Python:
# 
# 

# In[34]:


import prophet


# In[36]:


from prophet import Prophet
from prophet.plot import plot_plotly,plot_components_plotly


# In[39]:


model = Prophet()
model.fit(forecast_data)
forecasts = model.make_future_dataframe(periods =365)
predictions =model.predict(forecasts)
plot_plotly (model,predictions)


# So this is how you can analyze and forecast the weather using Python.
# 
# 

# In[ ]:




