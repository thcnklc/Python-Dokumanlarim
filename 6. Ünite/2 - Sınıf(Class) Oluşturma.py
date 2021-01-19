#Author : Taha Çinkılıç
#Subject : Sınıf(Class) Oluşturma (2)
#------------------------------------------------------------------------------
#"__init__ metodunu anlama:
class araba(): #Araba classımızı oluşturmaya başladık.
    model = "KIA Cee'd" #Model değişkenini tanımladık.
    renk = "Beyaz" #Renk değişkenini tanımladık.
    beygir = 128 #Beygir değişkenimizi tanımladık.
    silindir = 4 #Silindir değişkenimizi tanımladık.
    def __init__(self): #"__init__ fonksiyonumuzu tanımladık.
        print("Fonksiyon çağırıldı.")
araba1 = araba() #"araba1" objemizi, yazdığımız class yardımı ile oluşturduk.
araba1 #Fonksiyonumuzun çağrılıp çağrılmadığını test ettik.
"""
Fonksiyonumuzun parantezi içerisinde bulunan "self" anahtar kelimesi, objemi-
zi oluşturduğumuz zaman o objemizi gösteren bir referanstır ve metodlarımızda
en başta bulunması gereken bir parametredir. Bir objenin bütün özelliklerini
ve metodlarını bu referans üzerinden kullanabiliriz.
"""
#------------------------------------------------------------------------------