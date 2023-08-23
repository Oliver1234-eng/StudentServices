import data_io

# pretvaranje reda iz fajla sa referentima u recnik
# str_2_referent :: string -> dict
def str_2_referent(str_referent):
    podaci = str_referent.split(',')
    
    return {'ime': podaci[0], 'prezime': podaci[1], 'korisnicko ime': podaci[2], 'lozinka': podaci[3], 'obrisan': podaci[4] == 'True'}

# ucita listu referenata iz fajla
# () -> dict[]
def citanje_liste_referenata():
    return data_io.citanje_liste('referenti.csv', str_2_referent)