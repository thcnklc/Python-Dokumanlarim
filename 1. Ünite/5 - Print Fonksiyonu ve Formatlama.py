#Author : Taha Çinkılıç
#Subject : Print Fonksiyonu ve Formatlama
#------------------------------------------------------------------------------
#Print fonksiyonu:
print(45) #45 sayısını yazdırdık.
print("Taha") #Ekrana "Taha" yazdırdık.
a = 15
b = 20
print(a + b) #a ve b değişkenlerimizin değerlerini toplatıp yazdırdık.
print(a , b , a + b , "Taha" , "İstanbul")
#------------------------------------------------------------------------------
#Stringlerdeki özel karakterler:
print("Python\nÖğrenmeye\nÇalışıyoruz.") #"\n" operatörü bir sonraki satıra geçmek için kullanılır.
print("Ocak\tŞubat\tMart") #"\t" operatörü konulduğu yerde bir tab boşluk oluşturur.
#------------------------------------------------------------------------------
#Veri tipi bulma:
c = type(5.63)
print(c)
d = type("Taha")
print(d)
e = type(77)
print(e)
#------------------------------------------------------------------------------
#"sep" fonksiyonu:
print(65 , 54 , 79 , 90 , sep = "-")
print(65 , 54 , 79 , 90 , sep = ".")
print("İstanbul'a" , "Yaz" , "Gelmiyor" , sep = "/")
print("İstanbul'a" , "Yaz" , "Gelmiyor" , sep = "\n")
print(65 , 54 , 79 , 90 , sep = "\t")
"""
"sep" fonksiyonu, yazdırılacak değerler arasına istediğimiz işareti koymamıza 
olanak sağlar. Normal şartlarda Python, aralara sadece bir karakterlik boşluk 
koyar.
"""
#------------------------------------------------------------------------------
#Yıldızlı parametreler:
print(* "Python") #"*" paramteresiyle her karakteri ayırdık.
print(* "Python" , sep = "/") #Ayırdığımız karakterlerin arasına "/" ekledik.
print("T" , "B" , "M" , "M" , sep = ".")
print(*"TBMM" , sep = ".")
#------------------------------------------------------------------------------
#"format" fonksiyonu:
print("{} , {} , {}" . format(15 , 25 , "Taha"))
f = 15
g = 25
print("{} + {} değerlerinin toplamı = {}" . format(f , g , f + g))
"""
Yukarıda yazdığımız yazılımda, formatın içindeki değerler print fonksiyonunun
içindeki süslü parantezlerin sırasına göre yerleştirildi.
"""
print("{1} {0} {2}" . format("çok" , "İstanbul" , "soğuk!"))
"""
Yukarıda yazdığımız yazılımda ise, formatın içindeki değerler print fonksiyonu-
nun içindeki süslü parantezlerin sayılarına göre yerleştirildi.
"""
print("{:.2f} {:.3f}" . format(4.124789652 , 67.458796562))
"""
"f" harfinden önce gelen rakam, formatın içindeki sayının ondalıklı kısmından
sonra kaç rakamının alınacağını belirtir.
"""
"""
Format fonksiyonuyla alakalı daha fazla bilgi için "pyformat.info" sitesinden 
yararlanabilirsiniz.
"""
#------------------------------------------------------------------------------