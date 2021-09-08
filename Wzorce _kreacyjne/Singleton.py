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

s1 = Singleton_Genius("Yang", "Zhou","a")
s2 = Singleton_Genius("Elon", "Musk","b")
s1.plik_tekstowy()
s2.plik_tekstowy()

print(s1==s2)
a = 4
b = a
print("v1", b == a)
a = 5
print("v2", b == a)




