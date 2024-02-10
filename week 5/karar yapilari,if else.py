#KARAR YAPILARI
"""
a = 90
b = "SiberVatan"

num1,num2,num3 = 5,55,65
print("sayilar",num1,num2,num3)

num1=num1 + 50
num2=num2 + 55
num3=num3 + 90

num1+=num2
num1/=num2
"""
"""
numbers=(50,55,65)
print(type(numbers))
#type'i tuple
num1,num2,num3,=numbers
#num4'u print etmek istesek hata verir.

print(num2)


a,b,c,d = 50,100,50,75

print(a < b)
print(str(a < b))
#ikisininde cevaplari true

print(int(a<b))
#cevabi 1 olur .


sonuc=(a>b)
print(sonuc)
#false

sonuc=(a==c)
print(sonuc)
#true

sonuc= (a>d)
print(sonuc)
#false

sonuc=(a!=c)
print(sonuc)
#false

username1 = "ceku"
username2 = "arif"


print("A.R.O.G.'a hosgeldiniz.\n")
username_input = input("bir kullanici adi giriniz")


sonuc= (username1==username_input)
print("Eslesme sonucu:",sonuc)

sonuc= (username2==username_input)
print("Eslesme sonucu:",sonuc)

#string verileri karsilastirdik burda

sonuc= (username1.lower()==username_input.lower())
sonuc2= (username2.lower()==username_input.lower())
sonuc3 = (sonuc!=sonuc2)

print("Eslesme sonucu:",sonuc3)
"""
"""
#kullanicidan alinan email vesifrenin onceden tanimlanmis sozluk icerisinde bulunup bulunmadigini bulan ve bunu ekrana yazdiran programi.

users={
    "garavel.usta@gora.com.tr":"garavel123",
    "216.robot@gora.com.tr":"robot123" 
}

print("*-*-*-A.R.O.G portalina hosgeldinix*-*-*-*\n")
print("lutfen bilgilerinizi giriniz")

input_mail= input("mail giriniz:")
input_sifre= input("sifre giriniz:")

sonuc_mail=(input_mail in users.keys())
sonuc_sifre=(input_sifre in users.values())

sonuc_final=(int(sonuc_mail)+int(sonuc_sifre)==2)

print("eslesme durumu:",sonuc_final)


fruits=['elma','muz','portakal','kivi']

#(<birsey> <operator> <bisey>)
print("kiraz"in fruits )
#burda find yerine in kullandik. find daha uzun listelerde kullanilir.

x=y=[10,20,30]
z=[10,20,30]

print(x is y)
print(x is z)
print(x == z)
#is karsilastirma operatorudur.degiskenlerin adreslerini karsilastiriyoruz
#== ise icindeki degerler ayni mi diye karsilastiriyor.

#kullanicidan bir vize %40 ve bir final %60 notu alip ortalamasi 50den yuksekse gecti(TRUE/FALSE) yazdir
#ortalama = vize*0.4 + final*0.6   ,  ortalama>50
'''
vize_input = ("vize notunuz giriniz:")
final_input = ("final notunuzu giriniz:")

vize_ort = vize_input*0.4
final_ort = final_input*0.6

sonuc = (vize_ort+final_ort)

print(sonuc)
'''

#girilen bir sayinin pozitif cift sayi oldugu durumda ekrana true, tek sayi olma durumunda false yazdiran programi yaz
 
girilen_sayi = int(input('sayi:'))
result = (girilen_sayi>0 ) or (girilen_sayi%2 ==0)
print("sonuc:" + str(result))

#KOSULLAR
'''
if(): 
    #<eger kosul dogru(True) ise calisacak kodlar>
elif():
    #eger ikiside olmadiysa
else:
    #<eger kosul yanlis(False)ise calisacak kodlar> 
    
'''

x= 98
y=23
if(x>y):
    print("en buyuk sayi:",x)
elif(x==y):
    print("sayilar esittir")
else:
    print("en buyuk sayi:",y)


kullanici_takim = input("takim adi giriniz")

if kullanici_takim == "Galatasaray":
    print("en sevdiginiz renkler: sari ve kirmizi")
elif kullanici_takim == "Fenerbahce":
    print("sen sevdiginiz renkler: sari ve lacivert")
elif kullanici_takim == "Besiktas":
    print("en sevdiginiz renkler:siyah ve beyaz")
elif kullanici_takim == "Kardemir Karabuk Spor":
    print("en sevdiginiz renkler:bordo ve lacivert")
else:
"""

#kullanicidan alinan kullanici adi ve sifre bilgilerini kntrol eden ve ekrana bilgi yazan programi yaz.

usernameinput=input("kullanici adi giriniz:")
sifreinput= input("sifre giriniz:")
username = "faten"
sifre = "faten123"

if usernameinput =="faten" and sifreinput == "faten123":
    print("giris basarili")
elif usernameinput == "faten" and sifreinput != "faten123":
    print("sifre hatali")
elif usernameinput != "faten " and sifreinput != "faten123":
    print("her ikiside hatali") 
 
 #yanlis olana yere != koy
 










