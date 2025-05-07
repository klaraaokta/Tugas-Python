class Ayah:
    sifat = "sabar,jujur,dan pemalu"
    sikap = "pemaaf,dan bertanggung jawab"
    pola_komunikasi = "tertutup,dan juga pendengar yang baik"
    warna_kulit = "putih"
    warna_rambut = "hitam"
    tinggi_badan = "sedang"
    berat_badan = "kurus"
    warna_mata = "hitam"
    bentuk_hidung = "pesek"
    bentuk_bibir = "tipis"
    Tipe_rambut = "lurus"
    Telinga = "biasa"
    def ayah(self):
        print("")
    
class Ibu:
    watak = "sabar,jujur,dan ramah"
    perilaku = "tegas,dan bertanggung jawab"
    polakomunikasi = "terbuka,dan juga suka berbicara"
    warnakulit = "sawo matang"
    warnarambut = "cokelat tua"
    tinggi_badan = "sedang"
    beratbadan = "proporsional"
    warnamata = "cokelat"
    bentuk_hidung = "pesek"
    bentukbibir = "tebal"
    Tiperambut = "bergelombang"
    Telinga = "biasa"
    def ibu(self):
        print("Karakter Ayah dan Ibu yang Diwarisi Kepada Saya dan Adik - Adik Saya Yaitu:")
        print("")

class Klara(Ayah, Ibu):
    def karakter(self):
        print(f"Ayah saya mewariskan sifat yang {self.sifat} kepada saya")
    def perilaku(self):
        print(f"Ayah saya mewariskan sikap yang {self.sikap} kepada saya")
    def komunikasi(self):
        print(f"Ayah saya mewariskan pola komunikasi yang {self.pola_komunikasi} kepada saya")
    def kulit(self):
        print(f"Ayah saya mewariskan warna kulit yang {self.warna_kulit} kepada saya")
    def berat(self):
        print(f"Ayah saya mewariskan berat badan yang {self.berat_badan} kepada saya")
    def rambut(self):
        print(f"Ibu saya mewariskan warna rambut yang {self.warnarambut} kepada saya")
    def mata(self):
        print(f"Ibu saya mewariskan warna mata yang {self.warnamata} kepada saya")
    def bibir(self):
        print(f"Ibu saya mewariskan bentuk bibir yang {self.bentukbibir} kepada saya")
    def tipe(self):
        print(f"Ibu saya mewariskan tipe rambut yang {self.Tiperambut} kepada saya")
    def tinggi(self):
        print(f"Ayah dan Ibu saya mewariskan tinggi badan yang {self.tinggi_badan} kepada saya")
    def hidung(self):
        print(f"Ayah dan Ibu saya mewariskan bentuk hidung yang {self.bentuk_hidung} kepada saya")
    def kuping(self):
        print(f"Ayah dan Ibu saya mewariskan Telinga yang {self.Telinga} kepada saya")
        print("")

class Fairel(Ayah, Ibu):
    def rambut(self):
        print(f"Ayah saya mewariskan warna rambut yang {self.warna_rambut} kepada adik pertama saya")
    def berat(self):
        print(f"Ayah saya mewariskan berat badan yang {self.berat_badan} kepada adik pertama saya")
    def mata(self):
        print(f"Ayah saya mewariskan warna mata yang {self.warna_mata} kepada adik pertama saya")
    def bibir(self):
        print(f"Ayah saya mewariskan bentuk bibir yang {self.bentuk_bibir} kepada adik pertama saya")
    def tipe(self):
        print(f"Ayah saya mewariskan tipe rambut yang {self.Tipe_rambut} kepada adik pertama saya")
    def karakter(self):
        print(f"Ibu saya mewariskan sifat yang {self.watak} kepada adik pertama saya")
    def perilaku(self):
        print(f"Ibu saya mewariskan sifat yang {self.sikap} kepada adik pertama saya")
    def pola(self):
        print(f"Ibu saya mewariskan pola komunikasi yang {self.polakomunikasi} kepada adik pertama saya")
    def kulit(self):
        print(f"Ibu saya mewariskan warna kulit yang {self.warnakulit} kepada adik pertama saya")
    def tinggi(self):
        print(f"Ayah dan Ibu saya mewariskan tinggi badan yang {self.tinggi_badan} kepada adik pertama saya")
    def hidung(self):
        print(f"Ayah dan Ibu saya mewariskan bentuk hidung yang {self.bentuk_hidung} kepada adik pertama saya")
    def kuping(self):
        print(f"Ayah dan Ibu saya mewariskan Telinga yang {self.Telinga} kepada adik pertama saya")
        print("")

class Syhailendra(Ayah, Ibu):
    def kulit(self):
        print(f"Ayah saya mewariskan warna kulit yang {self.warna_kulit} kepada adik kedua saya")
    def rambut(self):
        print(f"Ayah saya mewariskan warna rambut yang {self.warna_rambut} kepada adik kedua saya")
    def mata(self):
        print(f"Ayah saya mewariskan warna mata yang {self.warna_mata} kepada adik kedua saya")
    def bibir(self):
        print(f"Ayah saya mewariskan bentuk bibir yang {self.bentuk_bibir} kepada adik kedua saya")
    def tipe(self):
        print(f"Ayah saya mewariskan tipe rambut yang {self.Tipe_rambut} kepada adik kedua saya")
    def hidung(self):
        print(f"Ayah dan Ibu saya mewariskan bentuk hidung yang {self.bentuk_hidung} kepada adik kedua saya")
    def kuping(self):
        print(f"Ayah dan Ibu saya mewariskan Telinga yang {self.Telinga} kepada adik kedua saya")

ayahsaya = Ayah()
ayahsaya.ayah()

ibusaya = Ibu()
ibusaya.ibu()

saya = Klara()
saya.karakter()
saya.perilaku()
saya.komunikasi()
saya.kulit()
saya.berat()
saya.rambut()
saya.mata()
saya.bibir()
saya.tipe()
saya.tinggi()
saya.hidung()
saya.kuping()

saya = Fairel()
saya.rambut()
saya.berat()
saya.mata()
saya.bibir()
saya.tipe()
saya.karakter()
saya.perilaku()
saya.pola()
saya.kulit()
saya.tinggi()
saya.hidung()
saya.kuping()

saya = Syhailendra()
saya.kulit()
saya.rambut()
saya.mata()
saya.bibir()
saya.hidung()
saya.kuping()