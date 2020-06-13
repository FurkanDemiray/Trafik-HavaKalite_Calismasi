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


| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ |:---------------:| -----:|
| col 3 is      | some wordy text | $1600 |
| col 2 is      | centered        |   $12 |
| zebra stripes | are neat        |    $1 |
