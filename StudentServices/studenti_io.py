import data_io

# pretvaranje recnika student u red u fajlu
# student_2_str :: dict -> string
def student_2_str(student):
    return student['broj indeksa'] + ',' + student['ime'] + ',' + student['prezime'] + ',' + student['ime roditelja'] + ',' + student['datum rodjenja'] + ',' + student['jmbg'] + ',' + student['adresa'] + ',' + student['telefon'] + ',' + student['email'] + ',' + str(student['godina studija']) + ',' + str(student['obrisan']) + ',' + str(student['id'])

# pretvaranje reda iz fajla sa studentima u recnik
# str_2_student :: string -> dict
def str_2_student(str_student):
    podaci = str_student.split(',')
    
    return {'broj indeksa': podaci[0], 'ime': podaci[1], 'prezime': podaci[2], 'ime roditelja': podaci[3], 
    'datum rodjenja': podaci[4], 'jmbg': podaci[5], 'adresa': podaci[6], 'telefon': podaci[7], 
    'email': podaci[8], 'godina studija': int(podaci[9]), 'obrisan': podaci[10] == 'True', 'id': int(podaci[11])}

# cuvanje liste studenata u fajl
# cuvanje_liste_studenata :: dict[] -> None
def cuvanje_liste_studenata(lista_studenata):
    data_io.cuvanje_liste(lista_studenata, 'studenti.csv', student_2_str)

# ucita listu studenata iz fajla
# () -> dict[]
def citanje_liste_studenata():
    return data_io.citanje_liste('studenti.csv', str_2_student)

# posto radimo logicko brisanje znamo da ce biti onoliko redova u fajlu
# koliko je bilo studenata od pocetka koriscenja aplikacije
def sledeci_id():
    f_studenti = open('studenti.csv', 'r')
    lines = f_studenti.readlines()
    f_studenti.close()
    
    return len(lines) + 1