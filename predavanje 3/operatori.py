import random


kurs = "Python Fundamentals"
print(kurs)

a = 10
b = 5

print(a + b)

rezultata_sabiranja = a + b
print(rezultata_sabiranja)

print("Oduzimanje:", a - b)
print("Mnozenje:",int(a / b))

print("Celobrojno deljenje:", a // b)
print(10 // 3)
print(10 / 3)
print(a ** 2)
print(a ** 3)
print(a % 3)
print(a % 2)
print(-a)

godine = 25
godine + 1
godine = 25 + 1
godine += 1
godine -= 5

print(godine)

godine *= 2
print(godine)

godine /= 2
print(godine)

print(int(godine))

broj1 = 15
broj2 = 20

# print("Zbir:", broj1 + broj2)

# broj1 = int(input("Unesite prvi broj: "))
# print(broj1)

# broj2 = int(input("Unesite drugi broj: "))

# print("Rezultat je: ", broj1 + broj2)

# poluprecnik = int(input("Unesite polupecnik: "))
# pi = 3.14
# povrsina = poluprecnik ** 2  * 3.14
# print("Povsina kruga je: ", povrsina)

# unos = input("Unesite nesto...")
# print(unos.isnumeric())

# broj1 = int(input("Unesite prvi broj: "))
# broj2 = int(input("Unesite drugi broj: "))
# print("Rezutat sabiranja je: ", broj1 + broj2)

# stara_kilaza = 80
# nova_kilaza = 99

# print(stara_kilaza > nova_kilaza)
# print(stara_kilaza < nova_kilaza)

# print(nova_kilaza != 100)
# print(stara_kilaza <= 80)

# username = "test"
# password = "abc123"

# print(username == "test")
# print(password == "abc123")

# godine = 20
# print(godine >= 16)

# broj = int(input("Unesite broj: "))
# provera = broj % 2
# print("Paran broj?", provera == 0)

# korisnik = int(input("Unesite broj:"))
# racunar = random.randint(1, 10)

# print("Korisnik:", korisnik)
# print("Racunar:", racunar)
# print("Pogodak:", korisnik == racunar)


automobil = 0
cilj = 50

print(automobil >= cilj)
automobil += 10
print(automobil >= cilj)
automobil += 20
print(automobil >= cilj)
automobil += 20
print(automobil >= cilj)

provera_imena = True  # ime == sacuvano_ime
provera_sifre = False  #  sifra == sacuvana_sifra

print(provera_imena and provera_sifre)

lepo_vreme = False
print(not lepo_vreme)

kurs = input("Unesite ime kursa: ")
generacija = int(input("Generacija: "))

odobreno = kurs == "python" and generacija == 2022
print(odobreno)








