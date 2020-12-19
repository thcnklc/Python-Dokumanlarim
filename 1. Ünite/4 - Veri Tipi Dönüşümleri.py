#Author : Taha Çinkılıç
#Subject : Veri Tipi Dönüşümleri
#------------------------------------------------------------------------------
#Değişken tipleriyle oynama:
a = 56 #Tam sayı değeri(integer) tanımladık.
b = 45.32 #Ondalıklı sayı değeri(float) tanımladık.
c = float(a) #Tam sayı değerimizi ondalıklı sayıya çevirdik.
print(c)
d = int(b)
print(d)
#------------------------------------------------------------------------------
#Sayıları stringe çevirme:
e = str(150.15) #150.15 sayısını string tipine çevirdik.
print(e)
print(len(e)) #Sayımız artık bir string olduğundan karakter sayısı bulunabilir.
#------------------------------------------------------------------------------
#Stringleri sayıya çevirme:
f = str(2020) #Stringimizi tanımladık.
f = int(f) #Stringimizi tam sayı formuna çevirdik.
print(f)
#------------------------------------------------------------------------------