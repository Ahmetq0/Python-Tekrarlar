kenar1=float(input("Birinci kenar değerini giriniz:"))
kenar2=float(input("İkinci kenar değerini giriniz:"))
kenar3=float(input("Üçüncü kenar değerini giriniz:"))


if kenar1 == kenar2 == kenar3:
    print("Eşkenar üçgen")
elif kenar1== kenar2 and kenar2== kenar3 and kenar1== kenar3:
    print("İkizkenar üçgen")
else:
    print("Çeşitkenar üçgen")