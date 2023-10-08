# tulis solusi code disini
class Kalkulator:
    def penjumlahan(self, x, y):
        return x + y
    
    def pengurangan(self, x, y):
        return x - y
    
    def perkalian(sself, x, y):
        return x * y
    
    def pembagian(self, x, y):
        return x / y

def main():
    kalkulator = Kalkulator()

    angka1 = 5
    angka2 = 6

    hasil_penjumlahan = kalkulator.penjumlahan(angka1, angka2)
    hasil_pengurangan = kalkulator.pengurangan(angka1, angka2)
    hasil_perkalian = kalkulator.perkalian(angka1, angka2)
    hasil_pembagian = kalkulator.pembagian(angka1, angka2)

    print("Penjumlahan: ", hasil_penjumlahan)
    print("Pengurangan: ", hasil_pengurangan)
    print("Perkalian: ", hasil_perkalian)
    print("Pembagian: ", hasil_pembagian)

if __name__ == "__main__":
    main()