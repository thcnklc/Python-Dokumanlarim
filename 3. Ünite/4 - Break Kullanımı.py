#Author : Taha Çinkılıç
#Subject : Break Kullanımı
#------------------------------------------------------------------------------
#"break" ifadesi sadece döngülerde kullanılır.
#While döngüsünde "break" kullanma:
i = 0
while i < 10: #"i" değişkenimin değeri 10'dan küçük olduğu müddetçe;
    if i == 6: #Eğer "i" değişkenimin değeri 5'e eşitse;
        break #Döngüyü kır.
    print(i) #"i" değişkenimin değerini yazdır.
    i += 1 #"i" değişkenimin değerine 1 ekle.
#------------------------------------------------------------------------------
#For döngüsünde "break" kullanma:
liste1 = [1 , 2 , 3 , 4 , 5]
for i in liste1:
    if i == 3:
        break
    print(i)
"""
Listemizi, içinde bulunan "3" değerine kadar yazdırdık. Python'da liste okuma-
ları soldan sağa olur.
"""
#------------------------------------------------------------------------------
#Örnek:
while True: #Döngü biz kırana kadar devam edecek.
    isim = input("İsminizi giriniz.(Çıkmak için 'q'ya basınız.)\n")
    if isim == "q":
        break
    print("İsminiz : " , isim)
#------------------------------------------------------------------------------