#!/usr/bin/env python
# coding: utf-8

# # FUTURE SALES PREDICTION ANALYSIS 

# Let’s start the task of future sales prediction with machine learning by importing the necessary Python libraries and the dataset:
# 
# 

# In[1]:


import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[2]:


data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/advertising.csv")
data.head()


# Let’s have a look at whether this dataset contains any null values or not:
# 
# 

# In[3]:


data.isnull().sum()


# So this dataset doesn’t have any null values. Now let’s visualize the relationship between the amount spent on advertising on TV and units sold:
# 
# 

# In[4]:


import plotly
import plotly.express as px
import plotly.graph_objects as go
figure =px.scatter(data_frame = data, x="Sales",
                  y= "TV",trendline ="ols")
figure.show()


# Now let’s visualize the relationship between the amount spent on advertising on newspapers and units sold:
# 
# 

# In[5]:


figure = px.scatter(data_frame= data, x="Sales",
                   y= "Newspaper", size = "Newspaper", trendline ='ols')
figure.show()


# Out of all the amount spent on advertising on various platforms, I can see that the amount spent on advertising the product on TV results in more sales of the product. Now let’s have a look at the correlation of all the columns with the sales column:
# 
# 

# In[6]:


correlation = data.corr()
print(correlation['Sales'].sort_values(ascending = False))


# # Future Sales Prediction Model
# 

# Now in this section, I will train a machine learning model to predict the future sales of a product. But before I train the model, let’s split the data into training and test sets:
# 
# 

# In[13]:


x=np.array(data.drop(["Sales"],axis=1))
y= np.array(data['Sales'])
xtrain,xtest,ytrain,ytest = train_test_split(x,y,
                                            test_size = 0.2,
                                            random_state =42)


# Now let’s train the model to predict future sales:
# 
# 

# In[15]:


model = LinearRegression()
model.fit(xtrain, ytrain)
print(model.score(xtest,ytest))


# In[16]:


# feature =[[TV,radio,Newspaper]]
features =np.array([[230.1,37.8,69.2]])
print(model.predict(features))


# In[ ]:




