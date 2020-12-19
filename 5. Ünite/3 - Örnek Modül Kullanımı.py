#Author : Taha Çinkılıç
#Subject : Örnek Modül Kullanımı (3)
#------------------------------------------------------------------------------
#Örnek modülde işlemler:
def factorial (sayı):
    print("Bizim fonskiyon")
    faktoriyel = 1
    if (sayı == 0 or sayı == 1):
        return 1
    else:
        while(sayı >= 1):
            faktoriyel *= sayı
            sayı -= 1
        return faktoriyel
#Fonksiyonumuzu oluşturduk.
from math import *
#"math" modülünün tüm fonksiyonlarını programımıza dahil ettik.
print(factorial(5))
#"factorial(5)" değerimizi yazdırdık.
"""
Farkettiyseniz, programımız yazdığımız fonksiyondaki işlemi değil de, importladığı-
mız modül içerisindeki fonksiyonu kullandı. Python, yazılan kodları yukarıdan aşa-
ğıya doğru sırasıyla çalıştırır. Biz eğer fonksiyonumuzu tanımlamadan önce modülü-
müzü dahil etseydik, bizim fonksiyonumuz çalışacaktı. 
"""
#------------------------------------------------------------------------------