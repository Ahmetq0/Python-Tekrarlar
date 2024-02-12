total = 0

buss_list = {"PamukkaleTruzim":300 , "VaranTruzim": 400 , "AnadoluTruzim":500 , "EfeTur":200 , "KamilKoç":600 , "HasTruzim":700}


def müşterinin_gitmek_istediği_şehir():
    selected = input("Gitmek istediğiniz şehiri giriniz\n")
    kişi_sayısı = int(input("Kaç kişi olduğunuzu giriniz\n"))
    return selected,kişi_sayısı
    
def müşterinin_seçtiği_otobüs():
    for i in buss_list:
        print(i)
    buss_selected = input("Seçiminizi yapınız\n")
    return buss_selected
    

def otobüs_fatura(buss_selected):
    if buss_selected == "PamukkaleTruzim":
        total + 300
    if buss_selected == "VaranTruzim":
        total + 400
    if buss_selected == "AnadoluTruzim":
        total + 500
    if buss_selected == "EfeTur":
        total + 200
    if buss_selected == "KamilKoç":
        total + 600
    if buss_selected == "HasTurizm":
        total + 700
        
        
def fatura(kişi_sayısı,selected,buss_selected):
    print(selected,"Şehire",kişi_sayısı,"Kişi ile",buss_selected,"Otobüs Firması ile Biletiniz Kesildi") 
    print("--"*20)
    print("Ödemeniz Gereken Ücret:",total)
    
