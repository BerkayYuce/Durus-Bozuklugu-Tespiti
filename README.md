# Duruş Bozukluğu Tespiti Veri Seti Oluşturma
### Sınıflandırma problemi için büyük ölçekli veri seti oluşturma (Veri Adedi: 25.677) </br> </br>
Kullanılan Teknolojiler: </br>
`PROGRAMLAMA DİLİ: Python` </br>
`KULLANILAN KÜTÜPHANELER: Selenium, Pillow` </br>
`IDE: PyCharm Community Edition` </br> 
`TARAYICI: Google Chrome Driver` </br> </br>
## Hastalık Sınıflarımız (Sınıflandırma Problemi) </br>
*Bu projede sınıflandırma problemi üzerinde çalıştık ve duruş bozuklukları tespiti için beş sınıflı bir veri seti hazırladık. Hastalıklar şunlardır;* </br>
**-Pektus Karinatum (Güvercin Göğüsü)** </br>
**-Pektus Ekskavatum (Kunduracı Göğüsü)** </br>
**-Poland Sendromu (Kas Eksikliği)** </br>
**-Skolyoz (Omurga Eğriliği)** </br>
**-Kifoz (Kamburluk)** </br>
## Google Görsellerden Görüntü İndirme </br>
*Python 'Selenium' kütüphanesini kullanarak veri setimizi oluşturmak için 'Chrome Driver' aracılığıyla google görsellerden verilerimizi indirdik. Bunun için istediğimiz sorguyu google görsellerde arattık. Aşağıdaki resimde bunun nasıl yapıldığını görebilirsiniz.* </br> </br> </br>
<img width="677" alt="download" src="https://github.com/user-attachments/assets/5e11cc0c-1df1-4145-997a-e516b846ba61"> </br>
*Burada 'query' değişkenini google görsellerde arama çubuğu için kullanıyoruz.* </br> </br> 
<img width="1234" alt="2" src="https://github.com/user-attachments/assets/0aa23f3c-afdc-423a-8948-82a659e9eeb2">
*(Chrome Driver Ekranı)* </br> </br>

## Veri Ön İşleme </br>
*Veri ön işleme (data preprocessing), ham veriyi model eğitimi için hazırlama sürecidir. 
Görsellerdeki gürültüyü azaltmak, boyutları düzenlemek ve görsel formatı standardize etmek gibi işlemleri içerir. 
Model eğitimi sırasında tüm verilerin boyutunun aynı olması önemlidir. Bu yüzden bizde indirdiğimiz görüntülerin boyutlarını eşitledik. 
Ayrıca görüntülerin daha kaliteli olması için de kalite iyileştirmesi yapmaya çalıştık.* </br> </br>
<img width="373" alt="resize" src="https://github.com/user-attachments/assets/16ddd191-f1bf-47f4-9893-e1da39f1b49f"> 
<img width="350" alt="quality" src="https://github.com/user-attachments/assets/f4da43e2-9569-4ffb-b284-9f7b8baffaf8">


## Veri Artıma </br>
*Veri artırma (data augmentation), mevcut veri setini artırmak için kullanılan bir tekniktir. 
Görseller üzerinde döndürme, çevirme, parlaklık ayarı, zoom gibi farklı işlemler uygulanarak yeni veriler oluşturulur. 
Bu projede, Pillow kütüphanesi ile data augmentation işlemleri gerçekleştirdik ve görsellerin çeşitliliğini artırdık.*
