
def müşteri_mi_sinemamı_mi():
 müşteri=input("Sinemaya mi yoksa Tiyatroya mi gidecekainiz:")
 öğrenci=input("Öğrenci misisniz?:")
 return (müşteri,öğrenci)

def kontrol(müşteri,öğrenci):
 if müşteri== "Tiyatro":
    print("Tiyatroya Hoşgeldiniz Ücret ",10/2)
 if müşteri== "Sinema":
    print("Sinemaya Hoşgeldiniz Ücret ",15/2)
 if öğrenci== "Hayir":
    print("Öğrenci olmadığınız için Tiyatronun fiyat 15 tl")
    print("Öğrenci olmadığınız için Sinemanın fiyati 10 tl")
    
soru_değer = müşteri_mi_sinemamı_mi()
kontrol(soru_değer[0],soru_değer[1])