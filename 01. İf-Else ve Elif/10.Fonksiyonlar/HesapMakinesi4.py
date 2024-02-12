import math


while True:
    selected = input("1/Toplama\n"
                     "2/Çıkarma\n"
                     "3/Çarpma\n"
                     "4/Bölme\n"
                     "5/Üslüçarpma\n"
                     "6/Karekök\n"
                     "Çıkış\n"
                     "Yapmak istediğiniz işlemi giriniz\n")
    
    if selected == "q":
        print("Uygulamadan çıkış yapıldı")
        break

    else:
        x = int(input("Birinci sayıyı giriniz\n"))
        y = int(input("İkinci sayıyı giriniz\n"))

        def Toplama(x,y):
            total = x + y
            print("--"*20)
            print("İşleminizin sonucu:",total)
            print("--"*20)
        
        def Çıkarma(x,y):
            total = x - y
            print("--"*20)
            print("İşleminizin sonucu:",total)
            print("--"*20)
        
        def Çarpma(x,y):
            total = x * y
            print("--"*20)
            print("İşleminizin sonucu:",total)
            print("--"*20)
        
        def bölme(x,y):
            total = x / y
            print("--"*20)
            print("İşleminizin sonucu:",total)
            print("--"*20)
        
        def Üslüçarpma(x,y):
            total = x ** y
            print("--"*20)
            print("İşleminizin sonucu:",total)
            print("--"*20)

        def Karekök(x):
            total = math.qsrt(x)
            print(total)
            
        if selected == "1":
            Toplama(x,y)
        
        elif selected == "2":
            Çıkarma(x,y)

        elif selected == "3":
            Çarpma(x,y)
        
        elif selected == "4":
            bölme(x,y)
        
        elif selected == "5":
            Üslüçarpma(x,y)
        
        elif selected == "6":
            Karekök(x)
            