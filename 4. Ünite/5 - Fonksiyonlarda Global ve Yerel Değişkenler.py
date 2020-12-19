#Author : Taha Çinkılıç
#Subject : Fonksiyonlarda Global ve Yerel Değişkenler
#------------------------------------------------------------------------------
#Global ve yerel değişkenleri anlama:
a = 10
def yaz():
    a = 2
    print(a)
yaz()
print(a)
"""
Fonksiyonumuzun içinde olmadan "a" isimli bir değişken tanımladık ve değer olarak
"10" verdik. Fonksiyonumuzun içerisinde de  aynı isimde bir değişken tanımladık ve
ona da "2" değerini verdik. Fonskiyonumuzu çağırdığımız zaman içerisinde bulunan
"a" değişkenini baz aldı ve o değişkenin değerini bize çıktı olarak verdi. Fakat
fonksiyonumuzun dışında, programımızın bize "a" değişkeninin değerini yazmasını
istediğimiz zaman ise bize globalde tanımladığımız "a" değişkenimizin değerini çık-
tı olarak verdi. Bunun sebebi, globaldeki değerleri fonksiyon içerisinde kullanabi-
liyor olmamız, globalde olmayan bir değişkeni globalde kullanamıyor olmamızdır. Eğer
fonksiyonumuzun içerisinde "a" değişkenini yeniden tanımlayıp herhangi bir değer
vermeseydik, çıktımız globaldeki değişkenin değeri olacaktı. Local değişkenşer sa-
dece fonksiyonlara ve sınıflara özgüdür. If, else, for, while gibi bloklar içerisin-
de de global değişkenler tanımlanabilir.
"""
b = 5
def yaz1():
    global b
    b = 2
    return b
print(yaz1())
print(b)
"""
Fonksiyonumuzun içinde olmadan "b" isimli bir değişken tanımladık ve değer olarak
"5" verdik. Fakat bu sefer globaldeki bu değeri, "global" ifadesi kullanarak fonk-
siyonumuzun içerisine dahil ettik. Fonksiyonumuz sonuca ulaştığında "b" değişkeni-
mizin değeri fonksiyonumuzun içerisinde neye eşit olursa, globalde de o değere e-
şit olacak.
"""
#------------------------------------------------------------------------------