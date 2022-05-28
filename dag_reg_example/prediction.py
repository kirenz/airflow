"""
    Make prediction

Step 1) Import model 
Step 2) Create new data
Step 3) Make prediction
Step 4) Store prediction

"""
#------------------------------------------------------
# Setup
import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import load

#------------------------------------------------------
# Step 1) Import model 
reg = load('my_linear_model.joblib')

#------------------------------------------------------
# Step 2) Make new data

# Create a new GDP value
X_new = pd.DataFrame({"gdp_per_capita": [50000]})

#------------------------------------------------------
# Step 3) Make prediction

# Make prediction
my_prediction = reg.predict(X_new)

#------------------------------------------------------
# Step 4) Save prediction

# Save prediction as dataframe 
df_prediction = pd.Dataframe({"pred": my_prediction})

# Store predictions as csv
df.prediction.to_csv("my_prediction.csv")

#------------------------------------------------------
