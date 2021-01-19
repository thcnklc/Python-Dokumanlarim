#Author : Taha Çinkılıç
#Subject : Özel Metodlar
#------------------------------------------------------------------------------
#Metodları tanımlama:
class kitap():
    def __init__(self , isim , yazar , sayfa , tür):
        self.isim = isim
        self.yazar = yazar
        self.sayfa = sayfa
        self.tür = tür
    def __str__(self):
        #print(f"İsim = {self.isim}\nYazar = {self.yazar}\nSayfa = {self.sayfa}\nTür = {self.tür}")
        #Eğer yukarıda görünen kodu yazmış olsaydık, özellikle fonksiyonu çağırmamız gerekirdi.
        return f"İsim = {self.isim}\nYazar = {self.yazar}\nSayfa = {self.sayfa}\nTür = {self.tür}"
    def __len__(self):
        # print(self.sayfa)
        # Eğer yukarıda görünen kodu yazmış olsaydık, özellikle fonksiyonu çağırmamız gerekirdi.
        return self.sayfa
    def __del__(self):
        print("Kitap siliniyor...")
kitap1 = kitap("İrade Terbiyesi" , "Jules Layot" , 208 , "Kişisel Gelişim")
print(kitap1)
print(len(kitap1))
del kitap1
"""
Pythonda normalde kullandığımız fonksiyonları, oluşturduğumuz sınıflar için baş-
tan tanımlayabiliyoruz. Böylelikle yazdığımız sınıf aracılığı ile oluşturduğu-
muz objeler üzerinde fonksiyonların işlevlerini düzenleyebiliyoruz.
"""
#------------------------------------------------------------------------------