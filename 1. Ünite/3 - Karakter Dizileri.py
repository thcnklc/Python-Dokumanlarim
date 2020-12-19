#Author : Taha Çinkılıç
#Subject : Karakter Dizileri
#------------------------------------------------------------------------------
#String oluşturma:
a = 'a'
b = "b"
c = """c"""
#Hatalı kod : "Hatalı'
print(a , b , c)
#Stringleri tek tırnak, çift tırnak veya 3 çift tırnak ile oluşturabilirsiniz.
#------------------------------------------------------------------------------
#Kullanım örnekleri:
"""
#Hatalı yazım :
#print('Ali'yi okula götür.')
#Doğru yazım :
"""
print('Ali\'yi okula götür.')
#Veya:
print("Ali'yi okula götür.")
"""
String'e hangi tırnak ile başlarsanız, o tırnak ile bitirmelisiniz. Tek tırnak
ile başladıysanız, cümle içinde tek tırnak kullanamazsınız. Çift tırnak ile
başlarsanız, cümle içinde çift tırnak kullanamazsınız. Eğer kullanmak istiyor-
sanız, yukarıda verilen örnekteki gibi bir kullanım yapmalısınız. Yani kullana-
cağınız tırnak işaretinden önce "\" işaretini koymalısınız.
"""
#------------------------------------------------------------------------------
#String indeksleme ve parçalama:
d = "Ali"
print(d[1]) #d stringinin 1. elemanını yazdırdık.
print(d[-1]) #d stringinin -1. elemanını yazdırdık.
"""
-Stringlerin idnekslemesi 0'dan başlar. Örneğin "Ali" kelimesinde 0. harf "A"dır. 
1. harf "l", 2. harf ise "i"dir.
-Stringler sadece baştan değil, sondan da indekslenebilir. Fakat bu sefer ele-
manların değerleri sıfırdan başlamayacak. Mesela sondan ikinci harfi öğrenmek 
istediğimiz zaman -2. elemanı yazdırmamız gerekir.
-Uzun bir stringin belirli bir kısmını almak istersek şu formülü kullanmamız
gerekiyor: [Başlama indeksi : Bitiş indeksi : Atlama değeri]
"""
e = "Kendinin bilincine varmak hastalıktır."
print(e[7 : 13])
"""
7. indeksten başla, 13. indekse kadar yaz.(13. indeks dahil değil.) Normalde 7.
harfimizin "i" olduğunu görebilirsiniz. Fakat aldanmayın, indeksleme her zaman
0 dan başlar.
"""
print(e[:22]) #22. indekse kadar yaz. 22. indeksi dahil etme.
print(e[26:]) #26. indeksten sonrasını yazdırdık.
print(e[:]) #Bütün stringi baştan sona yazdırdık.
print(e[:-1]) #-1. indeskten öncesini yazdırdık.
print(e[::2]) #Indeksleri 2'şer atlayarak yazdırdık.
print(e[2:23:3]) #2. indeksten başlayarak 23. indekse kadar 3'er atlayarak yazdırdık.
print(e[::-1]) #Stringi tersten yazdırdık.
#------------------------------------------------------------------------------
#String özellikleri:
print(len(e)) #e stringinin karakter sayısını(uzunluğunu) yazdırdık.
f = "Bugün "
g = "Okula "
h = "Gitmedim."
print(f + g + h) #Stringler de integerlar gibi toplanabilirler.
print(f * 3) #Stringlere de çarpma işlemi uygulayabiliriz.
#------------------------------------------------------------------------------