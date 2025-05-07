class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Hewan Bersuara")

class Kucing(Hewan):
    def suara(self):
        print(f"{self.nama}: Meong")

class Kambing(Hewan):
    def suara(self):
        print(f"{self.nama}: Mbeee")

class Sapi(Hewan):
    def suara(self):
        print(f"{self.nama}: Moooo")

h = Hewan("nama")
h.suara()
k = Kucing("Kucing")
k.suara()
k1 = Kambing("Kambing")
k1.suara()
s = Sapi("Sapi")
s.suara()