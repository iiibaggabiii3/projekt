class Singleton_Genius(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Singleton_Genius.__instance:
            Singleton_Genius.__instance = object.__new__(cls)
        return Singleton_Genius.__instance

    def __init__(self, first_name, last_name, text):
        self.first_name = first_name
        self.last_name = last_name
        self.text = text

    def plik_tekstowy(self):
        plik = open("file.txt", "a")
        if plik.writable():
            plik.write(self.text)
            plik.write("\n")
            plik.close()
        else:
            print("Problem z otwarciem pliku")

s1 = Singleton_Genius("Helm", "Gamma","string1")
s2 = Singleton_Genius("Johnson", "Vlissides", "string2")
s1.plik_tekstowy()
s2.plik_tekstowy()

print("Czy s1 i s2 to ten sam obiekt: ", s1==s2)

object_id = id(s1)
hexadecimal = hex(object_id)
print(hexadecimal)

object_id = id(s2)
hexadecimal = hex(object_id)
print(hexadecimal)

class testowa:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstawiam_sie(self):
        return f"nazywam sie:" + self.imie + " " + self.nazwisko

print("")
test = testowa("Lukasz", "Prządka")
print(test.przedstawiam_sie())
test1 = testowa("Lukasz", "Prządka")
print(test.przedstawiam_sie())
print("Czy test i test1 to ten sam obiekt: ", test == test1)

object_id = id(test)
hexadecimal = hex(object_id)
print(hexadecimal)

object_id = id(test1)
hexadecimal = hex(object_id)
print(hexadecimal)
