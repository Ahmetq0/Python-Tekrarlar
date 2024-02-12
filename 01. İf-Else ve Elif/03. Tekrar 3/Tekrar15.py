
def cinema_and_tiyatro_selected():
 müşteri=input("Sinemaya mi yoksa Tiyatroya mi gidecekainiz:")
 öğrenci=input("Öğrenci misisniz?:")
 return (müşteri,öğrenci)


def cinema_and_tiyatro_control(müşteri,öğrenci):
 if müşteri== "Tiyatro":
    print("Tiyatroya Hoşgeldiniz Ücret ",10/2)
 if müşteri== "Sinema":
    print("Sinemaya Hoşgeldiniz Ücret ",15/2)
 if öğrenci== "Hayir":
    print("Öğrenci olmadığınız için Tiyatronun fiyat 15 tl")
    print("Öğrenci olmadığınız için Sinemanın fiyati 10 tl")
    
cinema_and_tiyatro_değer = cinema_and_tiyatro_selected()
cinema_and_tiyatro_control(cinema_and_tiyatro_değer[0],cinema_and_tiyatro_değer[1])