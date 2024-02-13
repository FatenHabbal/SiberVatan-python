#1)Bir fonksiyon oluşturun. Emeklilik yaşını 65 olarak belirleyin. Kullanıcıdan yaşını alıp 65 yaş altındakilere emekliliğine kaç yıl kaldığını,65 yaş üstüne zaten emekli olduğunu ekrana yazdırın.


def emeklihesap(yas):
    emekliyasi = 65
    emekliyil = emekliyasi - yas
    
    if yas < emekliyasi:
        print("Emekliliğinize", emekliyil, "yil kaldi.")
    else:
        print("Zaten emekli oldunuz.")

yas = int(input("yasinizi girin lutfen: "))
emeklihesap(yas)

#2)Bir fonksiyon oluşturun.Fonksiyon kullanıcıdan iki sayı alıp bu iki sayı arasındaki asal sayıları ekrana bastırın.


def asalsayilar(sayi1, sayi2):
    asal_sayilar = []

    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i) == 0:
                    break
            else:
                asal_sayilar.append(sayi)

    if len(asal_sayilar) > 0:
        print("bu iki sayinin arasindaki asal sayilar:", ", ".join(map(str, asal_sayilar)))
    else:
        print("girilen sayilarin arasinda asal sayi yoktur.")

sayi1 = int(input("1. sayiyi girin lutfen: "))
sayi2 = int(input("2. sayiyi girin lutfen: "))

asalsayilar(sayi1, sayi2)

#Burada ChatGPTden yardim aldim.


#3)İki fonksiyon oluşturun. İki fonksiyon içinde de listeler olsun ilk fonksiyon içindeki listenin en büyük sayısını ikinci fonksiyon içindekilistenin en küçük sayısını toplayıp ekrana bastırın.


def enbuyuksayi(liste):
    return max(liste)

def enkucuksayi(liste):
    return min(liste)

liste1 = [10, 15, 20]
liste2 = [5, 100, 250]
en_buyuk = enbuyuksayi(liste1)
en_kucuk = enkucuksayi(liste2)

print(en_buyuk + en_kucuk)

#4)Bir fonksiyon oluşturun. Fonksiyon içinde bir tane liste olsun ve bu listenin ilk ve son sayısı eşitse ekrana true değilse false yazdırsın.

#Bu soruda da ChatGPTden baktim ama mantigini anl;amadigim icin yazmadim.

#5)Bir sayının palindrom sayı olup olmadığını kontrol eden fonksiyonu yazınız.


def palindrom(sayi):
    sayi_str = str(sayi)
    tersi_str = sayi_str[::-1]

    if sayi_str == tersi_str:
        return True
    else:
        return False

def palindrom_kontrol(sayi):
    if palindrom(sayi):
        print(sayi, "bu sayi bir palindrom sayisidirr")
    else:
        print(sayi, "bu sayi bir palindrom sayi degildir")

palindrom_kontrol(525)
palindrom_kontrol(124)

#6)Bir fonksiyon oluşturun. Fonksiyon içinde iki liste olsun ilk listenin çift sayılarını ikinci listenin tek sayılarını alıp yeni bir listeye ekleyin ve ekrana yazdırın.


def cift_teksayibirlesik(liste1, liste2):
    yeni_liste = []

    for num in liste1:
        if num %2 == 0:
            yeni_liste.append(num)

    for num in liste2:
        if num % 2 != 0:
            yeni_liste.append(num)

    return yeni_liste


#7)Rus ruleti oyunu yazın. Random kütüphanesi kullanarak 1-6 arasında bir sayı seçilsin ve kullanıcıdan bir sayı alsın eşit olduğunda oyun biter.

import random

def rastgelesayi():
    return random.randint(1, 6)

def rus_ruleti():
    rastgele_sayi = rastgelesayi()
    tahmin = int(input("tahmininizi girin (1 ile 6 arasinda bir sayi girin): "))

    if tahmin == rastgele_sayi:
        print("You're ALIVE!")
    else:
        print("You're DEAD!")

rus_ruleti()

#importing random ve randint ChatGPTden baktim.
