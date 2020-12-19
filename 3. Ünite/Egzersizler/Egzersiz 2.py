#Author : Taha Çinkılıç
#Subject : Faktoriyel Bulma
#------------------------------------------------------------------------------
sayı = int(input("Faktöriyelini almak istediğiniz sayıyı giriniz : "))
faktoriyel = 1
if sayı == 0 or sayı == 1:
    print(f"{sayı}! = {faktoriyel}")
else:
    for i in list(range(1, sayı + 1)):
        faktoriyel *= i
    print(f"{sayı}! = {faktoriyel}")
#------------------------------------------------------------------------------