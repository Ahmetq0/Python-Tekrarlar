
def ürün_girme():
 ürün1=float(input("Birinci ürünün fiyatını giriniz:\n"))
 ürün2=float(input("İkinci ürünün fiyatını giriniz:\n"))
 return (ürün1,ürün2)

def ürün_toplam(ürün1,ürün2):
 toplam=(float(ürün1)+float(ürün2))
 if toplam<200:
    print("Ödemeniz gereken miktar:",toplam)
 if toplam>200:
    print("İndirimden sonra ödemeniz gereken miktar:",toplam/4)
    
    
    
ürün_değer = ürün_girme()
ürün_toplam(ürün_değer[0],ürün_değer[1])
    
