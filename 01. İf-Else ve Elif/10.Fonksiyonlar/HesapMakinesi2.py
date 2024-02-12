import math

while True:
    selected = input("1/Toplama\n"
                     "2/Çıkarma\n"
                     "3/Çarpma\n"
                     "4/Bölme\n"
                     "5/Üslüçarpma\n"
                     "6/Karekök\n"
                     "Çıkış\n"
                     "Hangi işlemi yapmak istersiniz\n")
    
    def karekök(x):
        total = math.sqrt(x)
        print("--"*20)
        print("İşlemin Sonucu:",total)
        print("--"*20)
    
    if selected == "q":
        print("Uygulamadan çıkış yapıldı")
        break
    
    x = float(input("Birinci sayıyı giriniz\n"))
    if  selected == "6":
      karekök(x)
      continue
    

    y = float(input("İkinci sayıyı giriniz\n"))

    def Toplama(x,y):
            total = x + y
            print("--"*20)
            print("İşlemin Sonucu:",total)
            print("--"*20)

    def Çıkarma(x,y):
            total = x - y
            print("--"*20)
            print("İşlemin Sonucu:",total)
            print("--"*20) 

    def Çarpma(x,y):
            total = x * y
            print("--"*20)
            print("İşlemin Sonucu:",total)
            print("--"*20)
        
    def bölme(x,y):
            total = x / y
            print("--"*20)
            print("İşlemin Sonucu:",total)
            print("--"*20)

    def üslüçarpma(x,y):
           total = x ** y
           print("--"*20)
           print("İşlemin Sonucu:",total)
           print("--"*20)

    if selected == "1":
            Toplama(x,y)
        
    elif selected == "2":
            Çıkarma(x,y)
        
    elif selected == "3":
            Çarpma(x,y)
        
    elif selected == "4":
            bölme(x,y)
      
    elif selected == "5":
           üslüçarpma(x,y)

