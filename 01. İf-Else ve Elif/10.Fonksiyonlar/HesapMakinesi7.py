import math

while True:
    selected = input("1/Toplama\n"
                     "2/Çıkarma\n"
                     "3/Çarpma\n"
                     "4/Bölme\n"
                     "5/ÜslüÇarpma\n"
                     "6/Karekök\n"
                     "Çıkış\n"
                     "Hangi işlemi yapmak istersiniz\n")
    
    if selected == "q":
        print("Uygulamadan çıkış yapıldı")
        break
    
    else:
        n1 = float(input("Birinci sayıyı giriniz\n"))
        n2 = float(input("İkinci sayıyı giriniz\n"))
        
        
        def dekor_selected():
            print("--"*20)
            return print
        
        
        def toplama(n1,n2):
            total = n1 + n2
            print("İşleminizin Sonucu:",total)
            dekor_selected()
            
        def çıkarma(n1,n2):
            total = n1 - n2
            print("İşleminiz Sonucu:",total)
            dekor_selected()
            
        def çarpma(n1,n2):
            total = n1 * n2
            print("İşleminiziz Sonucu:",total)
            dekor_selected()
            
        def bölme(n1,n2):
            total = n1 /n2
            print("İşleminiz Sonucu:",total)
            dekor_selected()
            
        def ÜslüÇarpma(n1,n2):
            total = n1 ** n2
            print("İşleminizin Sonucu:",total)
            dekor_selected()
            
        def karekök(n1):
            total = math.sqrt(n1)
            print("İşleminizin Sonucu:",total)
            dekor_selected()
            
        if selected == "1":
            toplama(n1,n2)
            
        elif selected == "2":
            çıkarma(n1,n2)
        
        elif selected == "3":
            çarpma(n1,n2)
            
        elif selected == "4":
            bölme(n1,n2)
            
        elif selected == "5":
            ÜslüÇarpma(n1,n2)
            
        elif selected == "6":
            karekök(n1)            
            