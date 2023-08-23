# Pronalazenje studenta po broju indeksa. Nakon izvrsavanja ove komande prikazuju se podaci o 
# studentu sa datim brojem indeksa.
# pronalazenje_po_broju_indeksa :: (dict[], string) -> dict
def pronalazenje_po_broju_indeksa(lista_studenata, broj_indeksa):
    for student in lista_studenata:
        if student['broj indeksa'] == broj_indeksa:
            return student
    # return None

# Pretrazivanje studenata po prezimenu. Nakon izvrsavanja svake od ovih komandi prikazuju se podaci o studentima koji 
# zadovoljavaju kriterijum pretrazivanja.
# pronalazenje_po_prezimenu :: (dict[], string) -> dict
def pronalazenje_po_prezimenu(lista_studenata, deo_prezimena):
    ret_val = []
    for student in lista_studenata:
        if deo_prezimena.lower() in student['prezime'].lower():
            ret_val.append(student)
    
    return ret_val

# Pregledanje svih studenata sortiranih po prezimenu.
# sortiranje_liste_studenata :: dict[] -> dict[]    
def sortiranje_liste_studenata(lista_studenata):
    return sorted(lista_studenata, key = lambda student: student['prezime'])

# Izmena adrese, telefona i e-maila studenta. Pri izvrsavanju ove komande, referent unosi broj indeksa studenta ciji podaci
# se menjaju i potom nove podatke.
# izmena_podataka_o_studentu :: (dict[], string, string, string, string) -> dict
def izmena_podataka_o_studentu(lista_studenata, broj_indeksa, adresa, telefon, email):
    student = pronalazenje_po_broju_indeksa(lista_studenata, broj_indeksa)
    student['adresa'] = adresa
    student['telefon'] = telefon
    student['email'] = email

    return student

# Upis studenata na prvu godinu studija, tj. upis novog studenta koji prethodno nije bio evidentiran u sistemu.
# upis_studenta :: (dict[], dict) -> dict[]
def upis_studenta(lista_studenata, novi_student):
    for student in lista_studenata:
        if student['broj indeksa'] == novi_student['broj indeksa'] or student['jmbg'] == novi_student['jmbg']:
            return False
    lista_studenata.append(novi_student)

    return True

# Grupni upis studenata na narednu godinu studija. Pri tome, unose se brojevi indeksa onih studenata koji upisuju 
# narednu godinu, i podatak o tekucoj godini studija se inkrementira za svakog od njih.
# grupni_upis_godine :: (dict[], string[]) -> None
def grupni_upis_godine(lista_studenata, lista_indeksa):
    for indeks in lista_indeksa:
        for student in lista_studenata:
            if indeks == student['broj indeksa'] and student['godina studija'] <= 4:
                student['godina studija'] += 1

# uklanja studenta po broju indeksa - logicko brisanje
def brisanje_studenta(lista_studenata, broj_indeksa):
    student_za_brisanje = pronalazenje_po_broju_indeksa(lista_studenata, broj_indeksa)
    if student_za_brisanje:
        student_za_brisanje['obrisan'] = True
        return True

    return False

# uklanja studenta po broju indeksa - fizicko brisanje
# entitet se ukloni iz sistema
def brisanje_studenta_fizicko_brisanje(lista_studenata, broj_indeksa):
    student_za_brisanje = pronalazenje_po_broju_indeksa(lista_studenata, broj_indeksa)
    if student_za_brisanje:
        lista_studenata.remove(student_za_brisanje)
        return True

    return False