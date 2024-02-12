müşteri=input("Sinemaya mi yoksa Tiyatroya mi gidecekainiz:")
öğrenci=input("Öğrenci misisniz?:")

if müşteri== "Tiyatro":
    print("Tiyatroya Hoşgeldiniz Ücret ",10/2)
if müşteri== "Sinema":
    print("Sinemaya Hoşgeldiniz Ücret ",15/2)
if öğrenci== "Hayir":
    print("Öğrenci olmadığınız için Tiyatronun fiyat 15 tl")
    print("Öğrenci olmadığınız için Sinemanın fiyati 10 tl")