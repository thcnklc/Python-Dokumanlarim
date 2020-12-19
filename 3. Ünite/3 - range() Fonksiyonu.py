#Author : Taha Çinkılıç
#Subject : range() Fonksiyonu
#------------------------------------------------------------------------------
#range() fonksiyonunu kullanma:
print(*range(0 , 20))
#0'dan başlayıp  20'ye kadar olan sayıları yazdırdık.
print(list(range(0 , 20)))
#0'dan başlayıp 20'ye kadar olan sayıları listeledik.
print(*range(1 , 20))
#1'den başlayıp 20'ye kadar olan sayıları yazdırdık.
print(*range(20))
"""
"range()" fonksiyonunun içine bir başlangıç değeri yazmazsanız, pyhton otomatik
olarak başlangıç değerini "0" alır.
"""
print(*range(1 , 100 , 2))
#1'den başlayıp 100'e kadar olan sayıları ikişer atlayarak yazdırdık.
print(*range(3 , 100 , 3))
#3'ten başlayarak 100'e kadar olan ve üçe bölünebilen sayıları yazdırdık.
print(*range(50 , 0 , -1))
#50'den başlayarak 0'a kadar birer birer azaltarak yazdırdık.
#------------------------------------------------------------------------------
#range() fonksiyonunu "for" döngülerinde kullanma:
for i in range(1 , 100):
    print(i)
#1'den başlayarak 100'e kadar olan sayıları yazdırdık.
for i in range(1 , 10):
    print("* " * i)
"""
Önceki derslerimizden hatırlıyorsanız "string"leri "integer"lar ile çarpabili-
yorduk. Bu for döngüsünde de "i" değişkenimizi ,değeri her arttığında bir adet
"*" ile çarptık.
"""
#------------------------------------------------------------------------------