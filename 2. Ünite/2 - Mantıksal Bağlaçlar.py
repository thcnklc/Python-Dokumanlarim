#Author : Taha Çinkılıç
#Subject : Mantıksal Bağlaçlar
#------------------------------------------------------------------------------
#And operatörü:
print(1 < 2 and "Taha" == "Taha")
"""
Yazdığımız iki koşul da True çıktığı için çıktımız da "True" olacaktır. Eğer bir
koşulumuz sağlansaydı fakat diğeri sağlanmasaydı, çıktımız "False" olacaktı. Kaç
koşul yazarsanız yazın, çıktının "True" olması için yazdığınız tüm koşulların 
"True" olması gerekiyor.
"""
print(1 > 2 and "Taha" == "ahaT")
print(1 < 2 and "Taha" == "Taha" and "İstanbul" < "Ankara")
#------------------------------------------------------------------------------
#Or operatörü:
"""
Koşullarımızın hepsi "True" ise çıktımız da "True" olacaktır. Pekçok koşul ara-
sından sadece bir tane "False" var ise, yine de çıktımız "True" olacaktır. Tüm
koşullarımız "False" ise çıktımız da "False" olacaktır. 
"""
print(1 < 2 or "Taha" == "ahaT")
print(1 > 2 or "Taha" == "ahaT")
print(1 < 2 or "Taha" == "ahaT" or "İzmir" < "Ankara")
#------------------------------------------------------------------------------
#Not operatörü:
"""
Sonucumuz eğer "True" ise çıktıyı "False", sonucumuz eğer "False" ise çıktıyı
"True" yapmamızı sağlayan operatördür.
"""
print(not 2 == 2)
"""
Normalde koşulumuz "True" çıktısını verecektir. Fakat "Not" operatörü kullandı-
ğımız için çıktımız "False" olacak.
"""
#------------------------------------------------------------------------------
#Örnekler:
print(not((2 == 2 or "Taha" > "Yavuz") and (5 <= 10)))
"""
2 rakamı 2 rakamına eşittir. Burada işlemimiz "True"dur. "Taha" stringi "T" ile
başlamakta. "T" harfi "Y" harfinden önce gelir. Bu yüzden bu işlemimiz "False".
Fakat "Or" operatörü kullandığımız için ilk parantezimiz "True" olacak. İkinci
parantezimizde ise 10 sayısının 5'ten büyük veya eşit olduğu söylenmiş. Bu ko-
şul "True"dur. Birinci parantez ile ikinci parantez arasında kullanılan opera-
tör "And" operatörüdür. İlk parantezimiz "True" idi. İkinci parantezimiz de 
"True" olduğuna göre parantezlerimizin toplamı "True"dur. Fakat parantezimizin
içinde en başta "Not" operatörü kullanıldığı için sonucumuz "True" olmasına
rağmen çıktımız "False" olacaktır.
"""
#------------------------------------------------------------------------------