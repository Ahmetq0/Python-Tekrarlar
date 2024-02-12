import random

toplam = 0

def zar_atma(toplam):
 while True:  
    toplam  = random.randint(1,6)
    soru = int(input("Kaç defe zar atmak istersiniz\n"))  
    print("Gelen zar:",toplam)
    continue
 
 
zar_atma(toplam)