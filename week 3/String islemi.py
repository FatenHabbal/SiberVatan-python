#STRING ISLEMLERI

ad = "faten"
soyad = "habbal "
yas=13

print("benim adim",ad,soyad,"yasim",yas,"hosgeldin")
#sonuc=benim adim faten habbal yasim 13

karsilama = '  benim adim ' + ad + '' + soyad + '' + 'yasim ' + str(yas) + ' hosgeldin '
print(karsilama)
#burada sayiyi str fonksiyonun icine alip int bir deger cevirdik
 

#ad = "faten"
#soyad = "habbal"
#yas= "13"
#karsilama = ' benim adim ' + ad + ' ' + soyad + ' ' + 'yasim ' + yas + ' hosgeldin '
#print(karsilama)
 #burada ise yine ayni islem sadece yasi direkt int bir deger olarak girdik 



#uzunluk = len(karsilama)
#print(uzunluk)

print(karsilama[3])
#bir cogu yazilim dilinde 1den baslar. ama pythonda 0dan basliyor. indisteki sayilar koseli parantez icinde yazilir.

print(karsilama[-2])
#sayinin yaninda - koyarak sondaki karakterleri sayar.

print(karsilama[4:10])
#iki nokta aralik degeri verir. mesela burada 4ten baslayip 10a kadar indisleri saydi(10 dahil olmadan)

print(karsilama[0:10])
#sonuc= benim adim 

print(karsilama[:24])
#buarada baslangic onemli degil ama 24e kadar saysin.

print(karsilama[11:])
#buarada ise 10.dan baslayip sonuna kadar saydi.

print(karsilama[2:25:3])
#2den baslayip 25e kadar,her 3ten bir tanesi verir.
print(karsilama[:-4])
#0dan baslayip son 3unu alma 

print(karsilama[::-1])
#karakterlerin hepsini sagdan sola dizdi.yani tersten yaziyor.


#########

karsilama_upper = karsilama.upper()
print(karsilama_upper)
#tum yaziyi buyuk harflerle yazar.

karsilama_lower = karsilama.lower()
print(karsilama_lower)
#butun yaziyi kucuk harflerle yazar.

karsilama_strip = karsilama.strip()
print(karsilama_strip)
#burada yazdigimiz bosluklari silip en sade halini verir

karsilama_split = karsilama.split()
print (karsilama_split)
#her ifadeyi ayri ayri cikarir.['benim', 'adim', 'faten', 'habbal', 'yasim', '13', 'hosgeldin']
print(karsilama_split[-2])
#burada usteki kodun ifadelerinin sondan ikinciyi verir.

karsilama_join = "-".join(karsilama)
print(karsilama_join)
#tum harflerin(ifadelerin) arasinda - isareti gelir

karsilama_find = karsilama.find("faten")
print(karsilama_find)
#burada istedigimiz degeri aratabilirz.Mesela faten ismi 13. indisten basliyor

karsilama_startswith = karsilama.startswith(" ")
print(karsilama_startswith)
#benim ifadem bosluk ile basliyor mu? Ture 

karsilama_endswith = karsilama.endswith("Z")
print(karsilama_endswith)
#benim ifadem Z ile mi bitiyormu ? False

karsilama_replace = karsilama.replace("faten","maism ")
print(karsilama_replace)
#faten ismini yerine maism ismini yazdirmak istiyorsam.







