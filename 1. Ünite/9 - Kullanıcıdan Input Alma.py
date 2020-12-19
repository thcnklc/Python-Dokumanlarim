#Author : Taha Çinkılıç
#Subject : Kullanıcıdan Input Alma
#------------------------------------------------------------------------------
#Input fonksiyonunu kullanma:
print(input("Veri ="))
"""
Kullanıcıdan veriyi alıp yazdırdık fakat aldığımız veriyi hiçbir değişkene ata-
madığımız için, alınan veri kaybolacak. Alınan verinin kaybolmasını önlemek için
inputumuzu bir değişkene atayabiliriz.
"""
a = input("Veri = ") #Kullanıcıdan veri aldık ve bir değişkene atadık.
print("Kullanıcının girdiği veri =" , a) #Kullanıcıdan aldığımız veriyi yazdırdık.
print(a * 3)
"""
Normalde kullanıcının girdiği değerin 3 sayısı ile çarpılmasını bekleriz. Fakat
girilen değer üç kez yazılıyor. Çünkü alınan değerin type'ını belirtmedik. Python
bunu string olarak algılıyor ve bu yüzden 3 kez peş peşe yazdırıyor. Bir de şöyle
deneyelim:
"""
print(int(a) * 3) #Kullanıcıdan alınan veriy3 ile çarptık ve yazdırdık.
#Şöyle de yapabilirdik:
b = int(input("Veri =")) #Kullanıcıdan veri integer olarak aldık.
print(b * 5) #Kullanıcından aldığımız veriyi "5" ile çarpıp yazdırdık.
#------------------------------------------------------------------------------
#Örnekler:
c = int(input("Birinci sayı =")) #Birinci sayıyı aldık.
d = int(input("İkinci sayı =")) #İkinci sayıyı aldık.
e = int(input("Üçüncü sayı =")) #Üçüncü sayıyı aldık.
print("Toplam =" , c + d + e) #Alınan üç sayıyı da topladık.
#------------------------------------------------------------------------------