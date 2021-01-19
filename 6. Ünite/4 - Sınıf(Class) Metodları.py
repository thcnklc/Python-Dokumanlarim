#Author : Taha Çinkılıç
#Subject : Sınıf(Class) Metodları
#------------------------------------------------------------------------------
#Class içerisinde metod tanımlama:
class çalışan():
    def __init__(self , isim , soyisim , numara , maaş , diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maaş = maaş
        self.diller = diller
    def bilgilerigöster(self):
        print(f"İsim = {self.isim}\nSoyisim = {self.soyisim}\nNumara = {self.numara}\nMaaş = {self.maaş}\nDiller = {self.diller}\n")
    def zamyap(self , zam):
        self.maaş += zam
    def dilekle(self , yenidil):
        self.diller.append(yenidil)
çalışan1 = çalışan("Taha" , "Çinkılıç" , 12345 , 6500 , ["Python" , "Java" , "C#" , "C++"])
çalışan1.bilgilerigöster() #"bilgilerigöster" metodumuzu kullandık.
çalışan1.zamyap(1500) #"zamyap" metodumuzu kullandık.
çalışan1.dilekle("JavaScript")#"dilekle" metodumuzu kullandık.
çalışan1.bilgilerigöster()#"bilgilerigöster" metodumuzu kullandık.
"""
Normal fonksiyon tanımlamaktan pek de farkı yok. Tek farkı, parantez içerisinde
başa yazdığımız "self" parametremiz ve bu parametreyi kullanmamız.
"""
#------------------------------------------------------------------------------