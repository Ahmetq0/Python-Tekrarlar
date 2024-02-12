
def sayı_yaz():
 sayı_list = {8,5,22,3}
 return (sayı_list)


en_büyük_sayı = sayı_list[0]

def sayı_kontrol(sayı_list):
 for i in sayı_list:
    if en_büyük_sayı > i:
        en_büyük_sayı = i
        return en_büyük_sayı
    
sayı_değer = sayı_yaz()
sayı_kontrol(sayı_değer,en_büyük_sayı)    

    
