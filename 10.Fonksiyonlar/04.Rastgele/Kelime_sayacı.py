def kelime_gir():
 text = input("Metin giriniz\n")
 return (text)

def kelime_sayma(text):
 world = text.split()
 world_number = len(world)
 print("Yazdığınız toplam kelime sayısı:",world_number)
 

kelime_değer = kelime_gir()
kelime_sayma(kelime_değer)