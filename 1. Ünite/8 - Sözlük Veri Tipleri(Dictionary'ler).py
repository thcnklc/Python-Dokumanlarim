#Author : Taha Çinkılıç
#Subject : Sözlük Veri Tipleri(Dictionary'ler)
#------------------------------------------------------------------------------
#Sözlük oluşturma:
sözlük1 = {"Bir" : 1 , "İki" : 2 , "Üç" : 3 , "Dört" : 4} #Sözlük oluşturduk.
print(sözlük1) #Oluşturduğumuz sözlüğü yazdırdık.
sözlük2 = dict() #Boş sözlük oluşturduk.
print(sözlük2) #Boş sözlüğümüzü yazdırdık.
#------------------------------------------------------------------------------
#Sözlük değerlerine erişme:
print(sözlük1["Bir"]) #Sözlüğümüzdeki "Bir" in değerini yazdırdık.
print(sözlük1["Üç"]) #Sözlüğümüzdeki "Üç" ün değerini yazdırdık.
#------------------------------------------------------------------------------
#Sözlüğe değer ekleme:
sözlük1["Beş"] = 5 #Sözlüğümüze "Beş" değerini ekledik.
print(sözlük1) #Değer eklediğimiz sözlüğü yazdırdık.
#------------------------------------------------------------------------------
#Örnekler:
sözlük3 = {"A" : [[1 , 2] , [3 , 4 , 5] , 6] , "B" : 12}
print(sözlük3["A"][1][0])
"""
Sözlüğümüzün içinde bulunan "A" listesinin 1. indeksini bulduk. Ardından bu in-
deksin de içinden 0. indeksimizi bulup yazdırdık.
"""
sözlük3["A"][1][0] = 6
print(sözlük3)
"""
Sözlüğümüzün içinde bulunan "A" listesinin 1. indeksini bulduk. Ardından bu in-
deksin de içinden 0. indeksimizi bulup "6" ile değiştirdik. Değişen sözlüğümüzü
yazdırdık.
"""
sözlük3["B"] = 10 #Sözlüğümüzdeki "B" değerimizi 10 yaptık.
print(sözlük3) #Değişen sözlüğümüzü yazdırdık.
sözlük3["B"] += 1 #Sözlüğümüzdeki "B" değerimizi 1 artırdık.
print(sözlük3) #Değişen sözlüğümüzü yazdırdık.
#------------------------------------------------------------------------------
#İç içe sözlükler:
sözlük4 = {"Şehirler" : {"İstanbul" : "İs" , "İzmir" : "İz" , "Ankara" : "An"} , "Sayılar" : {"Bir" : 1 , "İki" : 2 , "Üç" : 3}}
print(sözlük4["Sayılar"]["İki"])
"""
Oluşturduğumuz sözlükteki "Sayılar" sözlüğünün içinde bulunan "İki" nin değeri-
ni yazdırdık.
"""
#------------------------------------------------------------------------------
#Keys metodu:
sözlük5 = {"Şehirler" : {"İstanbul" : "İs" , "İzmir" : "İz" , "Ankara" : "An"} , "Sayılar" : {"Bir" : 1}}
print(sözlük5.keys()) #Sözlüğümüzün içindeki anahtar değerleri yazdırdık.
print(sözlük5["Şehirler"].keys())
"""
Sözlüğümüzüm içinde bir "Şehirler" adında bir sözlüğümüz daha vardı. Bu sefer
bu sözlüğümüzün içindeki anahtar değerleri yazdırdık.
"""
#------------------------------------------------------------------------------
#Values metodu:
sözlük6 = {"Bir" : 1 , "İki" : 2 , "Üç" : 3 , "Dört" : 4 , "Beş" : 5 , "Altı" : 6}
print(sözlük6.values()) #Sözlüğümüzün içindeki değerleri yazdırdık.
#------------------------------------------------------------------------------
#İtems metodu:
print(sözlük6.items()) #Sözlüğümüzü demet veri tipine uygun yazdırdık.
#------------------------------------------------------------------------------