
def işlemci_ram_selected():
 işlemci=input("İşlemciyi giriniz:")
 ram=input("Rami giriniz:")
 return (işlemci , ram)

def işlemi_ve_ram_kontrol(işlemci,ram):
 if işlemci== "i7" or ram == "16gb":
    print("Kurulum Başarılı")
 else:
    print("Kurulum başarısız")
    
işlemci_ram_değer = işlemci_ram_selected()
işlemi_ve_ram_kontrol(işlemci_ram_değer[0],işlemci_ram_değer[1])
    
    
