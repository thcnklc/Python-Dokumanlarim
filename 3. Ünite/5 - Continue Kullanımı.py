#Author : Taha Çinkılıç
#Subject : Continue Kullanımı
#------------------------------------------------------------------------------
#"continue" ifadesi sadece döngülerde kullanılır.
#For döngüsünde "continue" kullanma:
liste1 = ["a" , "b" , 1 , "c" , 2 , 3]
for i in liste1:
    if (i == "b" or i == 2):
        continue
    print(i)
"""
Yazdığımız yazılım, listemizin içerisinde "b" veya "2" değerlerini gördüğünde
"if" bloğumuzu karşılamış oluyor. "if" bloğumuzda konut olarak sadece "continue"
var. "continue" komutu, döngüyü en başa gönderir ve diğer satırlara bakmaksızın
döngüye devam eder.
"""
#------------------------------------------------------------------------------
#While döngüsünde "continue" kullanma:
i = 0
while(i < 10):
    if i == 2:
        i += 1
        continue
    print(i)
    i += 1
"""
Döngümüzdeki "if" bloğunda eğer biz "i" değişkenimizin değerini 1 artırmasaydık
sonsuz bir döngüye girerdik. Hatırlarsınız ki Python'da kodlar yukarıdan aşağı
sırasıyla okunur ve çalıştırılırdı. Biz bu döngümüzü çalıştırdığımız zaman eğer
"i" değişkenimizin değeri "2" ise, if bloğumuzun koşulu sağlanmış oluyor. Fakat
"i" değişkenimizin değeri sabit kalıyor. Bu sebeple de sürekli if bloğumuzdaki
koşul sağlanmış oluyor ve yazılımımız sonsuz döngüye giriyor. Bu yüzden if
bloğumuzun içinde de "i" değişkenimizin değerini 1 artırdık ki, döngümüz sonsuz
olmasın.
"""
#------------------------------------------------------------------------------