#Author : Taha Çinkılıç
#Subject : Fonksiyonlarda Parametre Türleri
#------------------------------------------------------------------------------
#Fonksiyonlardaki parametrelere default değerler verme:
def bilgi(isim = "Bilgi Yok." , soyisim = "Bilgi Yok." , numara = "Bilgi Yok."):
    print(f"İsim = {isim} \nSoyisim = {soyisim} \nNumara = {numara}\n")
"""
Fonksiyonumuzu oluşturduk ve bu fonksiyonlardaki değişkenlere default değerler
atadık. Kullanıcının herhangi bir bilgi vermemesi durumunda, bizim yazdığımız
default veriler çıktı olarak verilir.
"""
bilgi() #Fonksiyonumuzu herhangi bir değer vermeden yazdırdık.
bilgi(numara = 543) #Fonksiyonumuzu sadece "numara" vererek yazdırdık.
bilgi(isim = "Taha") #Fonksiyonumuzu sadece "isim" vererek yazdırdık.
bilgi(soyisim = "Çinkılıç") #Fonksiyonumuzu sadece "soyisim" vererek yazdırdık.
#------------------------------------------------------------------------------
#Fonksiyonlara esnek sayıda değer verme:
def yaz(*a):
    print(a)
yaz(1 , 2 , 3 , 4 , 5)
"""
Fonksiyonumuzun parametresini yazmadan önce başına "*" koyduk. Bu sayede fonksi-
yonumuz, bizim verdiğimiz değerlerin hepsi ile işlem yapabilecek. Liste yapıları
gibi düşünebilirsiniz. Fonksiyonumuzdaki "a" parametresini, liste gibi kullanabi-
liriz.
"""
def toplama(*a):
    toplam = 0
    for i in a:
        toplam += i
    return toplam
print(toplama(1 , 2 , 3 , 4 , 5))
"""
For döngüsünü kullanarak liste içerisinde gezinmeyi görmüştünüz. Bu fonksiyonu-
muzdaki "a" parametremizin başındaki yıldız, bu parametrenin birden çok değer
alabileceğini bize gösteriyor. Kullanıcı kaç değer girerse, o kadar değer üze-
rinden işlem yapılacak. "a" parametremizi aldıktan sonra, bunların hepsini top-
lamak için for döngüsünden yardım aldık. "a" parametremizi liste gibi kullanabi-
leceğimizi söylemiştim. For döngümüzde de farkettiyseniz yaptığımız şey bir lis-
tenin içinde gezinmekten farksız. Listenin içindeki tüm değerleri topladık, ve
bu toplamı fonksiyonumuzun return değerine eşitledik. Sonuç olarak da fonksiyo-
numuzdan çıkan değeri yazdırdık.
"""
#------------------------------------------------------------------------------