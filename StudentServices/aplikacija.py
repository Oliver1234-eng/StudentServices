import studenti
import studenti_io
import referenti
import referenti_io

def test():
    lista_studenata = [{'broj indeksa': '12', 'ime': 'Pera', 'prezime': 'Peric', 'ime roditelja': 'Ivan', 'datum rodjenja': '21.03.1998', 
    'jmbg': '123321123321', 'adresa': 'Fruskogorska 18', 'telefon': '064/123-32-11', 'email': 'pera@gmail.com',
    'godina studija': 2}, {'broj indeksa': '13', 'ime': 'Mitar', 'prezime': 'Mitrovic', 'ime roditelja': 'Jovan', 'datum rodjenja': '22.07.1999', 
    'jmbg': '12332131221', 'adresa': 'Bulevar Cara Lazara', 'telefon': '063/123-32-12', 'email': 'mitar@gmail.com',
    'godina studija': 1}, {'broj indeksa': '14', 'ime': 'Stevan', 'prezime': 'Stevanovic', 'ime roditelja': 'Nemanja', 'datum rodjenja': '15.05.1999', 
    'jmbg': '1231232221', 'adresa': 'Maksima Gorkog 3', 'telefon': '064/123-32-22', 'email': 'steva@gmail.com',
    'godina studija': 1}, {'broj indeksa': '15', 'ime': 'Jovana', 'prezime': 'Perkovic', 'ime roditelja': 'Uros', 'datum rodjenja': '11.02.1998', 
    'jmbg': '112233221122', 'adresa': 'Temerinska 22a', 'telefon': '064/123-32-33', 'email': 'jovana@gmail.com',
    'godina studija': 1}, {'broj indeksa': '16', 'ime': 'Smiljana', 'prezime': 'Stevic', 'ime roditelja': 'Nikola', 'datum rodjenja': '10.09.1999', 
    'jmbg': '122112244', 'adresa': 'Bulevar Patrijarha Pavla 10', 'telefon': '064/123-32-55', 'email': 'smiljana@gmail.com',
    'godina studija': 1}]
    student = studenti.pronalazenje_po_broju_indeksa(lista_studenata, '12')
    print(student)
    student = studenti.pronalazenje_po_broju_indeksa(lista_studenata, '22')
    print(student)
    l = studenti.pronalazenje_po_prezimenu(lista_studenata, 'per')
    print(l)
    l = studenti.pronalazenje_po_prezimenu(lista_studenata, 'yyy')
    print(l)
    s = studenti.izmena_podataka_o_studentu(lista_studenata, '12', 'test adresa', '111', 'test@gmail.com')
    print(s)
    print(lista_studenata)
    x = studenti.upis_studenta(lista_studenata, {'broj indeksa': '19', 'ime': 'Mihajlo', 'prezime': 'Jovanovic', 
    'ime roditelja': 'Stevan', 'datum rodjenja': '11.09.1999', 'jmbg': '123', 'adresa': 'Bulevar Patrijarha Pavla 20', 
    'telefon': '064/123-32-51', 'email': 'mihajlo@gmail.com', 'godina studija': 1})
    print(x)
    print(lista_studenata)
    x = studenti.upis_studenta(lista_studenata, {'broj indeksa': '19', 'ime': 'Mihajlo', 'prezime': 'Jovanovic', 
    'ime roditelja': 'Stevan', 'datum rodjenja': '11.09.1999', 'jmbg': '123', 'adresa': 'Bulevar Patrijarha Pavla 20', 
    'telefon': '064/123-32-51', 'email': 'mihajlo@gmail.com', 'godina studija': 1})
    print(x)
    print(lista_studenata)
    studenti.grupni_upis_godine(lista_studenata, ['12', '13', '15'])
    print(lista_studenata)
    studenti_io.cuvanje_liste_studenata(lista_studenata)

def zaglavlje():
    print("id    |broj indeksa|ime          |prezime          |godina studija")
    print("------------------------------------------------------------------")

def prikaz_studenta(student):
    print(str(student['id']).ljust(6) + "|" + student['broj indeksa'].ljust(12) + "|" + student['ime'][:13].ljust(13) + "|" + student['prezime'][:17].ljust(17) + "|" + str(student['godina studija']))

def prikaz_studenata(lista_studenata):
    for student in lista_studenata:
        prikaz_studenta(student)

def meni():
    print("1 - Pronalazenje studenta po broju indeksa")
    print("2 - Pronalazenje studenta po prezimenu")
    print("3 - Prikaz svih studenata")
    print("4 - Izmena podataka studenta")
    print("5 - Upis novog studenta")
    print("6 - Grupni upis studenata")
    print("7 - Brisanje studenta")
    print("x - Kraj")

def main():
    lista_referenata = referenti_io.citanje_liste_referenata()
    korisnicko_ime = input("Korisnicko ime: ")
    lozinka = input("Lozinka: ")
    referent = referenti.prijava(lista_referenata, korisnicko_ime, lozinka)
    while not referent:
        korisnicko_ime = input("Korisnicko ime: ")
        lozinka = input("Lozinka: ")
        referent = referenti.prijava(lista_referenata, korisnicko_ime, lozinka)
    while True:
        meni()
        komanda = input(">> ")
        if komanda == '1':
            broj_indeksa = input("Broj indeksa: ")
            lista_studenata = studenti_io.citanje_liste_studenata()
            student = studenti.pronalazenje_po_broju_indeksa(lista_studenata, broj_indeksa)
            zaglavlje()
            prikaz_studenta(student)
        elif komanda == '2':
            prezime = input("Prezime: ")
            lista_studenata = studenti_io.citanje_liste_studenata()
            lista_studenata = studenti.pronalazenje_po_prezimenu(lista_studenata, prezime)
            zaglavlje()
            prikaz_studenata(lista_studenata)
        elif komanda == '3':
            lista_studenata = studenti_io.citanje_liste_studenata()
            lista_studenata = studenti.sortiranje_liste_studenata(lista_studenata)
            zaglavlje()
            prikaz_studenata(lista_studenata)
        elif komanda == '4':
            broj_indeksa = input("Broj indeksa: ")
            lista_studenata = studenti_io.citanje_liste_studenata()
            adresa = input("Adresa: ")
            telefon = input("Telefon: ")
            email = input("Email: ")
            studenti.izmena_podataka_o_studentu(lista_studenata, broj_indeksa, adresa, telefon, email)
            studenti_io.cuvanje_liste_studenata(lista_studenata)
        elif komanda == '5':
            broj_indeksa = input("Broj indeksa: ")
            ime = input("Ime: ")
            prezime = input("Prezime: ")
            ime_roditelja = input("Ime roditelja: ")
            datum_rodjenja = input("Datum rodjenja: ")
            jmbg = input("JMBG: ")
            adresa = input("Adresa: ")
            telefon = input("Telefon: ")
            email = input("Email: ")
            godina_studija = 1
            novi_student = {'broj indeksa': broj_indeksa, 'ime': ime, 'prezime': prezime, 'ime roditelja': ime_roditelja, 
            'datum rodjenja': datum_rodjenja, 'jmbg': jmbg, 'adresa': adresa, 'telefon': telefon, 
            'email': email, 'godina studija': godina_studija, 'obrisan': False, 'id': studenti_io.sledeci_id()}
            lista_studenata = studenti_io.citanje_liste_studenata()
            studenti.upis_studenta(lista_studenata, novi_student)
            studenti_io.cuvanje_liste_studenata(lista_studenata)
        elif komanda == '6':
            lista_indeksa = []
            while True:
                broj_indeksa = input("Broj indeksa: ")
                if broj_indeksa == '':
                    break
                lista_indeksa.append(broj_indeksa)
            lista_studenata = studenti_io.citanje_liste_studenata()
            studenti.grupni_upis_godine(lista_studenata, lista_indeksa)
            studenti_io.cuvanje_liste_studenata(lista_studenata)
        elif komanda == '7':
            broj_indeksa = input("Broj indeksa: ")
            lista_studenata = studenti_io.citanje_liste_studenata()
            studenti.brisanje_studenta(lista_studenata, broj_indeksa)
            studenti_io.cuvanje_liste_studenata(lista_studenata)
        elif komanda == 'x':
            print("Dovidjenja!")
            break
        else:
            print("Nije uneta validna komanda!")
        input('')

    
if __name__ == '__main__':
    main()