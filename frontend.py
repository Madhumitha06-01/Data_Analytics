import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
data =pd.read_excel("vissco.xlsx")
plt .figure(figsize=(10,6))
sns.histplot(data['MRP'].dropna(), kde =True, bins=20, color ='skyblue')
plt.title("Products_Data")
plt.xlabel("MRP")
plt.ylabel("Total")
plt.show()
plt.figure(figsize=(10,6))
sns.countplot(y='ITEMNAME', data=data, order=data['ITEMNAME'].value_counts().index, hue='ITEMNAME', palette='viridis', legend=False)
plt.title('Products details')
plt.xlabel('count')
plt.ylabel('Itemname')
# show plot @
plt.show()
