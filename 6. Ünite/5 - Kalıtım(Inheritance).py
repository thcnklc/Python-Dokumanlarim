#Author : Taha Çinkılıç
#Subject : Kalıtım(Inheritance)
#------------------------------------------------------------------------------
#Kalıtım(Inheritance)'ı anlama:
"""
Örneğin, bir şirketin çalışanlarını tasarlamak için sınıflar oluşturuyoruz. Bu-
nun için Yönetici, Proje Direktörü, İşçi gibi sınıflar oluşturmamız gerekiyor.
Fakat bu sınıfların aslında ortak özellikleri ve metodları bulunuyor. Bu ortak
özellikleri ve metodları tekrar tekrar bu sınıfların içinde tanımlamak yerine,
bir tane ana class tanımlayıp oluşturacağımız classların bu classın özellikleri-
ni ve metodlarını almalarını sağlayabiliriz.
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
    pass #Bir bloğu daha sonra tanımlayacaksanız bu komutu kullanabilirsiniz.
"""
"yönetici" sınıfı içerisinde herhangi bir şey tanımlamadık fakat "çalışan" sı-
nıfından miras aldık. Yönetici sınıfını kullanarak oluşturduğumuz her objemiz,
çalışan sınıfındaki tüm özelliklere sahip olacak. Bir nevi miras almış olduğu-
muz class'ın kopyasını oluşturup onun üzerinde oynama yapıyoruz denebilir.
"""
#------------------------------------------------------------------------------