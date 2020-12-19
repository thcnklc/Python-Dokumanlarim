#Author : Taha Çinkılıç
#Subject : Basit Hesap Makinesi
#------------------------------------------------------------------------------
print("""
*********************************
    HESAP MAKİNESİ PROGRAMI
İşlemler:
1 - Toplama
2 - Çıkarma
3 - Çarpma
4 - Bölme
*********************************
""")
a = float(input("Birinci sayı ="))
b = float(input("İkinci sayı ="))
c = input("Yapmak istediğiniz işlem =")
if c == "1":
    print("{1} + {0} = {2}".format(a , b , a + b))
elif c == "2":
    print("{} + {} = {}".format(a , b , a - b))
elif c == "3":
    print("{} + {} = {}".format(a , b , a * b))
elif c == "4":
    print("{} + {} = {}".format(a , b , a / b))
else:
    print("Lütfen geçerli bir işlen seçiniz.")
#------------------------------------------------------------------------------