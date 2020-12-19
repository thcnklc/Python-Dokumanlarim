#Author : Taha Çinkılıç
#Subject : Fibonacci Dizisi
#------------------------------------------------------------------------------
sayı = int(input("Fibonacci dizinizin kaç eleman içereceğini giriniz : "))
a = [0]
b = [1 , 1]
for i in range(sayı):
    b.append(a[i])
    a.append(b[i + 2] + b[i + 1])
print("{} elemanlı fobonacci diziniz" .format(sayı) , *b[2:] , sep = " -> ")
#------------------------------------------------------------------------------