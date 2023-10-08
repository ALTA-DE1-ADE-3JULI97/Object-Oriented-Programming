# tulis solusi code disini
class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    
    def hitung_luas(self):
        return self.sisi * self.sisi
    
    def hitung_keliling(self):
        return 4 * self.sisi

class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi
    
    def hitung keliling(self):
        return self.alas + self.tinggi + ((self.alas**2 + self.tinggi**2)**0.5)

class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def hitung_luas(self):
        return self.panjang * self.lebar
    
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

def main():
    persegi = Panjang(4)
    segitiga = Segitiga(3, 4)
    persegi_panjang = PersegiPanjang(7, 8)

    print("Luas")
    print("Persegi: ", persegi.hitung_luas())
    print("Segitiga: ", segitiga.hitung_luas())
    print("Persegi Panjang: ", persegi_panjang.hitung_luas())

    print("Keliling")
    print("Persegi: ", persegi.hitung_keliling())
    print("Segitiga: ", segitiga.hitung_keliling())
    print("Persegi Panjang: ", persegi_panjang.hitung_keliling())

if __name__ == "__main__":
    main()