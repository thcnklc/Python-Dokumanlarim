#Author : Taha Çinkılıç
#Subject : Sınıf(Class) Oluşturma
#------------------------------------------------------------------------------
#Class oluşturma:
class araba(): #Araba classımızı oluşturmaya başladık.
    model = "KIA Cee'd" #Model değişkenini tanımladık.
    renk = "Beyaz" #Renk değişkenini tanımladık.
    beygir = 128 #Beygir değişkenimizi tanımladık.
    silindir = 4 #Silindir değişkenimizi tanımladık.
araba1 = araba() #"araba1" objemizi, yazdığımız class yardımı ile oluşturduk.
araba2 = araba() #"araba2" objemizi, yazdığımız class yardımı ile oluşturduk.
print(araba1.beygir) #"araba1" objemizin beygirini yazdırdık.
print(araba1.model) #"araba1" objemizin beygirini yazdırdık.
print(araba2.beygir) #"araba2" objemizin beygirini yazdırdık.
print(araba2.model) #"araba2" objemizin modelini yazdırdık.
print(araba.silindir) #Sınıfımızdaki silindir değişkeninin değerini yazdırdık.
print(dir(araba)) #Sınıfımız içerisindeki metodları yazdırdık.
"""
Farkındaysanız oluşturduğumuz objelerin ikisinin de değişken değerleri aynıydı.
Bu durumu "__init__" metodu ile düzelteceğiz.
"""
#------------------------------------------------------------------------------