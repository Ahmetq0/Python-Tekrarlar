
def bagajhakkı_gir():
 bagaj_hakki=float(input("Eşya yükünüzü giriniz:\n"))
 return (bagaj_hakki)


def bagaj_hakkı_kontrol(bagaj_hakki):
 if bagaj_hakki<20:
    print("Ödemeniz gerek herhangi bir ücret yoktur")
 if bagaj_hakki>20:
    print("Fazla bagaj hakkı için ödemeniz gerek miktar :",bagaj_hakki*1+10)
    
bagaj_değer = bagajhakkı_gir()
bagaj_hakkı_kontrol(bagaj_değer)