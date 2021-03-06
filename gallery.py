import time


class araba():
    galeriAdı = "Backyard Galeri"
    aracSayısı = 0
    aracID = 10000

    def __init__(self, marka="Girilmedi", model="Girilmedi", yıl="Girilmedi", renk="Girilmedi"):
        self.marka = marka
        self.model = model
        self.yıl = yıl
        self.renk = renk
        araba.aracSayısı += 1
        araba.aracID += 11
        self.aracID = araba.aracID
        self.index = -1

    def zamanHesapla(fonk):
        def wrapper(*args, **kwargs):
            baslangicZamani = time.time()
            fonk
            bitisZamani = time.time()
            print("Bu işlem toplam {} saniye sürdü:".format(bitisZamani - baslangicZamani))

        return wrapper

    @zamanHesapla
    def renkDegistir(self, yeniRenk):
        self.renk = yeniRenk

    def __str__(self):
        return f"Arabanın markası: {self.marka} \nArabanın Modeli: {self.model} \nArabanın Yılı: {self.yıl} \n,Arabanın Rengi: {self.renk} \n"

    def __len__(self):
        return self.yıl

    @zamanHesapla
    def __add__(self, other):
        return self.yıl + other.yıl

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.marka):
            return self.marka[self.index]
        else:
            self.index = -1
            raise StopIteration

    def aGenerator(self):
        for i in range(1, self.yıl):
            yield 2 * i

    @classmethod
    def aracSayısınıSoyle(cls):
        return cls.aracSayısı

    @staticmethod
    def galeriAdınıSoyle():
        return araba.galeriAdı


arac1 = araba("Renault", "Megane", 2015, "Beyaz")

arac2 = araba("Fiat", "Linea", 2017, "Kırmızı")

araba.galeriAdı
araba.aracSayısı
arac1.aracID

arac1.renkDegistir("Mor")
print(arac1)  # Artık rengi siyah :)

arac1 + arac2  # Yıllarının toplamını gösterecek.

iterator9 = iter(arac2)
for i in arac1:
    print(i)

print("--------")
while True:
    try:
        i = next(iterator9)
        print(i)

    except StopIteration:
        break

araba.aracSayısınıSoyle()
araba.galeriAdınıSoyle()

generator = arac1.aGenerator()
iterator10 = iter(generator)
next(iterator10)

arac1.renkDegistir("Siyah")

arac1 + arac2
