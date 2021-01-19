#Author : Taha Çinkılıç
#Subject : Kalıtım(Inheritance) (2)
#------------------------------------------------------------------------------
#Kalıtım(Inheritance)'ı anlama:
class çalışan():
    def __init__(self , isim , soyisim , numara , maaş , departman):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maaş = maaş
        self.departman = departman
    def bilgilerigöster(self):
        print(f"İsim = {self.isim}\nSoyisim = {self.soyisim}\nNumara = {self.numara}\nMaaş = {self.maaş}\nDepartman = {self.departman}\n")
    def zamyap(self , zam):
        self.maaş += zam
class yönetici(çalışan): #Çalışan sınıfından miras aldık.
    def departmandeğiş(self , dep):
        self.departman = dep
yönetici1 = yönetici("Taha" , "Çinkılıç" , 12345 , 6500 , "Yazılım")
yönetici1.bilgilerigöster() #"bilgilerigöster" metodumuzu kullandık.
yönetici1.departmandeğiş("IT") #"departmandeğiş" metodumuzu kullandık.
yönetici1.bilgilerigöster() #"bilgilerigöster" metodumuzu kullandık.
"""
Gödüğünüz gibi, yönetici sınıfını oluştururken çalışan sınıfından miras aldık.
Yönetici sınıfı için, çalışan sınıfındaki tüm özellikleri miras aldıktan sonra
bir de "departmandeğiş" adlı metodumuzu tanımladık ve sorunsuz bir şekilde ça-
lıştı.
"""
#------------------------------------------------------------------------------