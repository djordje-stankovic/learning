'''
Zadatak 1 - 20 poena

Napisati program za sortiranje imena ljudi. Korisnik treba da moze da ukuca porizvoljan broj "Prezime Ime" stringova.
Nakon sto korisnik udari Enter bez unosa, program treba da ispise sortirano imena ljudi (od A do Z)
'''

# Resenje:

names = []
name = input("Unesite ime")
while name != "":
    names.append(name)
    name = input("Unesite ime")
print (names)
# Sortiranje niza
names.sort()
print (names)

'''
Zadatak 2 - 40 poena

Napisati program za video klub.
KOrisnicki meni treba da ima sledece opcije:
1. Unos filma novog filma u bazu. - 10p
Unosi se samo ime filma pri cemu program generise ID koji je u sustini redni broj u bazi
2. Izdavanje filma. Unosi se ID filma koji se izdaje. - 10p
3. Vracanje filma. Unosi se ID filma koji se vraca. - 10p
4. Pregled filmova (izlistavaju se sifra, naslov i da li je film dostupan) - 10p
'''

# Resenje:
Videoteka = []
Izdati_filmovi = []
# Ispis menija
def Menu():
    print    ("1 - Unos filma u bazu")
    print    ("2 - Izdavaje filma")
    print    ("3 - vracanje filma")
    print    ("4 - pregled filmova")
    
# odabir opcija
def Operatiom():
    operation =input("What you want to do?") 
# prva opcija
def Unos():
    film = input("Unesite ime filma")
    Videoteka.append(film)
# druga opcija
def Izdavanje_filma():
    film_za_izdavanje = input("Koji film zelite da uzmete?")
    if film_za_izdavanje not in Izdati_filmovi:
        film_za_izdavanje.append(Izdati_filmovi)
        print("Zelimo vam prijatno gledanje!")
    else:
        i = input("Zao nam je film je izdat, da li zelite neki drugi? y/n")
        if "y":
            Izdavanje_filma()
        else:
                close


# treca opcija

def Vracanje_filma():
    film_za_vracanje = input("Koji film vracate?")
    if film_za_vracanje in Izdati_filmovi:
        film_za_vracanje.remove(Izdati_filmovi)
    else:
        a = input("da li ste sigurni da ste film iznajmili kod nas? da li hocete da vratite neki drugi? y/n?")
        if "y":
            Vracanje_filma()
        else:
            close
# cetvrta opcija

def Prikaz_svih_filmova():
    print (Videoteka)


def Main():
    Menu()
    opcija =  int(input("Koju opciju zelite?")
    if (opcija != '1', or opcija != '2', or opcija != '3' or opcija != '4')
        print("Zao nam je ali ta opcija ne postoji, probajte neku drugu.")
    elif opcija == '1':
        Unos()
    elif opcija == '2':
        Izdavanje_filma()
    elif opcija == '3':
        Vracanje_filma
    elif opcija == '4':
        Prikaz_svih_filmova()


'''
Zadatak 3 - 30 poena

Napisati program za citanje fajla i ispis u konzoli. 
Uz ispis, program bi trebalo da proveri da li je tekst pesma:
- da li svaki od redova ima manje od 40 slova
- da li postoji struktura strofa - ukoliko se nakon svakog 3eg ili 4og stiha javlja prazan red radi se o pesmi
'''

# Resenje
# Napraviti listu u koju se upisuje tekst
open_file = open(Provera, "rb")
print (open_file)
# Napraviti proveru da li red ima manje od 40 slova
# proveriti da li postoje strofe
# pesma jeste ili nije



'''
Zadatak 4 - 10 poena

Napisati funkciju koja sracunava faktorijal
'''
n = int(input("Unesi broj faktorijala"))

# Resenje
n = int(input("Unesi broj faktorijala"))
num = 1
while n >= 1:
    num = num * n
    n = n - 1
print (num)
