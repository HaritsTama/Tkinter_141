class PersegiPanjang :
    def __init__(self, panjang, lebar) :
        self.panjang = panjang
        self.lebar = lebar
    
    def Keliling(self) :
        return self.panjang + self.panjang + self.lebar + self.lebar

    def Luas(self) :
        return self.panjang * self.lebar
    
    def __str__(self) :
        return f"Panjang : {self.panjang} cm, Lebar : {self.lebar} cm"



def main() :
    try :
        P = float(input("Berapa Panjang : "))
        L = float(input("Berapa Lebar : "))
        if P <= 0 or L <= 0 :
            print("Value Harus Positif")
            return
        pp = PersegiPanjang(P, L)
        print(pp)
        print("Kelilingnya : ",  pp.Keliling())
        print("Luasnya : ", pp.Luas())
        
    except ValueError :
        print("Salah")

main()


