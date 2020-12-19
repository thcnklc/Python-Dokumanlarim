#Author : Taha Çinkılıç
#Subject : Kullanıcı Girişi
#------------------------------------------------------------------------------
kullanıcı_adı = "thcnklc"
parola = "12345"
a = input("Kullanıcı adı =")
b = input("Parola =")
if (kullanıcı_adı != a and parola == b):
    print("Kullanıcı adı hatalı.")
elif (kullanıcı_adı == a and parola != b):
    print("Parola hatalı.")
elif(kullanıcı_adı != a and parola != b):
    print("Kullanıcı adı ve parola hatalı.")
else:
    print("Başarıyla giriş yapıldı.")
# ------------------------------------------------------------------------------