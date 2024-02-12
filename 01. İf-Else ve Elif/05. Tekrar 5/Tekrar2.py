kenar1=float(input("Birinci değeri yazınız:"))
kenar2=float(input("İkinci değeri yazınız:"))
kenar3=float(input("Üçüncü değeri yazınız:"))

if kenar1== kenar2== kenar3:
    print("Eşkenar üçgen")
elif kenar1== kenar2:
    print("İkizkenar üçgen")
else:
    print("Çeşitkenar üçgen")