cars_basket = []

total = 0

while True:
    print("Otoparkımıza Hogeldiniz")
    time_selected = int(input("Saat başı ücret 10 tldir\n"
                              "Otoparkımızda kaç saat kalmak istersiniz\n"))

    if time_selected >1:
        total = time_selected*10
        print("--"*20)
        print(time_selected,"Saat kaldınız","Ödemeniz gereken ücret ise",total,"tl dir")
        print("--"*20)