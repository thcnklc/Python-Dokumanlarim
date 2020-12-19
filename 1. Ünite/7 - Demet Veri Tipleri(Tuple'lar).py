#Author : Taha Çinkılıç
#Subject : Demet Veri Tipleri(Tuple'lar)
#------------------------------------------------------------------------------
"""
Demetler, listelere oldukça benzerdir. Fakat listelerden farkları, değiştirile-
memeleridir. Bu yüzden programlarımızda değiştirilmesini istemediğimiz değerleri
bir demet içinde depolayabiliriz.
"""
#------------------------------------------------------------------------------
#Demet oluşturma:
demet1 = (1 , 2 , 3 , 4 , 5 , 6)
print(type(demet1)) #"demet1" değişkeninin tipini yazdırdık.
print(demet1[3]) #Demetimizin 3. indeksini yazdırdık.
print(demet1[-1]) #Demetimizin sonuncu indeksini yazdırdık.
print(demet1[::-1]) #Demetimizi tersten yazdırdık.
print(demet1[1:3]) #Demetimizi 1. indeksinden 3. indeksine kadar yazdırdık.
#------------------------------------------------------------------------------
#Count metodu:
demet2 = (1 , 1 , 1 , 1 , 1 , 2 , 3 , 3)
print(demet2.count(1)) #Demetimizin içinde "1"den kaç tane olduğunu yazdırdık.
#------------------------------------------------------------------------------
#İndeks metodu:
demet3 = ("Taha" , "Ankara" , "İstanbul" , "İzmir" , 34)
print(demet3.index("Ankara") , demet3.index(34))
"""
İndeks metodu, aradığımız şeyin kaçıncı indekste olduğunu bize gösteren bir me-
toddur.
"""
#------------------------------------------------------------------------------