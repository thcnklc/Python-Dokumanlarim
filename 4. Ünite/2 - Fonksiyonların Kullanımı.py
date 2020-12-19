#Author : Taha Çinkılıç
#Subject : Fonksiyonların Kullanımı
#------------------------------------------------------------------------------
#Fonksiyon oluşturma:
def selamla(): #"selamla" adlı fonksiyonumuzu defineladık.
    print("Selam!") #"Selam!" yazdırdık.
selamla() #"selamla" fonksiyonumuzu çağırdık.
print(type(selamla)) #Fonksiyonumuzun veri tipini yazdırdık.
def selamla1(isim): #"selamla1" adlı fonksiyonumuzu defineladık.
    print("Selam" , isim)
selamla1("Taha") #"selamla1" fonksiyonumuzu çağırdık.
def topla(a , b , c): #"topla" adlı fonksiyonumuzu defineladık.
    print(f"{a} + {b} + {c} = {a + b + c}")
topla(10 , 20 , 30) #"topla" fonksiyonumuzu çağırdık.
def faktöriyel(sayı): #"faktoriyel" adlı fonksiyonumuzu defineladık.
    faktöriyel = 1
    if sayı == 0 or sayı == 1:
        print(f"{sayı}! = {faktöriyel}")
    else:
        for i in list(range(1 , sayı + 1)):
            faktöriyel *= i
        print(f"{sayı}! = {faktöriyel}")
faktöriyel(5) #"faktoriyel" fonksiyonumuzu çağırdık.
#------------------------------------------------------------------------------