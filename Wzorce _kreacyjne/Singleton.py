from threading import Lock, Thread

class Singleton_Genius(type):

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=Singleton_Genius):

    def __init__(self, value, first_name, last_name, text):
        self.value = value
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


if __name__ == "__main__":
    s1 = Singleton("FOO","FOO","FOO","FOO5")
    s2 = Singleton("BAR1","BAR1","BAR1","BAR5")

    w1 = Thread(target=s1.plik_tekstowy, args=())
    w2 = Thread(target=s2.plik_tekstowy, args=())
    w1.start()
    w2.start()

    # s1 = Singleton_Genius("Helm", "Gamma", "string1")
    # s2 = Singleton_Genius("Johnson", "Vlissides", "string2")
    # s1.plik_tekstowy()
    # s2.plik_tekstowy()
    #print("Czy s1 i s2 to ten sam obiekt: ", s1 == s2)