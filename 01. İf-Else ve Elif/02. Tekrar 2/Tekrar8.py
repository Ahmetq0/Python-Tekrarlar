
def plaka():
 plaka=input("Plakayı giriniz:")
 return (plaka)

def plaka_kontrol(plaka):
 if plaka== "06":
    print("Ankaraya Hoşgeldiniz")
 elif plaka== "07":
    print("Antalyaya Hoşgeldiniz")
 elif plaka== "08":
    print("Artvine Hoşgeldiniz")
 else:
    print("Türkiyeye Hoşgeldiniz")
    
plaka_değer = plaka()
plaka_kontrol(plaka_değer)
    
    