class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        luas = 3.14 * self.jari_jari * self.jari_jari
        print(f"Luas lingkaran dengan jari-jari {self.jari_jari} adalah {luas}")

    def hitung_keliling(self):
        keliling = 2 * 3.14 * self.jari_jari
        print(f"Keliling lingkaran dengan jari-jari {self.jari_jari} adalah {keliling}")

lingkaran = Lingkaran(7)
lingkaran.hitung_luas()
lingkaran.hitung_keliling()