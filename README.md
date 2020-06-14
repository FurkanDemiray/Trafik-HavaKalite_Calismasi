# Trafik-Hava Kalitesi İlişkisi

Hava kirliliğine etki eden ölçütlere baktığımızda en fazla ağırlığı olan 3 başlık vardır. Bunlar; volkanik patlamalardan dolayı gerçekleşen hava kirliliği, trafik kaynaklı hava kirliliği ve sanayi alanlarının getirdiği hava kirliliği. Ülkemizde volkanik patlamaların hava kirliliğine etkisinin olmadığı düşünülerek bu iki başlık üzerinde yoğunlaştık.

Araştırmalar İstanbul için yapılacaktır. Hava kalitesini etkileyen faktörlerde denize yakınlık ve rüzgar gibi faktörler etki edeceği için İstanbul’da bir orta nokta merkez alınması gerektiğini düşünerek Başakşehir Hava İstasyonundan gelen veriler ile çalışılacaktır.

Özetle anlatmak gerekirse trafiğin getirdiği yabancı madde ölçümleri ile trafik yoğunluğu indeksi arasındaki temel bağıntıyı öğrenmeye yönelik bir çalışma amaçlanıyor.

##  Veriseti Hazırlığı

Kullanacağımız veriler Çevreve Şehircilik Bakanlığı ve İBB Veri Portalından alınmıştır.

> İBB Açık Veri [https://data.ibb.gov.tr/dataset/trafik-indeks-raporu](https://data.ibb.gov.tr/dataset/trafik-indeks-raporu)

> Çevreve Şehircilik Bakanlığı Hava İzleme [https://www.havaizleme.gov.tr/](https://www.havaizleme.gov.tr/)

Alınan bu iki veri seti tek bir veri setinde toplanarak düzenli ve ortak bir çalışma gerçekleştirmek amaçlanmıştır.

Verisetinin sütunları son şu şekilde oluşmuştur.

`Tarih` `PM10` `SO2` `CO` `NO2` `NOX` `NO` `O3` `Trafik_Indeks` 

Havadaki moleküller µg/m³ cinsinden verilmiştir.
`Trafik_Indeks` değeri ise saatlik bazda alınmış olup günlük ortalamaya çevrilmiştir. Bu sütun yüzdelik bazda verilmiştir.
Yaklaşık 1 yıllık bir veri seti ile çalışacağız.

![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/readme_images/dataset.PNG?raw=true)

## Hava Kalitesi İndeksi

Çalışacağımız alan için en önemli kavramlardan biriside hava kalitesi indeksidir. Hava kalitesinin kritik sınırlarını belirler.



![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/readme_images/aqi.jpg?raw=true)



Hava kalitesi indeksi ise aşağıdaki formül ile hesaplanır :



![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Report/calc.png)



Maddelerin sınırlarını ayrı ayrı görmek istersek tablo şu şekilde oluyor :  



![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Report/table.png)

##  Veriseti Max-Min Değerler

Verilerin analizi için max-min sınırlar bizlere karakteristik bazı özelliklerini gösterir. Bu sebeple max-min sınırlar aşağıdaki tabloda gösterilmiştir.

| Özellik       | Min                 | Min                 |
| :------------ |:-------------------:|:-------------------:|
| Tarih         | 2019-01-01 00:00:00 | 2020-02-04 00:00:00 |
| PM10          | 16.3583             | 163.483             |
| SO2           | 0.879167            | 14.275              |
| CO            | 162.229             | 2077.03             |
| NO2           | 49.5158             | 198.396             |
| NOX           | 57.1208             | 740.883             |
| NO            | 7.525               | 401.712             |
| O3            | 1.59167             | 65.6875             |
| Trafik_Indeks | 4.6993              | 44.4826             |


## Trafik - Zararlı Madde İlişkileri

Verinin özellikleri ile araştıralan değer arasındaki ilişki grafikler üzerinde daha net görülebilir. Bu yüzden özelliklerin zaman içerisindeki değişimini çizgi grafiğine aktardık. 

##### Grafik oluşturmak için kullanılan .py dosyası :　

```python
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
plt.xlabel("Tarih")
plt.ylabel("PM10-SO2-NO2-NO-O3 Miktarı")
plt.title("Zamana Göre PM10(Red)-SO2(Blue)-NO2(Black)-NO(Orange)-O3(Gray)")
plt.show()

sea.scatterplot(x ="SO2",y="Trafik_Indeks", data=data)
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
```

![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/All.png)

Grafiğe bakıldığında genellikle bir değer pick yaptığında diğer değerlerle birlikte artışa geçmiş. Bu da bizlere zararlı maddeler arasında bir bağlantı olduğu, aynı zamanda bir tetikleme(Trafik artışı, Sanayi aktivitesi) ile pick yaptığı düşünülebilir.


Trafik ve zararlı maddeler ilişkisini daha net görmek adına her maddeyi trafik oranıyla birlikte ele alalım. İki durum arasındaki ilişkiyi en net şekilde gösteren grafiklerden biriside korelasyon grafikleridir. 

![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/KolerasyonCO.png)
![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/KolerasyonNO.png)
![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/KolerasyonNO2.png)
![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/KolerasyonNOX.png)
![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/KolerasyonPM10.png)
![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/KolerasyonSO2.png)
![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/Korelasyon_O3.png)

Grafiklere bakıldığında orta alanda bir yoğunluk görülmekte. Trafik max durumdayken zararlı madde artışı net olmasada min ile max oratasında bir yığılma var. Bu da zararlı madddelerin çoğunlukla %20 - %30 civarında artışa geçtiğini gösteriyor. Ancak bu maddelerin artışında bir çok faktörün rol oynadığı unutulmamalıdır. CO grafiğine bakıldığında diğerlerine kıyasla trafik ile daha paralel bir artış gerçekleştiğini söylemek mümkün. Bu da CO değerinin, Trafik_Indeks oranını tahmin etme aşamasında yüksek ağırlıklardan birisi olacağını göstermektedir.

## LSTM Algoritması ile Trafik İndeks Tahmini

LSTM bir RNN algoritmasıdır. Yapılan çalışmalarda yinelenen sinir ağları(RNN), yapısal olarak bu çalışmaya daha uygun olacağı düşünülmüştür. Yapay öğrenme gerçekleşirken yüksek kaynak tüketimi nedeni ile Google Colab ile çalışma devam etmiştir.

##### Grafik oluşturmak için kullanılan .py dosyası :　

```python
from google.colab import files
uploaded = files.upload()
!pip install pyyaml h5py
import io
import pandas as pd
import numpy as np

data = pd.read_excel(io.BytesIO(uploaded['merged_full.xlsx']))


import math
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt


plt.figure(figsize=(20,6))
plt.plot(data.Tarih,data.Trafik_Indeks)
plt.show()


veri = data.filter(['Trafik_Indeks'])
dataset = veri.values
training_data_len = math.ceil( len(dataset) *.8)
scaler = MinMaxScaler(feature_range=(0, 1)) 
scaled_data = scaler.fit_transform(dataset)

train_data = scaled_data[0:training_data_len  , : ]
x_train=[]
y_train = []
for i in range(60,len(train_data)):
    x_train.append(train_data[i-60:i,0])
    y_train.append(train_data[i,0])
    
    
x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))


model = Sequential()
model.add(LSTM(units=50, return_sequences=True,input_shape=(x_train.shape[1],1)))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dense(units=25))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error',metrics=["accuracy",'mse','mae'])

model.fit(x_train, y_train, batch_size=1, epochs=70)

test_data = scaled_data[training_data_len - 60: , : ]

x_test = []
y_test =  dataset[training_data_len : , : ]
for i in range(60,len(test_data)):
    x_test.append(test_data[i-60:i,0])
    
x_test = np.array(x_test)

x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1],1))   

predictions = model.predict(x_test) 
predictions = scaler.inverse_transform(predictions)

rmse=np.sqrt(np.mean(((predictions- y_test)**2)))
rmse


train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions

plt.figure(figsize=(25,8))
plt.title('Model')
plt.xlabel('Tarih', fontsize=18)
plt.ylabel('Trafik', fontsize=18)
plt.plot(train['Trafik_Indeks'])
plt.plot(valid[['Trafik_Indeks', 'Predictions']])
plt.legend(['Eğitim Verisi', 'Gerçek Değer', 'Tahmin'], loc='lower right')
plt.show()

valid

model.save_weights('model.h5')

print("Ortalama Kayıp:",np.mean(model.history.history["loss"]))


plt.plot(model.history.history["loss"])
plt.title("Model Başarımları")
plt.ylabel("Kayıp Oranı")
plt.xlabel("Epok")
plt.legend(["Kayıp","Test"],loc="upper left")
plt.show()

from keras.callbacks import History 
history = History()
plt.plot(model.history.history['mse'])
plt.plot(model.history.history['mae'])
plt.legend(["Mean Squared Error","Mean Absolute Error"],loc="upper left")
plt.show()

```

Model oluşturulurken bir çok farklı düğüm ve katman modeli test edilmiştir. Ancak en stabil çalışan model söz konusu model olduğu için bu şekilde devam edilmiştir. Eğitim için verinin %80'i kullanılmıştır.

Eğitilmiş model ile her çalışmada başlangıcında tekrar tekrar eğitim gerçekleştirmemek adına modelin ağırlık dosyası kaydedilip çalışma başında yüklenerek ilerleme kaydedildi. Bu sayede lokal bilgisayarlarda çalışma imkanı elde ettik. Aynı zamanda bu ağırlık dosyası konu ile ilgili tahmin uygulamaları geliştirmelerinde kullanılabilir hale geldi.

Eğitim sonrasında `rmse` değerine bakıldığında `7.496736151229131` gibi bir değer görülmekte. Bu değer 0'a ne kadar yakın olursa; tahmin değerleri, gerçek değerler kümesine o kadar yaklaşır. Bu da başarımın ve kaybı temsil değerlerinden biridir.

Ortalama kayıp ve hata değerleri aşağıdaki grafiklerde gösterilmiştir:

![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/avg_loss.png)
![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/mse.png)


Test amaçlı olarak ayrılan 60 gerçek veri ile tahmini verileri içeren bir dataframe oluşturulmuştur. Gerçek değerler ile tahmin değerlerini net bir şekilde görmek adına çizgi grafiğinde gösterilmiştir.

![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/Figure_1.png)

Sonuç olarak bir genelleme yapılırsa algoritmanın tahminleri yaklaşık olarak yapması ve hata oranlarının düşük olması zararlı maddelerin oranı trafik ile ilişkisinin güçlü olduğunu söyleyebiliriz. Bu durumda trafik etkeninin hava kalitesindeki ağırlığı gözler önüne serilmiştir.
