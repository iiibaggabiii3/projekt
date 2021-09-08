from __future__ import annotations
from random import randrange
from typing import List


class Produkt():

    def attach(self, obserwujacy: Obserwator) -> None:
        pass

    def detach(self, obserwujacy: Obserwator) -> None:
        pass

    def notify(self) -> None:
        pass

class Konkretny_produkt(Produkt):
    _status_produkty = None
    _Lista_obserwatorow: List[Obserwator] = []

    def attach(self, obserwujacy: Obserwator) -> None:
        print("Dodanie obserwatora")
        self._Lista_obserwatorow.append(obserwujacy)

    def detach(self, obserwujacy: Obserwator) -> None:
        print("Usunięcie obserwatora")
        self._Lista_obserwatorow.remove(obserwujacy)

    def notify(self) -> None:
        print("Powiadomienei obserwatorów")
        for obserwujacy in self._Lista_obserwatorow:
            obserwujacy.update(self)

    def zdarzenie(self) -> None:
        print("\nRobię coś ważnego")
        self._status_produkty = randrange(0, 10)
        print(f"Mój stan się zmienił: {self._status_produkty}")
        self.notify()


class Obserwator():

    def update(self, subject: Produkt) -> None:
        pass

class Obserwujacy_A(Obserwator):
    def update(self, produkt: Produkt) -> None:
        if produkt._status_produkty < 3:
            print("Obserwujacy_A: Zareagował na zdarzenie")


class Obserwujacy_B(Obserwator):
    def update(self, produkt: Produkt) -> None:
        if produkt._status_produkty == 0 or produkt._status_produkty >= 2:
            print("Obserwujacy_B: Zareagował na zdarzenie")

class Obserwujacy_C(Obserwator):
    def update(self, produkt: Produkt) -> None:
        if produkt._status_produkty == 3 or produkt._status_produkty >= 1:
            print("Obserwujacy_C: Zareagował na zdarzenie")

if __name__ == "__main__":
    # The client code.

    przedmiot = Konkretny_produkt()
    obserwujacy_a = Obserwujacy_A()
    przedmiot.attach(obserwujacy_a)

    obserwujacy_b = Obserwujacy_B()
    przedmiot.attach(obserwujacy_b)

    obserwujacy_c = Obserwujacy_C()
    przedmiot.attach(obserwujacy_c)

    przedmiot.zdarzenie()
    przedmiot.zdarzenie()
    przedmiot.zdarzenie()


