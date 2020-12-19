#Author : Taha Çinkılıç
#Subject : Geometrik Şekil Hesaplama
#------------------------------------------------------------------------------
print("""
Bir geometrik şekil seçin.
1 = Dörtgen
2 = Üçgen
""")
s = input("Seçim =")
if s == "1":
    a = int(input("Birinci kenar uzunluğu ="))
    b = int(input("İkinci kenar uzunluğu ="))
    c = int(input("Üçüncü kenar uzunluğu ="))
    d = int(input("Dördüncü kenar uzunluğu ="))
    if (a == b and c == d and a == d):
        print("Bu bir karedir.")
    elif (a == c and b == d):
        print("Bu bir dikdörtgendir.")
    else:
        print("Bu bir dörtgendir")
elif s == "2":
    a = int(input("Birinci kenar uzunluğu ="))
    b = int(input("İkinci kenar uzunluğu ="))
    c = int(input("Üçüncü kenar uzunluğu ="))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print("Bu bir eşkenar üçgendir.")
        elif ((a == b and a != c) or (a == c and a!= b) or (b == c and b != a)):
            print("Bu bir ikizkenar üçgendir.")
        else:
            print("Bu bir çeşitkenar üçgendir.")
    else:
        print("Bu bir üçgen değildir.")
else:
    print("Geçersiz şekil.")
# ------------------------------------------------------------------------------