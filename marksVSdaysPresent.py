import pandas as pd
import numpy as np
import plotly_express as px

df = pd.read_csv("marksVSdaysPresent.csv")
data1=df["Marks In Percentage"].to_list()
data2=df["Days Present"].to_list()

graph=px.scatter(x=data1, y=data2) 
graph.show()
result=np.corrcoef(data1,data2)
print(result[0][1])