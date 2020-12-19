#Author : Taha Çinkılıç
#Subject : Fonksiyonlarda Return
#------------------------------------------------------------------------------
#Fonksiyonlarda return kullanma:
def topla(a , b):
    print(f"{a} + {b} = {a + b}")
    return a + b
def ikiyleçarp(a):
    print(f"{a} x 2 = {a * 2}")
    return a * 2
def dördeböl(a):
    print(f"{a} / 4 = {a / 4}")
    return a / 4
print(dördeböl(ikiyleçarp(topla(10 , 10)))) #Fonksiyonlarımızı iç içe yazdırdık.
print(type(topla) , type(ikiyleçarp) , type(dördeböl))
#Fonksiyonlarımızın tipini yazdırdık.
#------------------------------------------------------------------------------
"""
Üç adet fonksiyon tanımladık. Bunlardan ilki, girilen sayıları topluyor. İkincisi
girilen sayıyı iki ile çarpıyor. Üçüncüsü ise girilen sayıyı dörde bölüyor. Son
işlem olarak da bu fonksiyonları birlikte kullandık. Matematiksel işlemlerde nasıl
ki parantez içine öncelik veriliyorsa, yazılım yazarken de aynı kural geçerlidir.
Eğer biz fonksiyonlar içerisinde kullandığımız "print"leri "return"den önce yaz-
saydık, fonksiyonlarımız bize "print" kullanmadan herhangi bir çıktı vermeyecek-
lerdi. Fonksiyonlardaki "return", döngü yapılarındaki "break" ile bir nevi işlev
bakımından benzerdirler. "return" satırında girilen değer, fonksiyonumuzun çıktısı
görevini görmekte. Eğer ki biz fonksiyonumuza herhangi bir return değeri vermezsek,
fonksiyonumuzun type'ı "None" olacaktır. Fakat bir "return" değeri verdiğimiz zaman
fonksiyonlarımızın type'ı "function" olarak bize gösterilir. Fonksiyonu fonksiyon
yapan şey, return değeridir. Bir katı meyve sıkacağı düşünün. Bu meyve sıkacağına
elma verirseniz, size elma suyu verir. Fonksiyonlara da girilen değerlerin dışarıya
ne olarak çıkmasını istiyorsanız, return değeri ile bunu belirtmelisiniz. Aksi tak-
dirde fonksiyonunuz sadece içerisindeki blokları çalıştıracak, herhangi bir return
değeri olmaksızın sizin yazdığınız işlemleri tek sefere mahsus yapacak, çıkan değeri
bir başka işlem için kullanamayacaksınız. Yani bir nevi tek sefere mahsus çalışan ve
çıkardığı ürünü tek sefere mahsus kullanabileceğiniz bir makine yazmış olursunuz.
"""
#------------------------------------------------------------------------------