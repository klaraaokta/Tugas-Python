class Laptop:
    merk = 'Asus'
    ram = '8 GB'

    def __init__(self, merk,ram):
        self.merk = merk
        self.ram = ram

    def info(self):
        print(f"Laptop ini bermerek {self.merk}, dengan ram {self.ram}")

Siswa1 = Laptop('Asus', '8 GB')
Siswa1.info()