
def sıcaklık_değer_gir():
 sıcaklık=float(input("Hava sıcaklığını giriniz:"))
 return sıcaklık

def sıcaklık_kontrol(sıcaklık):
 if sıcaklık<5:
    print("Hava soğuk")
 elif sıcaklık<=14:
    print("Hava ılık")
 elif sıcaklık>15:
    print("Hava sıcak")
    

sıcaklık_değer = sıcaklık_değer_gir()
sıcaklık_kontrol(sıcaklık_değer)
