import random
for i in range(1):
    a = random.randint(0,20)
    sayı= int(input("Bir sayı giriniz:"))
    if sayı < a:
        print("Sayıyı arttır")
        continue
    elif sayı > a:
        print("Sayıyı azalt")
        continue
        