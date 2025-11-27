
# # brojevi.sort()

# brojevi.reverse()
# print(brojevi)


brojevi = [9, 1, 3, 2, 5, 8, 7]

sortirani_brojevi = [1, 2, 3, 5, 7, 8, 9]


# while True:
#     izvrsena_zamena = False
#     for i in range(1, len(brojevi)):
#         if brojevi[i] < brojevi[i-1]:
#             privremena = brojevi[i]
#             brojevi[i] = brojevi[i-1]
#             brojevi[i-1] = privremena
#             izvrsena_zamena = True
#     if izvrsena_zamena == False:
#         break    
# print(brojevi)





# while True:
#     izvrsena_zamena = False
#     for i in range(1, len(brojevi)):
#         if brojevi[i] < brojevi[i-1]:
#             privremena = brojevi[i]
#             brojevi[i] = brojevi[i-1]
#             brojevi[i-1] = privremena
#             izvrsena_zamena = True
#     if izvrsena_zamena == False:
#         break
# print(brojevi)      






proizvodi = ["telefon","TV","Laptop"]
cene = [100,200,300]

for i in range(len(proizvodi)):
    print(proizvodi[i],cene[i])


automobili = ["Audi","BMW","Yugo","Citroen","KIA","Peugeot"]


for i in range(len(automobili)):
    if i == 3:
        print("Aleksandra vozi:", automobili[i])


proizvodi = [ ["iphone 11", "samsung s22", "xiaomi x3"],["acer", "macbook", "dell"],["ipad", "samsung galaxy tab", "xiaomi tablet"]]





telefoni = ["iphone 11", "samsung s22", "xiaomi x3"]
laptopovi = ["acer", "macbook", "dell"]
tableti = ["ipad", "samsung galaxy tab", "xiaomi tablet"]

# print(proizvodi[0][1])

# for kategorija in proizvodi:
#     for stavka in kategorija:
#         print(stavka)

for i in range(len(proizvodi)):
    print(proizvodi[i])
    for j in range(len(proizvodi[i])):
        print(proizvodi[i][j])


hrana = [  ["cokolada", "bombone","palacinke"],
           ["sarma","musaka", "kiseli kupus"],
           ["pecena paprika", "ajvar", "sopska"]
        ]

for kategorija in hrana:
    for jelo in kategorija:
        print("Naziv:", jelo)

ime = "Sofija"
poruka = f"Cao {ime} !!!"
print(poruka)


a = 10
b = 15

sabiranje = f"Sabiranje brojeva {a} i {b} je {a+b}"

# biblioteka = [["uvod u pajton", "nepoznat autor", 123],
#              ["uvod u racunare", "aleksandra lazarevic", 321]

#               ]



print("Odaberi omandu: 1 unos, 2 prikaz, 3 brisanje, > izlaz")
komanda = int(input("Unesite komandu: "))

biblioteka = []

while True:
    if komanda == 1:
        # unos knjige , preuzmi podatke
        naslov = input("Unesite naslov: ")
        autor = input("Unesite autora: ")
        isbn = int(input("Unesite isbn: "))
        biblioteka.append([naslov, autor, isbn])
        print("Dodata knjiga!")
    if komanda == 2:
        for knjiga in biblioteka:
            for detalj in knjiga:
                print(detalj)
    if komanda == 3:
        # ovde vrsim brisanje
        kljucna_rec = input("Unesite naziv knjige koju zelite da obrisem. ")
        for knjiga in biblioteka:
            # Proveravam detalje knjige
            for detalj in knjiga:
                if detalj == kljucna_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana")












