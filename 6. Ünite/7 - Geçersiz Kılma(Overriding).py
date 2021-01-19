#Author : Taha Çinkılıç
#Subject : Geçersiz Kılma(Overriding)
#------------------------------------------------------------------------------
#Geçersiz Kılma(Overriding)'yı anlama:
"""
Eğer miras aldığımız bir classın metodlarını; aynı isimle kendi sınıfımızda tek-
rar tanımlarsak , artık metodu çağırdığımız zaman miras aldığımız değil kendi
metodumuz çalışacaktır. Bu olaya "Overriding" yani "Geçersiz Kılma" denmektedir.
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
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maaş = maaş
        self.departman = departman
        self.yaş = yaş #Yeni bir değişken ekledik.
    def departmandeğiş(self , dep):
        self.departman = dep
yönetici1 = yönetici("Taha" , "Çinkılıç" , 12345 , 6500 , "Yazılım" , 21)
yönetici1.bilgilerigöster() #"bilgilerigöster" metodumuzu kullandık.
"""
Farkettiyseniz "bilgilerigöster" fonksiyonumuz "çalışan" adlı sınıfımızdan aldı-
ğımız bir metod idi. Metodumuzu incelediğimiz zaman "yaş" değişkeninin değerinin 
yazdırılmadığını görüyoruz. Bu metod üzerinde oynayarak "yaş" değişkeninin değe-
rini yazdırmaya kalkarsak hata alırız. Yönetici sınıfımızı oluştururken çalışan
sınıfımızdan miras aldığımız için, yönetici sınıfımızdaki herhangi bir değişken,
çalışan sınıfımızda var olmayacak. Fakat çalışan sınıfımızdaki tüm değişkenler ve
metodlar aynı zamanda yönetici sınıfında da kullanılabilir durumdalar.
"""
#------------------------------------------------------------------------------