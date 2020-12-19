#Author : Taha Çinkılıç
#Subject : Lambda İfadeleriyle Fonksiyon Tanımlama
#------------------------------------------------------------------------------
#Lambda ifadesiyle fonksiyon tanımlama:
def ikiyleçarp(x):
    return x * 2
print(ikiyleçarp(5))
"""
Girdiğimiz sayıyı ikiyle çarpan bir fonksiyon yazdık. Şimdi bu fonksiyonu lambda
ifadesini kullanarak tek satırda yazmaya çalışalım.
"""
üçleçarp = lambda x : x * 3
print(üçleçarp(10))
"""
"üçleçarp" adlı değişkene, bir fonksiyon eşitledik. "lambda"dan sonra bir değiş-
ken tanımladık, iki noktadan sonra ise bu değişken ile ne yapılacağını belirttik.
İki noktadan sonraki kısım, bir nevi bizim "return" değerimiz oldu.
"""
topla = lambda a , b , c : a + b + c
print(topla(10 , 20 , 30))
"""
Bu sefer "lambda" ifadesi ile oluşturduğumuz fonksiyonumuzun içerisine birden çok
değer girdik ve bu değerler ile yapılacak işlemi yazdık.
"""
terscevir = lambda kelime : kelime[::-1]
print(terscevir("Python yazıyorum."))
"""
Lambdadan sonra bir string değişkeni aldık. Sonrasında bu stringi ters yazdırdık.
"""
çiftkontrol = lambda x : x % 2 == 0
print(çiftkontrol(25))
"""
Fonksiyonumuza gönderilen sayının çift olup olmadığını kontrol eden bir fonksi-
yonu "lambda" ifadesi ile yazdırdık. Eğer girilen sayı çift ise fonksiyonumuz 
çıktı olarak "True", değilse "False" değerini verecek.
"""
#------------------------------------------------------------------------------