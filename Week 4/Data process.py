#Data Process#

liste = [1,2,3,4,5]
# list tanimlarken kapali parantez kullanmalisin

print(liste)
print(liste[4])
print(type(liste))

liste[3] = 67
print(liste)
#burada 3. indistindeki sayiyi 67ye cevirdim.

alt_liste = liste[2:4]
print(alt_liste)

#### Tuple ####
tuple = (10,20,30,40)
print(tuple)
print(tuple[1])

#tuple[1] = 50
#print(tuple)
#bu kod hata verir.

alt_tuple = tuple[1:4]
print(alt_tuple)

#### KUMELER (sets) #### 
kume = {100,200,300,400,500,100,100,200,100}
print(kume)
#sirasiz bir sekilde verir.ama bazen denk de gelebilir. ayni sayiyi bir kere sayar. 

print(type(kume))

kume.add(700)
print(kume)
#burada kumenin icine 700 sayiyi ekledi. ve herhangi bir siraya yerlesti.

kume.update([400,900])
print(kume)
#icindeki bir veriyi bulup guncelledi

#### Dict Dictionary (sozluk) ####

dict = {'anahtar1':'deger1','anahtar2':'deger2'}
print(dict)
deger = dict['anahtar1']
print(deger)


kume_list = list(kume)
print("kume to list",kume_list)
#kumeyi listeye gonderdik ve cikti olarak biz bir liste verdi.
print(type(kume_list))

kume_tuple = set(tuple)
print("tuple to set",kume_tuple)
#tuple kumeye cevirdin

list_keys = list(dict.keys())
print(type(list_keys))
print(list_keys)
#sozlukteki anahtarlari listeye cevirdik

list_values = list(dict.values())
print(type(list_values))
#burada sozlukteki degerler listeye cevirdik
print(list_values)

sayilar = [10,8,10,5,3,15]
en_buyuk = max(sayilar)
print(en_buyuk)
#en buyuk sayiyi gosterir,yani 15

en_kucuk = min(sayilar)
print(en_kucuk)
#en kucuk sayiyi gosterir,yani 3

sayilar.append(20)
sayilar.append(1)
#append listeye yeni deger eklerler.

yeni_en_buyuk = max(sayilar)
yeni_en_kucuk = min(sayilar)
#yeniden tanimladik cunku 20yi ve 1i ekledik.

print(yeni_en_buyuk)
print(yeni_en_kucuk)

print(sayilar)
#yeni degrlerle bersaber yazdirir.

sayilar.pop()
print(sayilar)
#burada son giren sayiyi ilk ciksr (LIFO)

sayilar.sort()
print(sayilar)
#"sort"verdigimiz ifadeleri siralar.(sayilari kucukten buyuge siraladi)

sayilar.reverse()
print(sayilar)
#"reverse" ise verdigimiz degerleri tersten siralar.(sayilari buyukten kucuge siraladi)

print(sayilar.count(10))
#burada listemdeki ne kadar "10" oldugunu saydi

aralik = range(1,100)
print(list(aralik))
#1den 100e kadar arasindaki tum sayilari yazdi

import random

rastgele_sayi = random.randint(1,100)
print("tutulan sayi",rastgele_sayi)
#1 ile 100 arasindaki sayilardan rastgele bir sayi secer.
#randint = rastgele tam sayi 



