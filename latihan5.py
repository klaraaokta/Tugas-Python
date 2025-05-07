class Siswa(object):
    nama = None

    def __init__(self, nama):
        self.nama = nama

    def minum(self):
        print('{} air putih'.format(self.nama))

class SiswaMileial(Siswa):
    CitaCita = None

    def citacita(self, citacita):
        self.citacita = citacita

    def info(self):
        print('Nama :{},Cita - Cita:{}'.format(self.nama, self.citacita))

Klaraa = SiswaMileial('Klaraa')
Klaraa.citacita('Guru')
Klaraa.info()

Ridaa = SiswaMileial('Ridaa')
Ridaa.citacita('-')
Ridaa.info()