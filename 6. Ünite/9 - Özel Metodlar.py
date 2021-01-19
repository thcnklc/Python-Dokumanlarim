#Author : Taha Çinkılıç
#Subject : Özel Metodlar
#------------------------------------------------------------------------------
#Metodları tanımlama:
"""
Özel metodlar, bizim özel olarak çağırmadığımız ancak her classa ait metodlar-
dır. Bunların çoğu biz tanımlamasak bile Python tarafından varsayılan olarak ta-
nımlanır. Bu metodların bazılarını da özel olarak bizim tanımlamamız gerekmekte-
dir. "__init__" metodu bu metodlara örnektir.
"""
class kitap():
    pass
kitap1 = kitap() #"__init__" metodunu çağırdık.
"""
print(len(kitap1))
Bu komutu çalıştırmak istediğimiz zaman bir hata ile karşılaşırız. Bunun nedeni,
"__len__" metodunu çağırıyor olmamızdan kaynaklanıyor. Bu metodu bizim tanımla-
mamız gerekiyor. Python'ın default olarak tanımladığı bir metod değil.
"""
print(kitap1) #"__str__" metodumuzu çağırdık.
del kitap1 #"__del__" metodumuzu çağırarak "kitap1" objemizi sildik.
#------------------------------------------------------------------------------