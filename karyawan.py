class Karyawan:
    def salam(self):
        print("Halo, saya adalah karyawan")

class Manager(Karyawan):
    def salam(self):
        print("Halo, saya adalah manager")

k = Karyawan()
k.salam()
m = Manager()
m.salam()