class Manusia(object):
    nama = None

    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print ('{} makan nasi'.format(self.nama))

class ManusiaMilenial(Manusia):
    email = None
    __password = None

    def set_email(self, email):
        self.email = email

    def set_pass(self, password):
        self.__password = password

    def __samarkan_password(self):
        return self.__password.replace('a', '*')

    def info(self):
        print ('nama={}, email={}, pass={}'.format(self.nama, self.email, self.__samarkan_password()))

guru = ManusiaMilenial('Klaraa')
guru.set_email('klaraa@gmail.com')
guru.set_pass('rahasia')

guru.info()

programmer = ManusiaMilenial('Ridaa')
programmer.set_email('ridaa@gmail.com')
programmer.set_pass('ridaa123')

programmer.info()