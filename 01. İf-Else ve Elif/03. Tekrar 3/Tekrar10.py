
def otoparkta_kaç_saat_kalacaksınız():
 otopark=float(input("Kaç saat kalacaksınız:"))
 return (otopark)


def saat_kontrol(otopark):
 if otopark<=1:
    print("Ödemeniz gereken ücret 5 tl")
 elif otopark<=5:
    print("Ödemeniz gereken ücret :",otopark*4)
 elif otopark>5:
    print("Ödemeniz gereken ücret:",otopark*3)
    
    
otopark_değer = otoparkta_kaç_saat_kalacaksınız()
saat_kontrol(otopark_değer)