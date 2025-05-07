class Buku:
    def __init__(self, judul, penulis):
        self.__judul = judul # private attribute
        self.penulis = penulis

    def info(self):
        print(f"Judul: {self.__judul}, Penulis: {self.penulis}")

b1 = Buku("Python Dasar", "Budi")
b1.info()