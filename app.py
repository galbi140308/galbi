print("## program python menghitung luas segitiga")
print("==========================================")
print()

def hitungluassegitiga(a,t):
    return round(0,5*a*t,2)

alas = float(input("input alas segitiga"))
tinggi = float(input("tinggi segitiga"))

print('luas segitiga =',hitungluassegitiga(alas,tinggi))
print()

print("## program python menghitung panjang persegi")
print("==========================================")
print()

def hitungpersgipanjang(p,l):
    return round(p*l,2)

panjang=float(input("input panjang : "))
lebar=float(input("input lebar : "))
print('luas persegi panjang =',hitungpersegipanjang(panjang,lebar))