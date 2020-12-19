#Author : Taha Çinkılıç
#Subject : Mantıksal Değerler ve Karşılaştırma Operatörleri
#------------------------------------------------------------------------------
#Boolean:
a = True
print(type(a)) #"a" değişkeninin tipini yazdırdık.
b = False
print(type(b)) #"b" değişkeninin tipini yazdırdık.
"""
Eğer bir boolean parantezinin içine 0'dan farklı bir sayı yazarsak, Python bunu
True olarak anlayacak. Eğer boolean parantezinin içine 0'dan farklı bir sayı
yazmazsak, Python bunu False olarak anlayacak.
"""
print(bool(0)) #Boolean içinde "0" değerimizin ne olduğunu yazdırdık.
print(bool(0.30)) #Boolean içinde "0.30" değerimizin ne olduğunu yazdırdık.
print(bool(15)) #Boolean içinde "15" değerimizin ne olduğunu yazdırdık.
print(1 == 1) #Yazdığımız şeyin doğru veya yanlışlığını yazdırdık.
print(1 == 10) #Yazdığımız şeyin doğru veya yanlışlığını yazdırdık.
#------------------------------------------------------------------------------
#None değişkeni:
c = None #"c" değişkeninin değerini "None" yaptık.
print(c)
c = 100 #"c" değişkenimize değer verdik.
print(c)
#------------------------------------------------------------------------------
#Karşılaştırma operatörleri:
"""
== -> İki değer birbirine eşitse True, değilse False.
!= -> İki değer birbirine eşit değilse True, eşitse False.
>  -> Soldaki değer sağdaki değerden büyükse True, değilse False.
<  -> Sağdaki değer soldaki değerden büyükse True, değilse False.
>= -> Soldaki değer sağdaki değerden büyükse veya eşitse True, değilse False.
<= -> Sağdaki değer soldaki değerden büyükse veya eşitse True, değilse False.
"""
print("Taha" == "Taha")
print("Taha" == "ahaT")
print(15 <= 2)
print(22 >= 2)
print("Taha" != "ahaT")
print([1 , 2 , 3] == [1 , 2 , 3])
print([1 , 2 , 3] == [1 , 3 , 3])
print("Ardahan" < "İzmir") #Alfabetik sıraya göre baktık.
#------------------------------------------------------------------------------