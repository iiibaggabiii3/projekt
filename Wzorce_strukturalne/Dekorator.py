def dekorator(func):
    def wrapper():
        plik = open("file.txt", "a")
        if plik.writable():
            plik.write(func())
            plik.write("\n")
            plik.close()
            print("tekst pomyślnie zapisany do pliku: ")
        else:
            print("mamy problem z otwarciem pliku")
            plik.close()
    return wrapper


@dekorator
def witaj():
    return input("własny tekst: ")

@dekorator
def cos_swojego():
    return "to moj tekst testowy"

t = witaj()
cos_swojego()

