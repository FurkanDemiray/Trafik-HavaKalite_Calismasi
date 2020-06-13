import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sea
data = pd.read_excel('merged_full.xlsx')
print(data.isnull().sum())

print(data.mean())

data = data.fillna(data.mean())

plt.figure(figsize=(12,6))
plt.plot(data.Tarih,data.Trafik_Indeks)
plt.show()

plt.figure(figsize=(72,12))
plt.subplot(2,2,1)
plt.plot(data.Tarih,data.PM10,color="red")
plt.plot(data.Tarih,data.SO2,color="blue")
plt.plot(data.Tarih,data.NO2,color="black")
plt.plot(data.Tarih,data.NO,color="orange")
plt.plot(data.Tarih,data.O3,color="gray")
plt.plot(data.Tarih,data.NOX)
plt.plot(data.Tarih,data.CO)
plt.plot(data.Tarih,data.Trafik_Indeks)
plt.xlabel("Tarih")
plt.ylabel("Madde Miktarı")
plt.title("Zamana Göre Maddeler")
plt.show()

sea.scatterplot(x ="SO2",y="Trafik_Indeks", data=data)
plt.show()
sea.scatterplot(x ="O3",y="Trafik_Indeks", data=data)
plt.show()
sea.scatterplot(x ="NO",y="Trafik_Indeks", data=data,color="red")
plt.show()
sea.scatterplot(x ="NOX",y="Trafik_Indeks", data=data,color="yellow")
plt.show()
sea.scatterplot(x ="PM10",y="Trafik_Indeks", data=data,color="orange")
plt.show()
sea.scatterplot(x ="NO2",y="Trafik_Indeks", data=data,color="gray")
plt.show()
sea.scatterplot(x ="CO",y="Trafik_Indeks", data=data,color="black")
plt.show()


