#1
def suhu (temperatur , unit) :
    if unit == "C" :
        print(f"Konversi ke Fahrenhait : {temperatur + 32} ")
    elif unit == "F" :
        print(f"Konversi ke Celcius : {temperatur - 32}")
    else :
        print("Pilihan hanya bisa C/F")

T = int(input("Berapa Temperatur? "))
U = input("Apa Unitnya? ")
suhu(T , U)

#2
r = int(input("Masukan r = "))
Area = lambda r : 3.14 * r * r
print(Area(r))