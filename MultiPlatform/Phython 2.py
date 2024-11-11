#Nomor 1
nilai= input("Berapa nilai murid? ")
if int(nilai) >= 90 :
    print("Excellent Performance!")
elif int(nilai) >= 80 :
    print("Very Good Performance!")
elif int(nilai) >= 70 :
    print("Good Performance!")
elif int(nilai) >= 60 :
    print("Average Performance")
else : print("Nice Try!")

#Nomor 2
nomor1 = int(input("Angka 1 = "))
nomor2 = int(input("Angka 2 = "))
nomor3 = int(input("Angka 3 = "))
besar=max(nomor3, nomor2, nomor1)
print("Angka Terbesar Adalah :",besar)

#Nomor 3
deret = int(input("Masukan Deret = "))
a, b = 0, 1
hasil = []
while a <= deret :
    hasil.append(a)
    a, b = b, a + b
print(hasil)


#Nomor 4
batas = int(input("Masukan batas maksimal bilangan = "))
OddNumber = [n for n in range(1, batas+1) if  n %2 != 0]
print(OddNumber)

#Nomor 5
angkas = int(input("Angka = "))
for n in range(1, angkas + 1 ) :
    print(str(n) * n)

