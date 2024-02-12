
def plaka_gir():
 plaka=input("Plakanızı giriniz:")
 return (plaka)

def plaka_kontrol(plaka):
 if plaka== "06":
    print("Ankara")
 elif plaka== "07":
    print("Antalya")
 elif plaka== "08":
    print("Artvin")
 else:
    print("Türkiye")
    
plaka_değer = plaka_gir()
plaka_kontrol(plaka_değer)