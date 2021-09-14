from __future__ import annotations
from typing import List


class Produkt:
    _lista_obserwatorow: List[Obserwator] = []
    _lista_danych: List[Obserwator] = []

    def subscribe(self, observer: Obserwator):
        print("dodany obserwator")
        self._lista_obserwatorow.append(observer)

    def detach(self, observer: Obserwator):
        self._lista_obserwatorow.remove(observer)

    def onNext(self):
        for observer in self._lista_obserwatorow:
            print("obserwator poinformowany")
            observer.update(self)


    def sprawdzenie_iloci_znakow_w_pliku(self):
        plik = open("text.txt", "r")
        if plik.readable():
            ile = len(plik.read())
            plik.close()
            return ile
        else:
            print("coś jest nie tak z plikiem")

    def sprawdzenie_pliku(self, status):
        "Biznesowa logika"
        sprawdzany_plik = self.sprawdzenie_iloci_znakow_w_pliku()
        # print( "a: ", sprawdzany_plik, "sta;", status)
        if sprawdzany_plik != status:
            self.onNext()
            return sprawdzany_plik
        else:
            return "brak zmian"

class Obserwator:

    def update(self, produkt: Produkt):
        pass

class Obserwator1(Obserwator):
    def update(self, produkt: Produkt):
        status = produkt.sprawdzenie_iloci_znakow_w_pliku()
        print( f"obserwatorze dziękuje za informacje, jest teraz {status} znaki w pliku")

class Obserwator2(Obserwator):
    def update(self, produkt: Produkt):
        status = produkt.sprawdzenie_iloci_znakow_w_pliku()
        znaki = int(status)
        if znaki <= 100:
            print("obserwatorze, plik ma wiecej znaków niż 100")
        else:
            print("obserwatorze, plik ma mniej znaków nież 100")

class Obserwator3(Obserwator):
    def update(self, produkt: Produkt):
        #status = produkt.sprawdzenie_iloci_znakow_w_pliku()
        print(f"obserwatorze dziękuje za informacje, jest teraz {status} znaki w pliku")

def pisanie_do_pliku(moj_tekst):
    plik = open("text.txt", "a")
    if plik.writable():
        # plik.write("\n")
        plik.write(moj_tekst)
        plik.close()
    else:
        print("coś jest nie tak z plikiem")

if __name__ == "__main__":

    produkt = Produkt()
    status = produkt.sprawdzenie_iloci_znakow_w_pliku()
    obserwator1 = Obserwator1()
    produkt.subscribe(obserwator1)

    obserwator2 = Obserwator2()
    produkt.subscribe(obserwator2)

    print(status)
    pisanie_do_pliku(input("wpisz swoj tekst do wpisania do pliku: "))

    produkt.sprawdzenie_pliku(status)

