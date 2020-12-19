#Author : Taha Çinkılıç
#Subject : Metodlar
#------------------------------------------------------------------------------
#Metodları kullanma:
liste = [1 , 2 , 3 , 4 , 5] #Liste oluşturduk.
print(type(liste)) #Oluşturduğumuz listenin veri tipini yazdırdık.
liste.insert(1 , 6) #"insert" metodunu ile listemizin 1. indeksine "6" ekledik.
print(liste) #Yeni listemizi yazdırdık.
liste.append("Taha") #"append" metodu ile listemize "Taha"yı ekledik.
print(liste) #Yeni listemizi yazdırdık.
liste.pop(1) #Listemizin 1. indeksini listemizden çıkardık.
print(liste) #Yeni listemizi yazdırdık.
help(liste.remove) #"remove" metodumuzun ne işe yaradığını yazdırdık.
#------------------------------------------------------------------------------