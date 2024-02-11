#Kullanıcıdan bir cümle alın, cümlenin başındaki ve sonundaki boşlukları kaldırın, ardından tüm harfleri küçük harfe çevirin.
user_input=input("Lütfen bir cumle Giriniz:")
user_input=user_input.strip()
user_input=user_input.lower()
print(user_input)

#Bir string içinde belirli bir karakterin kaç kez geçtiğini sayın.
str1 = "arkadasimla sinemaya gittim"
str_count=str1.count("a")
print(str_count)

#Kullanıcıdan bir kelime ve bir harf alın, kelimenin içindeki o harfi kaç kez içerdiğini kontrol edin.
user_input1=input("Lütfen bir kelime Giriniz:")
user_input2=input("Lütfen bir harf Giriniz:")
strg=user_input1
str_count=strg.count(user_input2)
print(str_count)

#İki string'i birleştirin ve ardından bir substring arayın ve konumunu bulun.
ad= "faten"
soyad= "habbal "
karsilama= "benim adim " + ad + " soyadim " +soyad
print(karsilama)
print(karsilama[3])
karsilama_find =karsilama.find(karsilama[3])
print(karsilama_find)

#Kullanıcıdan bir cümle alın ve cümlenin içindeki kelimeleri alfabetik sıraya göre sıralayın.
user_input1=input("Lütfen cümle Giriniz:")
user_input1_split=user_input1.split()
user_input1=[(user_input1_split)]
user_input1_split.sort()
print(user_input1_split)

#Kullanıcıdan iki string alın, bu stringleri birleştirin ve tüm karakterleri küçük harfe çevirin.
user_input1=input("Lütfen kelime1 Giriniz:")
user_input2=input("Lütfen kelime2 Giriniz:")
birlesikstr= user_input1 + user_input2
birlesikstr=birlesikstr.lower()
print(birlesikstr)

#7. soruyu yapamadim

#Kullanıcıdan bir kelime alın ve kelimenin içindeki tüm 'a' harflerini '@' ile değiştirin.
user_input1=input("Lütfen kelime Giriniz:")
user_input1_replace=user_input1.replace("a","@")
print(user_input1_replace)

#Kullanıcıdan bir kelime alın ve kelimenin palindrome (tersinden de okunduğunda aynı olan) olup olmadığını kontrol edin.
kelime=input("Lütfen kelime Giriniz:")
kelimenintersi=kelime[::-1]
print("girilen kelimenin tersi = %s " % (kelimenintersi))
if kelimenintersi == kelime :
    print("girilen kelime palindrom")
else:
    print("girilen kelime palindrom değil")

#Kullanıcıdan bir cümle alın, cümlede geçen kelimelerin içinde en uzun olanını bulun.
cümle=input("Lütfen cümle Giriniz:")
kelimelerayir = cümle.split()
enuzunkelime= max(kelimelerayir,key=len) 
print(enuzunkelime)

#Bir liste oluşturun ve listenin ortasındaki elemanı bulun.
liste=[1,2,3,4,5,]
listeninuzunluğu = len(liste)
ortadakieleman = listeninuzunluğu // 2  
print("listenin ortadaki eleman:",ortadakieleman)

#Bir tuple oluşturun, tuplein 2. ve 4. elemanlarını yeni bir tuple olarak alın.
tuple=(20,30,40,50,60,70)
yenituple= (tuple[1],tuple[3]) 
print(yenituple)

#Bir set oluşturun, set içine bir sayı ekleyin, ardından bu sayıyı setden çıkarın.
#kumeler(sets)
kume={100,200,300,400,500}
eklenensayi=700
kume.add(eklenensayi) 
print(kume) 
kume.remove(eklenensayi)

#Bir dictk oluşturun, dicte yeni bir anahtar-değer çifti ekleyin, ardından bir anahtarı silin.
dict={"anahtar1":"deger1","anahtar2":"deger2"}
yenianahtar= "anahtar3"
yenideger= "deger3"
dict[yenianahtar] = yenideger 
silincekanahtar = 'anahtar2'
del dict[silincekanahtar] 
print(dict)

#Bir liste oluşturun, listenin ortasına yeni bir sayı ekleyin.
liste =[1,2,3,4,5]
listeninuzunluğu = len(liste)
eklenceksayi = 7
ortadakieleman = len(liste) // 2 
liste.insert(ortadakieleman,eklenceksayi) 
print("yeni Liste:",liste)

#Bir liste oluşturun ve listenin ortasındaki elemanı bir tuplee ekleyin.
liste=[1,2,3,4,5,6]
tuple=(10,20,30)
listeninuzunluğu = len(liste)
ortadakieleman = listeninuzunluğu // 2  
yenituple=tuple + (ortadakieleman,) 
print(yenituple)

#Bir set oluşturun ve setin elemanlarını içeren bir liste oluşturun, ardından bu liste elemanlarının toplamını hesaplayın.
kume={100,200,300,400,500,}
kume_list=list(kume)
print("kume to list",kume_list)
listeelemantoplam = sum(kume_list) 
print("liste elemanlarinin toplami:",listeelemantoplam)

#Bir liste oluşturun ve listenin içindeki en büyük sayıyı bulun, ancak sadece aritmetik operatörler (+, -, *, /) kullanmadan yapın.
liste = [1,2,3,4,5]
enbuyuksayi = max(liste)
print("listedeki en buyuk sayi:", enbuyuksayi)

