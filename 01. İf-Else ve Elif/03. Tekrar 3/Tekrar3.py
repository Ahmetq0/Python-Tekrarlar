
def bagaj_ağırlığı_gir():
 bagaj_agirligi = int(input("Bagaj ağırlığını giriniz (kg): "))
 return (bagaj_agirligi)


def baga_kontrol(bagaj_agirligi):
 if bagaj_agirligi <= 20:
    print("Herhangi bir ücret ödemeniz gerekmiyor.")
 else:

    ek_ucret = (bagaj_agirligi - 20) * 10
    print("Fazla bagaj için", ek_ucret, "TL ödemelisiniz.")
    
bagaj_değer = bagaj_ağırlığı_gir()
baga_kontrol(bagaj_değer)