l = [2, 4, 5, 1, 3]

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

tacke = [(1, 2), (2, 3), (1, 1), (4, 4), (12, 19)] # tacka[0]**2 + tacka[1]**2

def student_selector(student):
    return student['prezime']

def broj_selector(x):
    return x

def tacka_selector(tacka):
    return tacka[0]**2 + tacka[1]**2

# funkcija primi listu i vrati sortiranu listu
# sortiraj :: list -> list
def sortiraj(l, selector):
    for i in range(len(l)):
        indeks_najmanjeg = i
        for j in range(i + 1, len(l)):
            if selector(l[indeks_najmanjeg]) > selector(l[j]):
                indeks_najmanjeg = j
        temp = l[i]
        l[i] = l[indeks_najmanjeg]
        l[indeks_najmanjeg] = temp

sortiraj(l, broj_selector)
print(l)

sortiraj(lista_studenata, student_selector)
print(lista_studenata)

sortiraj(tacke, tacka_selector)
print(tacke)

#def broj_indeksa_selector(student):
    #return student('broj indeksa')

sortiraj(lista_studenata, lambda student: student['broj indeksa'])
print(lista_studenata)