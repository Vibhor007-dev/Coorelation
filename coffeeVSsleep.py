import pandas as pd
import numpy as np
import plotly_express as px

df = pd.read_csv("coffeeVSsleep.csv")
data1=df["Coffee in ml"].to_list()
data2=df["sleep in hours"].to_list()

graph=px.scatter(x=data1, y=data2) 
graph.show()
result=np.corrcoef(data1,data2)
print(result[0][1])