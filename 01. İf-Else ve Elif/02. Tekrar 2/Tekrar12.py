
def boy_kilo_gir():
 boy=float(input("Boyunuzu giriniz:"))
 boy1=float(input("Boyunuzu giriniz:"))
 kilo=float(input("Kilonuzu giriniz:"))
 vki=(float(boy)*float(boy1)/float(kilo))
 return (vki)


def vki_kontrol(vki):
 if vki>=18<=25:
    print("Normal")
 elif vki<=30:
    print("Kilolu")
 elif vki<=35:
    print("Obez")
 elif vki>35:
    print("Ciddi obez")
    
    
    
    
vki_değer = boy_kilo_gir()
vki_kontrol(vki_değer)