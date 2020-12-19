#Author : Taha Çinkılıç
#Subject : Örnek Modül Kullanımı
#------------------------------------------------------------------------------
#Örnek modülde işlemler:
import math
#"math" modülünü programımıza dahil ettik.
print(dir(math))
#Modülümüzün içindeki fonksiyonları yazdırdık.
print(help(math))
#Modülümüzün içindeki fonksiyonların nasıl kullanıldığını yazdırdık.
print(math.factorial(5))
#"math" modülümüzün içindeki "factorial" fonksiyonumuzu kullandık.
print(math.ceil(7.8))
#"math" modülümüzün içindeki "ceil" fonksiyonumuzu kullandık.
import math as matematik
#"math" modülünün ismini "matematik" olarak değiştirdik.
print(matematik.factorial(5))
#"matematik modülümüzün içindeki "factorial" fonksiyonumuzu kullandık.
from math import *
"""
"math" modülündeki tüm fonksiyonları programa dahil ettik. Artık "math" modü-
lümüzün içindeki fonksiyonları kullanmak için başına "math" yazmamıza gerek
yok.
"""
print(factorial(6))
#"math" modülümüzün içindeki "factorial" fonksiyonumuzu kullandık.
#------------------------------------------------------------------------------