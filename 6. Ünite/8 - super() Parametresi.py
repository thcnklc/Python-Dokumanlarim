#Author : Taha Çinkılıç
#Subject : super() Parametresi
#------------------------------------------------------------------------------
#super() parametresini anlama:
"""
super() parametresi, override ettiğimiz bir metodun içinde aynı zamanda miras
aldığımız bir metodu kullanmak istersek kullanılabilir. Yani super() parametresi;
miras aldığımız sınıfın metodları içerisindeki değişkenleri, alt sınıflardaki me-
todlarda da kullanmamızı sağlar.
"""
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
    def __init__(self , isim , soyisim , numara , maaş , departman , yaş):
        super().__init__(isim , soyisim , numara , maaş , departman)
        #Miras aldığımız sınıfın değişkenlerini bu yol ile tanımladık.
        self.yaş = yaş #Yeni bir değişken ekledik.
    def departmandeğiş(self , dep):
        self.departman = dep
    def bilgilerigöster(self): #"bilgilerigöster" metodunu override ettik.
        print(f"İsim = {self.isim}\nSoyisim = {self.soyisim}\nNumara = {self.numara}\nMaaş = {self.maaş}\nDepartman = {self.departman}\nYaş = {self.yaş}\n")
yönetici1 = yönetici("Taha" , "Çinkılıç" , 12345 , 6500 , "Yazılım" , 21)
yönetici1.zamyap(500) #Çalışan sınıfımızdaki fonksiyonu kullandık.
yönetici1.bilgilerigöster() #"bilgilerigöster" metodumuzu kullandık.
#------------------------------------------------------------------------------