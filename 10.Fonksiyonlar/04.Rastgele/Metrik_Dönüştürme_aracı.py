
def boy_girme():
 boy = float(input("Boyunuzu metre cinsinden giriniz\n"))
 return (boy)

def kilo_girme():
 kilo = float(input("Kilonuzu gram cinsinden giriniz\n"))
 return (kilo)


def kilo_boy_kontrol(boy,kilo):
 print(f"Boyunuzu metre cinsinden {boy} metre kilometre cinsinden {boy * 0.001}  hesaplandı")
 print("--"*20)
 print(f"Kilonuz gram cinsinden {kilo} gram kilogram cinsinden {kilo * 0.001} hesaplandı")
 print("--"*20)
 print(f"Antremana başlamadan önce {boy * 0.001} Koşmanızı  {kilo * 0.001} ağırlık çalışmanızı öneririm ")
 
 

boy_değer = boy_girme()
kilo_değer = kilo_girme()
kilo_boy_kontrol(boy_değer,kilo_değer)