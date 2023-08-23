# cuvanje liste u fajl
# cuvanje_liste :: dict[] -> None
def cuvanje_liste(lista_entiteta, naziv_fajla, konverter):
    f = open(naziv_fajla, 'w')
    for entitet in lista_entiteta:
        print(konverter(entitet), file = f)
    f.close()

# ucita listu studenata iz fajla
# () -> dict[]
def citanje_liste(naziv_fajla, konverter):
    f = open(naziv_fajla, 'r')
    redovi = f.readlines()
    f.close()
    ret_val = []
    for red in redovi:
        entitet = konverter(red.strip())
        if 'obrisan' in entitet and entitet['obrisan'] == False:
            ret_val.append(entitet)
    
    return ret_val