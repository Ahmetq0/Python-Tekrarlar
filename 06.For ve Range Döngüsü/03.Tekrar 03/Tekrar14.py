import random

for i in range(1):
    a = random.randint(0,20)
    sayı = int(input("0 ile 20 arasında bir sayı giriniz:"))
    if sayı == a:
        print("Doğru sayı")
        break
    elif sayı > a:
        print("Azalt")
    elif sayı < a:
        print("Arttır")
        