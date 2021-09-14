from __future__ import annotations
from typing import List


class Produkt:
    test = 1 + 3
    pass


class Obserwator1:
    def update(self, produkt: Produkt):
        print(f"Test{produkt.test}")

produkt = Produkt()
o = Obserwator1
o.update("d")