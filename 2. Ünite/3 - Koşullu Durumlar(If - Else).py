#Author : Taha Çinkılıç
#Subject : Koşullu Durumlar(If - Else)
#------------------------------------------------------------------------------
#If bloğunu kullanma:
yaş = int(input("Yaşınızı giriniz =")) #Kullanıcıdan yaşını aldık.
if (yaş < 18): #Eğer "yaş" 18'den küçükse;
    print("Yaşınız 18'den küçük.") #"Yaşınız 18'den küçük." yazdır.
#------------------------------------------------------------------------------
#Else bloğunu kullanma:
puan = int(input("Sınav notunuzu giriniz ="))
if (puan < 60): #Eğer "puan" 60'tan küçükse;
    print("Kaldınız!") #"Kaldınız!" yazdır.
else: #Eğer "puan" 60'tan küçük değilse;
    print("Geçtiniz!") #"Geçtiniz!" yazdır.
"""
"Else"den sonra herhangi bir koşul vermeye gerek yoktur. "If" ile verilen koşul
eğer sağlanmazsa, programımız otomatik olarak "Else" bloğunda yazan kodu çalış-
tıracaktır.
"""
#------------------------------------------------------------------------------
#Elif bloğunu kullanma:
işlem = input("İşlem giriniz =")
if (işlem == "1"): #Eğer işlem 1'e eşitse;
    print("1. işlemi seçtiniz.") #"1. işlemi seçtiniz." yazdır.
elif (işlem == "2"): #Eğer işlem 2'ye eşitse;
    print("2. işlemi seçtiniz.") #"2. işlemi seçtiniz." yazdır.
elif (işlem == "3"):#Eğer işlem 3'e eşitse;
    print("3. işlemi seçtiniz.") #"3. işlemi seçtiniz." yazdır.
else: #Eğer işlem 1,2 veya 3'e eşit değilse;
    print("Geçersiz işlem!") #"Geçersiz işlem!" yazdır.
"""
Python, her zaman yukarıdan aşağı doğru okuma yapar. Elif kullanırken dikkat et-
memiz gereken şey şudur; eğer ilk koşul sağlanıyorsa, programımız ilk koşulu ça-
lıştıracak ve diğer koşullara bakmayacaktır. Bir koşul sağlanana kadar Python o-
kumaya devam edecek, fakat bir koşul sağlandıktan sonra diğer koşullara bakmak-
sızın sağlanan koşulu çalıştıracak ve programımızı sonlandıracaktır.
"""
#------------------------------------------------------------------------------
#Örnekler:
note = float(input("Notunuzu giriniz ="))
if (note > 90):
    print("AA")
elif (note > 85):
    print("BA")
elif (note > 80):
    print("BB")
elif (note > 75):
    print("CB")
elif (note > 70):
    print("CC")
elif (note > 65):
    print("DC")
elif (note > 60):
    print("DD")
else:
    print("Kaldınız.")
#------------------------------------------------------------------------------