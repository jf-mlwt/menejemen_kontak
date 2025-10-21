print("Nama saya Jana")
def halo():
    print("Halooo")

def halo2():
    return "Kenyang"

var = halo2()
for i in var:
  print(var[:4])

def luas_persegi(sisi):
    luas = sisi*sisi
    print(f'Luas persegi dengan sisi {sisi} adalah {luas}')

luas_persegi(5)

def genap(nilai):
    if nilai%2 == 0:
        print("Angka ini adalah genap")
    else:
        print("Angka ini adalah ganjil")

genap(9)

#Menghitung huruf fokal#
def huruf_vokal(var):
    total = 0
    for i in var:
        if i in 'aiueoAIUEO':
            total +=1
    return total

huruf_vokal("Muhammad Fauzi")