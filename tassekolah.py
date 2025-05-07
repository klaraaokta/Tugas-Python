class TasSekolah:
    merk = "Movic"
    warna = "Pink"
    ukuran = "Besar"
TasSekolah_saya = TasSekolah()
print(TasSekolah_saya.merk) # Output: Movic
TasSekolah_saya = TasSekolah()
print(TasSekolah_saya.warna) # Output: Pink
TasSekolah_saya = TasSekolah()
print(TasSekolah_saya.ukuran) # Output: Besar

class TasSekolah:
    def __init__(self):
        self.merk = "Movic"
        self.warna = "Pink"
        self.ukuran = "Besar"

    def tempatpenyimpanan(self):
        print("Tempat Penyimpanan Buku atau Barang")

    def dipakai(self):
        print("Dipakai untuk Sekolah")

tassekolah = TasSekolah()
tassekolah = TasSekolah()

tassekolah.tempatpenyimpanan()
tassekolah.dipakai()