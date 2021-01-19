#Author : Taha Çinkılıç
#Subject : Kullanıcının Girdiği Sayıya Kadar Olan Mükemmel Sayıları Yazdırma
#------------------------------------------------------------------------------
def mükemmelsayı(a):
    toplam = 0
    for i in range(1 , a):
        if a % i == 0:
            toplam += i
    return a == toplam
sayı = int(input("Hangi sayıya kadar olan mükemmel sayıların yazdırılacağını giriniz : "))
for i in range (2 , sayı):
    if mükemmelsayı(i):
        print(i)
#------------------------------------------------------------------------------