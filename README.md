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


## SDAFLŞKAFEDGK
