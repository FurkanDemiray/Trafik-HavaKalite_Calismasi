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

Grafiğe bakıldığında genellikle bir değer pick yaptığında diğer değerlerle birlikte artışa geçmiş. Bu da bizlere zararlı maddeler arasında bir bağlantı olduğu, aynı zamanda bir tetikleme(Trafik artışı, Sanayi aktivitesi) ile pick yaptığı düşünülebilir. Trafik artışı ile maddelerin paralel ilerlemesi kaydadeğer şekilde bir ilişkiyi göstermektedir.

Trafik ve zararlı maddeler ilişkisini daha net görmek adına her maddeyi trafik oranıyla birlikte ele alalım. İki durum arasındaki ilişkiyi en net şekilde gösteren grafiklerden biriside korelasyon grafikleridir. 

![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/KolerasyonCO.png)
![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/KolerasyonNO.png)
![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/KolerasyonNO2.png)
![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/KolerasyonNOX.png)
![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/KolerasyonPM10.png)
![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/KolerasyonSO2.png)
![](https://github.com/FurkanDemiray/Trafik-HavaKalite_Calismasi/blob/master/Graphs/Korelasyon_O3.png)

Grafiklere bakıldığında orta alanda bir yoğunluk görülmekte. Trafik max durumdayken zararlı madde artışı net olmasada min ile max oratasında bir yığılma var. Bu da zararlı madddelerin çoğunlukla %20 - %30 civarında artışa geçtiğini gösteriyor. Ancak bu maddelerin artışında bir çok faktörün rol oynadığı unutulmamalıdır. CO grafiğine bakıldığında diğerlerine kıyasla trafik ile daha paralel bir artış gerçekleştiğini söylemek mümkün. Bu da CO değerinin, Trafik_Indeks oranını tahmin etme aşamasında yüksek ağırlıklardan birisi olacağını göstermektedir.




