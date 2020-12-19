import modul1
modul1.toplama(3 , 4 , 5)
#Oluşturduğumuz modül içerisindeki "toplama" fonksiyonumuzu kullandık.
modul1.selamla("Taha")
#Oluşturduğumuz modül içerisindeki "selamla" fonksiyonumuzu kullandık.
print(modul1.programlama_dilleri)
#Modülümüzdeki "programlama_dilleri" listemizi yazdırdık.
"""
Oluşturduğunuz modüle her yerden ulaşmak isterseniz python'ın yüklü olduğu
klasörde "Lib" klasörünün içine, yazdığınız metodu atmalısınız. Böylece
evrensel bir metodunuz olmuş oluyor.
"""
help(modul1)
#Oluşturduğumuz modül hakkında bilgi aldık.