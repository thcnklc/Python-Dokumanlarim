#Author : Taha Çinkılıç
#Subject : While Döngüleri
#------------------------------------------------------------------------------
#While döngüsünü kullanma:
i = 0
while (i < 10): #"i" değişkenimin değeri 10'dan küçük olduğu müddetçe;
    print("i'nin değeri " , i) #"i" değerini yazdır.
    i += 1 #"i" değişkenimin değerine 1 ekle.
"""
"i" değişkenimize "0" değerini atamamızın sebebi bir başlangıç sayısı vermekti.
Döngümüze verdiğimiz koşul, "i" değerimizin "10"dan küçük olması. Yani programı-
mız "i" değerimiz "10"dan küçük olduğu müddetçe while döngümüzün içerisindeki 
komut satırlarını çalıştıracak.
"""
a = 0
while a < 40: #"a" değişkenimin değeri 40'tan küçük olduğu müddetçe;
    print("Python öğreniyorum.") #"Python öğreniyorum." yazdır.
    a += 1 #"a" değişkenimin değerine 1 ekle.
#------------------------------------------------------------------------------
#While döngüsü ile liste işlemleri:
liste1 = [1 , 2 , 3 , 4 , 5]
indeks = 0
while indeks < len(liste1):
    print("İndeks : {} --- Liste Elemanı : {}" . format(indeks , liste1[indeks]))
    indeks += 1
"""
Programımız, "indeks" değerimiz listemizdeki eleman sayısından küçük olduğu müd-
detçe while bloğundaki komut satırlarını çalıştıracak.
"""
#------------------------------------------------------------------------------