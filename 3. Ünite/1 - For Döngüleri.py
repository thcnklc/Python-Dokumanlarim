#Author : Taha Çinkılıç
#Subject : For Döngüleri
#------------------------------------------------------------------------------
#In operatörü:
print(10 in [1 , 2 , 3 , 4 , 5])
"""
"10" sayısının bu listede olup olmadığını kontrol ettirip sonucu yazdırdık. Fakat 
listemizde "10" sayısı bulunmadığı için çıktımız "False" oldu.
"""
print(5 in [1 , 3 , 5 , 7 , 9])
"""
"5" sayısının bu listede olup olmadığını kontrol ettirip sonucu yazdırdık. Liste-
mizde "5" sayısı olduğu için çıktımız "True" oldu.
"""
print("p" in "python")
"""
"p" stringinin "python" kelimesi içinde olup olmadığını kontrol ettirdik ve sonu-
cu yazdırdık. "python" kelimesi içinde "p" harfi olduğundan dolayı çıktımız "True"
oldu.
"""
print(not "s" in "python")
"""
"not" operatörü çıktının zıttını elde etmemizi sağlayan operatördü. "python" ke-
limesi içinde "s" harfi olmadığını biliyoruz. Eğer "not" operatörünü kullanmasay-
dık çıktımız "False" olacaktı. Fakat "not" operatörünü kullandığımız için çıktı-
mız "True" oldu.
"""
#------------------------------------------------------------------------------
#For döngüsünü kullanma:
liste1 = [1 , 2 , 3 , 4 , 5]
for i in liste1:
    print(i)
#Listemiz bitene kadar tüm elemanları teker teker yazdırdık.
liste2 = [1 , 2 , 3 , 4 , 5]
toplam = 0
for i in liste2:
    toplam = toplam + i
print(toplam)
#Liste içindeki elemanları topladık.
liste3 = [1 , 2 , 3 , 4 , 5 , 17 , 26 , 74 , 35]
for i in liste3:
    if i % 2 == 0:
        print(i)
#Listedeki çift sayıları yazdırdık.
s = "python"
for i in s:
    print(i * 3)
#"Python" kelimesindeki her harfi üç ile çarparak alt alta yazdırdık.
liste3 = [(1 , 2) , (3 , 4) , (5 , 6) , (7 , 8)]
for eleman in liste3:
    print(eleman)
#Listedeki elemanları yazdırdık.
for (i , j) in liste3:
    print("i : {} <-> j : {}" .format(i , j))
"""
Listemizin içindeki demetlerde bulunan elemanları yazdırdık. Her demetimizin e-
leman sayısı aynı olduğu zaman bu yöntemi kullanabiliriz. Üç elemanlı demetleri-
miz olsaydı, "for" yazdıktan sonra üç adet değişken tanımlamalıydık. Bu döngüde-
ki "i" 0. indeksi, "j" ise "1". indeksi temsil etmektedir.
"""
for (i , j) in liste3:
    print(i * j)
#Listemizde bulunan demetlerin içindeki elemanları çarptık ve yazdırdık.
#------------------------------------------------------------------------------
#Sözlükler üzerinde gezinme:
sözlük = {"bir" : 1 , "iki" : 2 , "üç" : 3 , "dört" : 4}
for i in sözlük:
    print(i)
#Sözlük içerisindeki anahtarları yazdırdık.
for i in sözlük.values():
    print(i)
#Sözlük içerisindeki değerleri yazdırdık.
for (i , j) in sözlük.items():
    print("Anahtar : {} <-> Değer : {}" .format(i , j))
"""
".items()" metodu, sözlük içindeki değerleri listelemeye yarayan bir metoddur. 
Bu metodu kullanarak anahtarları ve değerleri ayrı ayrı yazdırdık.
"""
#------------------------------------------------------------------------------