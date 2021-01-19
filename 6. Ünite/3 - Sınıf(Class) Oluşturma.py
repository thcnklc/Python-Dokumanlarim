#Author : Taha Çinkılıç
#Subject : Sınıf(Class) Oluşturma (3)
#------------------------------------------------------------------------------
#"self" parametresini anlama:
class araba(): #Araba classımızı oluşturmaya başladık.
    def __init__(self , model = "Bilgi yok." , renk = "Bilgi yok." , beygir = "Bilgi yok." , silindir = "Bilgi yok."):
        self.model = model
        self.renk = renk
        self.beygir = beygir
        self.silindir = silindir
araba1 = araba("KIA Cee'd" , "Siyah" , "128" , "4")
araba2 = araba("AUDI A6" , "Beyaz" , "310" , "6")
araba3 = araba(renk = "Siyah") #"araba3" objemizin sadece "renk" değişkenine değer verdik.
print(araba1.model)
print(araba2.silindir)
print(araba3.silindir)
"""
"araba" classımızı tanımladıktan sonra bu class yardımı ile objelerimizi oluştur-
duk. Objelerimizi oluştururken classımız içerisindeki değişkenleri bir fonksiyona
değer giriyormuş gibi girdik. Classımızın içerisinde bulunan "__init__" metodumuz-
daki tüm değişkenlerin önünde farkettiyseniz "self" parametremizi kullandık. Bu
parametreyi bir nevi sahiplik olarak düşünebilirsiniz. Bulunduğu classa ait özel-
likleri sahiplenen bir parametre.
Metodumuzun içerisinde bulunan değişkenlerimize default değerler verdik. O değiş-
kene ait bir bilgi girilmediği zaman, biz o bilgiye erişmek istersek verdiğimiz
defult değer baz alınacak. "print" fonksiyonu ile yazdırdığımız değerleri dikkat-
lice inceleyin.
"""
#------------------------------------------------------------------------------