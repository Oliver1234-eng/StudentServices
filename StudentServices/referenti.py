# funkcija proverava da li postoji referent sa tim korisnickim imenom i lozinkom u sistemu
# prijava :: (dict[], string, string) -> dict | None
def prijava(lista_referenata, korisnicko_ime, lozinka):
    for referent in lista_referenata:
        if korisnicko_ime == referent['korisnicko ime'] and lozinka == referent['lozinka']:
            return referent

    return None