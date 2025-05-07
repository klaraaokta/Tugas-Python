class SepedaListrik:
    merk = "Genio"
    warna = "Biru"
    tipe = "Lipat"
SepedaListrik_saya = SepedaListrik()
print(SepedaListrik_saya.merk) # Output: Genio
SepedaListrik_saya = SepedaListrik()
print(SepedaListrik_saya.warna) # Output: Biru
SepedaListrik_saya = SepedaListrik()
print(SepedaListrik_saya.tipe) # Output: Lipat


class SepedaListrik:
    def __init__(self):
        self.merk = "Genio"
        self.warna = "Merah"
        self.tipe = "Lipat"

    def maju(self):
        print("Sepeda ini sedang maju")

    def mundur(self):
        print("Sepeda ini mundur")

    def berhenti(self):
        print("Sepeda ini berhenti")
sepedalistrik = SepedaListrik()
sepedalistrik = SepedaListrik()
sepedalistrik = SepedaListrik()

sepedalistrik.maju()
sepedalistrik.mundur()
sepedalistrik.berhenti()