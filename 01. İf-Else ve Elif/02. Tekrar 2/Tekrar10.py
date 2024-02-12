
def otopark_saat_gir():
 otopark=int(input("Otoparkta kaç saat kalacaksınız:"))
 return (otopark)

def otopark_kontrol(otopark):
 if otopark<=1:
    print("Ücret 5 tl")
 elif otopark<=5:
    print("Ücret:",otopark*4)
 elif otopark>5:
    print("Ücret:",otopark*3)
    
otopark_değer = otopark_saat_gir()
otopark_kontrol(otopark_değer)
    

