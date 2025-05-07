class RekeningBank:
    def __init__(self, saldo):
        self.__saldo = saldo

    def lihat_saldo(self):
        print(f"Kamu Mempunyai Saldo Sebanyak {self.__saldo}")

    def tambah_saldo(self, jumlah):
        self.__saldo += jumlah
        print(f"Saldo anda ditambahkan {jumlah}")

    def tarik_saldo(self, jumlah):
        self.__saldo -= jumlah
        print(f"Saldo Anda Ditarik {jumlah}")

rp = RekeningBank(100000)
rp.lihat_saldo()
rp.tarik_saldo(50000)
rp.tambah_saldo(10000)
rp.lihat_saldo()