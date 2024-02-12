
def işlemci_and_ram_gir():
 işlemci=input("İşlemciyi giriniz:")
 ram=input("Rami giriniz:")
 return (işlemci,ram)

def işlemci_and_ram_kontrol(işlemci,ram):
 if işlemci == "i7" and ram == "16gb":
    print("Kurulum Başarılı")
 else:
    print("Kurulum Başarısız")
    
işlemci_ve_ram_değer = işlemci_and_ram_gir()
işlemci_and_ram_kontrol(işlemci_ve_ram_değer[0],işlemci_ve_ram_değer[1])