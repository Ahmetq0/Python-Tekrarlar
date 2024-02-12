hasta_list = []


def hasta_kayıt():
    name = input("Hastanın adını giriniz\n")
    print(name,"Adlı hastanın kaydı açılmıştır")
    hasta_list.append(name)
    
    
def hasta_sorgulama():
    name = input("Hastanın adını giriniz\n")
    if name in hasta_list:
        print("Böyle bir hasta vardır")
    else:
        print("Böyle bir hasta mevcut değildir")
        
        
        
def hasta_çıkış():
    quit_name = input("Çıkarmak istediğiniz hastanın adını giriniz\n")
    if quit_name in hasta_list:
        hasta_list.remove(quit_name)
        print(quit_name,"Adlı hastanın çıkışı yapılmıştır")
        