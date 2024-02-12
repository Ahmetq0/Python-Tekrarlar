import math

toplama = "+"
çikarma = "-"
çarpma = "*"
bölme = "/"
üstlü_çarpma = "**"
Çikiş1 = "q"
Çikiş2 = "Q"
karekök = "K"


while True:
    operation = input("Yapmak istedğiniz işlemi seçiniz:\n"
                      "+: toplama\n"
                      "-: çikarma\n"
                      "*: çarpma\n"
                      "/: bölme\n"
                      "**: üs alma\n"
                      "K: karekök alma\n"
                      "q: çikiş\n"
                      "Q: çikiş2\n")
    
    if operation == Çikiş1 or operation == Çikiş2:
        print("Çikiş yapiliyor.")
        break
    
    
    if operation == karekök:
        number = float(input("Karekök alinacak sayiyi giriniz"))
        if number < 0:
            print("Negatif sayilarin karekökü yoktur.")
        else:
            result = math.sqrt(number)
            print("Karekök sonucu:", result)
    else:
        number1 = float(input("1. sayiyi giriniz: "))
        number2 = float(input("2.sayiyi giriniz: "))
        if operation == toplama:
            print("Toplama sonucu:", number1 + number2)
        elif operation == çikarma:
            print("Çikarma sonucu:", number1 - number2)
        elif operation == çarpma:
            print("Çarpma sonucu:", number1 * number2)
        elif operation == üstlü_çarpma:
            print("Üstalma sonucu:", number1 ** number2)
        elif operation == bölme:
            if number2 == 0:
                print("Sifira bölünemez!")
            else:
                print("Bölme sonucu:", number1/number2)   