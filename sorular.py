### SORU: girilen kullanıcı ismine göre ekrana "merhaba kullancı" yazdıran pyhton kodunu yazınız.

user_name = "ekinksy"

print("------GİRİŞ PANELİ------")

kullanici_adi = str(input("Lütfen kullanıcı adınız girin: "))

if user_name == kullanici_adi:
    print("Merhaba kullanıcı !")
else:
    print("Sistamde kaydınız bulunmamaktadır !")


### SORU: Klavyeden girilen iki sayıyı toplayan ve sonucu ekrana yazdıran python kodunu yazınız.

sayi1 = int(input("Lütfen il sayıyı girin: "))
sayi2 = int(input("Lütfen ikinci sayıyı girin: "))

print(sayi1 + sayi2)


### SORU: Klavyeden girilen iki sayının ortalamasını bulan ve sonucu ekrana yazdıran python kodunu yazınız.

sayi1 = int(input("İlk sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

print((sayi1 + sayi2) / 2)


### SORU: Klavyeden girilen vize ve final notuna göre ;
# vizenin ½40'ını ve finalin %60'ını alan ve sonucu ekrana yazdıran python kodunu yazın.

vize = int(input("Vize notunuz girin: "))
final = int(input("Final notunuzu girin: "))

print(((vize * 40) / 100) + ((final * 60) / 100))


### SORU: Klavyeden girilen 3 yazılı notunun ortalamsını bulan ve ekrana yazdıran
# python kodunu yazın.

yazili1 = int(input("İlk yazılı notunuzu girin: "))
yazili2 = int(input("İkinci yazılı notunuzu girin: "))
yazili3 = int(input("Üçüncü yazılı notunuzu girin: "))

print((yazili1 + yazili2 + yazili3) / 3)


### SORU: Bir dersin ortalaması girilen öğrencinin o dersten geçip geçmediğini
# gösteren python kodunu yazın. (50 ve üzeri geçer.)

sinav1 = int(input("İlk sınav notunuzu girin: "))
sinav2 = int(input("İkinci sınav notunuzu girin: "))
ortalama = (sinav1 + sinav2) / 2

if ortalama == 50 or ortalama > 50:
    print("Dersten geçtiniz !")
elif ortalama < 50:
    print("Dersten kaldınız !")
else:
    print("Yanlış değer !")


### SORU: Klavyeden girilen sayının tek mi çift mi olduğunu yazdıran python kodunu yazın.

klavyeden = int(input("Lütfen bir değer girin: "))

if klavyeden % 2 == 0:
    print("Sayı çift !")
elif klavyeden % 2 == 1:
    print("Sayı tek !")


### SORU: Klavyeden girilen değerin pozitif mi negatif mi yoksa 0 mı olduğunu
# yazdıran python kodunuz yazın.

sayi = float(input("Lütfen bir sayı girin: "))

if sayi == 0:
    print("Girdiğiniz sayı 0 !")
elif sayi > 0:
    print("Pozitif bir değer girdiniz !")
elif sayi < 0:
    print("Negatif bir değer girdiniz !")


### SORU: Kullanıcının, klavyeden girilen yaşa göre ehliyet alıp alamayacağını
# yazdıran python kodunu yazın.

yas = int(input("Yaşınızı girin: "))

if yas >= 18:
    print("Ehliyet alabilirsiniz !")
elif yas < 18:
    print("Ehliyet için gerekli yaş şartını sağlamıyorsunuz !")


### SORU: 1'den 10'a kadar olan sayıları alt alta yazdıran python kodunu yazın.

for i in range(1,11):
    print(i)


### SORU: 1' den 20'ye kadar olan çift sayıları alt alta yazdıran python kodunu yazın.

for i in range(1,21):
    if i % 2 == 0:
        print(i)


### SORU: 1'den 20'ye kadar olan tek sayıları alt alta yazdıran python kodunu yazın.

for i in range(1,21):
    if i % 2 == 1:
        print(i)


### SORU: Klavyeden kısa kenar uzunluğu ve uzun kenar uzunluğu girilen dikdörtgenin
# alan ve çevresini hesaplayan python kodunu yazınız.

dikdortgen_kisakenar = int(input("Dikdörtgenin kısa kenar uzunluğunu girin: "))
dikdortgen_uzunkenar = int(input("Dikdörtgenin uzun kenar uzunluğunu girin: "))

alan = dikdortgen_kisakenar * dikdortgen_uzunkenar
cevre = (dikdortgen_kisakenar * 2) + (dikdortgen_uzunkenar * 2)

print(alan)
print(cevre)


### SORU: Kullanıcı adı ve şifre giren kişinin sistemde kaydı var hoş geldiniz yazsın.

db = {"username":"ekinaksoy","password":"1235689"}
username = input("Kullanıcı adı girin: ")
password = input("Parola girin: ")

if username == db["username"] and password == db["password"]:
    print("Hoş geldiniz!")
else:
    print("Kullanıcı adı veya parola hatalı!")


def girisekrani():
    dogrukullaniciadi = "ekinaksoy"
    dogrusifre = "1235689"

    while True:
        kullaniciad = input("Kullanıcı adı girin: ")
        sifre = input("Şifre girin: ")

        if kullaniciad == dogrukullaniciadi and sifre == dogrusifre:
            return "Hoş Geldiniz!"
        else:
            print("Hatalı kullanıcı girişi!")

sonuc = girisekrani()
print(sonuc)


### SORU: Kullanıcıdan alınan sayı negatif ise mutlak değere alıp pozitif halini yazdırın.

def mutlakdeger(sayi):
    if sayi < 0:
        sayi = -sayi
        return sayi
    else:
        print("Sayı zaten pozitif !")

sayi = float(input("Sayı girin: " ))
mutlaksayi = mutlakdeger(sayi)
print(mutlaksayi)


### SORU: Verilen sayının ve ismin elemanlarını alt alta yazdırın.

sayi = 19782

for i in str(sayi):
    print(i)

isim = "ekin"

for i in isim:
    print(i)


### SORU: Yaşı girlen kullanıcının doğum yılını yazdırın.

yas = int(input("Yaşınızı girin: "))
dogumyili = 2023 - yas

print(f"Doğum yılınız: {dogumyili}")


### SORU: Maaşa yapılan zam oranına göre zamlı maaşı yazdırın.

def hesapla(maas,zam):
    return maas + (maas * zam/100)

maas = int(input("Maaşınızı girin: "))
zam= int(input("Zam oranını girin: %"))

print(int(hesapla(maas,zam)))




























