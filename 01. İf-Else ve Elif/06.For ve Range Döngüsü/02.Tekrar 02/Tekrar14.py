import random

for i in range(1):
    a = random.randint(0,21)
    while True:
        sayı = int(input("Bir sayı giriniz:"))
        if sayı == a:
            print("Sayı doğru")
            break
        elif sayı > a:
            print("Sayıyı azalt")
        elif sayı < a:
            print("Sayıyı arttır")
        