#Author : Taha Çinkılıç
#Subject : Liste Veri Tipleri
#------------------------------------------------------------------------------
#Liste oluşturma:
liste1 = [1 , 2 , 3 , "Armut" , "42" , 25]
a = type(liste1) #Yukarıda d-yazdığımız kodun liste tipinde olduğunu gösterdik.
print(a) #Listemizin tipini yazdırdık.
print(liste1) #Listemizi yazdırdık.
#Listeler boş da olabilirler.
print(len(liste1)) #Listemizin eleman sayısını aldık.
liste2 = list("18.08.1999 doğum günüm")
print(liste2) #Listemizi yazdırdık.
print(len(liste2)) #Listemizin uzunluğunu yazdırdık.
"""
Verdiğimiz stringin tüm karakterlerini "list()" komutu ile bir listeye çevirdik.
"list()" fonksiyonunun içine yazdığımız her string, bize liste şeklinde sunula-
caktır.
"""
#------------------------------------------------------------------------------
#Listeleri indeksleme:
liste3 = [1 , 2 , 3 , 4 , 5 , 9]
print(liste3[2]) #Listemizin ikinci elemanını yazdırdık.
print(liste3[-1]) #Listemizin sondaki elemanını yazdırdık.
print(liste3[len(liste3) - 1]) #Listemizin son elemanını farklı bir yolla yazdırdık.
"""
Sondaki elemanı yazdırmak için farklı bir yol daha yazdık. Listemizin uzunluğunu
öğrenmek istediğimiz zaman "len()" komutunu kullanıyorduk. Bu komutu yazıp ça-
lıştırdığımız zaman "6" değerini çıktı olarak alıyoruz. Fakat hatırlarsanız in-
deksleme işlemleri her zaman "0"dan başlıyordu. Bu yüzden listenin uzunluğundan
"1" çıkardığımız zaman python, bize son elemanı çıktı olarak verecektir.
"""
#------------------------------------------------------------------------------
#Listeleri parçalama:
print(liste3[2:]) #Listenin ikinci elemanından itibaren yazdırdık.
print(liste3[::2]) #Baştan sona kadar ikişer atlayarak yazdırdık.
print(liste3[::-1]) #Listemizi tersten yazdırdık.
#------------------------------------------------------------------------------
#Temel liste işlemleri:
liste4 = [1 , 2 , 3]
liste5 = [4 , 5 , 6]
liste6 = ["İstanbul" , "Ankara" , "İzmir"]
print(liste4 + liste5 + liste6) #Üç listeyi topladık ve yazdırdık.
print(liste6 * 3) #Listemizi 3 kez yazdırdık.
"""
Listemizi 3 ile çarparak 3 kez yazdırılmasını sağladık. Fakat listemize herhangi
bir değişime sebebiyet vermedik. Listemiz hala aynı. Eğer listemizi değiştirmek
isteseydik şu şekilde yazacaktık:
"""
liste6 = liste6 * 3 #Listemizi 3 kez çarpılmış haliyle değiştirdik.
print(liste6) #Yeni listemizi yazdırdık.
"""
String yapısında herhangi bir indeksi değiştiremiyorduk. Fakat liste yapısında
istediğimiz indeksimizi değiştirmemiz mümkün.
"""
liste7 = ["a" , "b" , "c" , "d" , "e" , "f"]
liste7[3] = "Merhaba" #Listemizin 3. indeksini değiştirdik.
print(liste7) #Değişen listemizi yazdırdık.
liste8 = [1 , 2 , 3 , 4 , 5]
liste8[:2] = [6 , 7] #Listemizin ilk iki elemanını 6 ve 7 ile değiştirdik.
print(liste8)
#------------------------------------------------------------------------------
#Append(Ekleme) metodu:
liste9 = ["a" , "b" , "c" , 1 , 2 , 3 , "Taha" , "İstanbul"]
liste9.append("Python") #Listemize "Python" stringini ekledik.
print(liste9)
#------------------------------------------------------------------------------
#Pop(Çıkarma) metodu:
liste10 = [1 , 3 , 5 , 7 , 9]
print(liste10)
liste10.pop(-1) #Listemizin son elemanını attık.
print(liste10)
liste10.pop(0) #Listemizin ilk elemanını attık.
print(liste10)
#------------------------------------------------------------------------------
#Sort(Sıralama) metodu:
liste11 = [1 , 3 , 2 , 15 , 6 , 384 , 221]
liste11.sort() #Listemizi küçükten büyüğe doğru sıraladık.
print(liste11)
liste11.sort(reverse = True) #Listemizi büyükten küçüğe doğru sıraladık.
print(liste11)
liste12 = ["Taha" , "Sena" , "Meryem" , "Yavuz"]
liste12.sort() #Listemizi alfabetik sıraya göre sıraladık.
print(liste12)
liste12.sort(reverse = True) #Listemizi alfabetik sıraya göre tersten sıraladık.
print(liste12)
#------------------------------------------------------------------------------
#İç içe listeler:
liste13 = ((0 , 1) , (1 , 2) , (2 , 3) , 4 , 5)
print(liste13[1][0]) #Listemizim 1. indeksindeki 0. indeksini yazdırdık.
#------------------------------------------------------------------------------