#Author : Taha Çinkılıç
#Subject : Random ve Time Modülü İle Sayı Tahmin Oyunu
#------------------------------------------------------------------------------
import random
import time

print("""
-----------SAYI TAHMİN OYUNU-----------
1 ile 100 arasında bir sayı tahmin edin.
""")
random_sayı = random.randint(1 , 100)
tahmin_hakkı = 5
while True:
    tahmin = int(input("Tahmininiz : "))
    if (tahmin < random_sayı):
        print("Sorgulanıyor...")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin.")
        tahmin_hakkı -= 1
    elif (tahmin > random_sayı):
        print("Sorgulanıyor...")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyin.")
        tahmin_hakkı -= 1
    else:
        print("Sorgulanıyor")
        time.sleep(1)
        print("Tebrikler! Sayımız : " , random_sayı)
        break
    if (tahmin_hakkı == 0):
        print("Tahmin hakkınız bitti. Sayımız : " , random_sayı)
        break
        # ------------------------------------------------------------------------------