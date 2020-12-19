#Author : Taha Çinkılıç
#Subject : Temel Matematik Operatörleri
#------------------------------------------------------------------------------
#Toplama işlemi yapma:
print("Toplam =" , 10 + 21.3 + 33)
#------------------------------------------------------------------------------
#Çıkarma işlemi yapma:
print("Çıkarma =" , 48 - 16 - 3.4)
#------------------------------------------------------------------------------
#Çarpma işlemi yapma:
print("Çaprma =" , 4.7 * 8 * 2)
#------------------------------------------------------------------------------
#Bölme işlemi yapma:
print("Bölme =" , 18.2 / 7)
#------------------------------------------------------------------------------
#Tamsayı bölmesi yapma:
print("Tamsayı bölmesi =" , 18.2 // 7)
"""
Ondalıklı sayıları böldüğümüz zaman sonucun tamsayı gelmesini istiyorsak bölme
işaretini iki kez koyuyoruz.
"""
#------------------------------------------------------------------------------
#Kalan bulma:
print("Kalan bulma =" , 15 % 4)
"""
15'in 4'e bölümünden kalan sayıyı bulduk.
Çıkan cevaba göre sayının tekliği veya çiftliğini bu operatörle anlayabiliriz.
"""
#------------------------------------------------------------------------------
#Üs bulma:
print("Üs bulma =" , 2**4)
"""
Çok büyük sayılar, bilgisayarınızın performansı ile doğru orantılı olarak bil-
gisayarınızı zorlayabilir. Verdiğiniz değerlere dikkat edin!
"""
#------------------------------------------------------------------------------
#Karekök bulma:
print("Karekök bulma =" , 100 ** 0.5)
#------------------------------------------------------------------------------
#Küpkök bulma:
print("Küpkök bulma =" , 8 ** (1/3))
#------------------------------------------------------------------------------
#İşaret değiştirme:
a = -4
print("İşaret değiştirme =" , -a)
print("İşaret değiştirme =" , --a)
#------------------------------------------------------------------------------
#Operatörleri beraber kullanma ve işlem sırası:
"""
-Parantez içi her zaman önce yapılır.
-Çarpma ve bölme işlemleri, toplama ve çıkarmaya göre önceliklidir.
-İşlemler soldan sağa yapılır.
"""
print("Parantezsiz işlem =" , 8 + 4 * 3 / 2 - 18)
"""
Önce 4 ile 3'ü çarptı. Sonrasında 12'yi 2'ye böldü. Sonra 6 ile 8'i topladı. 
Son olarak 14'ten 18'i çıkardı. Cevabı -4 olarak bize sundu. 
"""
print("Parantezli işlem =" , 8 + ((4 * 3) / 2) - 18)
"""
Önce 4 ile 3'ü çarptı. Sonrasında 12'yi 2'ye böldü. Sonra 6'dan 18'i çıkardı.
Son olarak -14 ile 8'i topladı ve cevabı -4 olarak bize sundu.
"""
print("Parantezi değişen işlem =" , (8 + 4) * 3 / 2 - 18)
"""
Önce 8 ile 4'ü topladı. Sonrasında 12 ile 3'ü çarptı. Sonra 36'yı 2'ye böldü.
Son olarak 18'den 18'i çıkardı ve cevabı 0 olarak bize sundu.
"""
#------------------------------------------------------------------------------