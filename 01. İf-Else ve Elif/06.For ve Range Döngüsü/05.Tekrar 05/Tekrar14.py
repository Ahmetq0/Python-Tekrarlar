import random
sayı = int(input("1 ile 20 arasında sayı giriniz:"))

for i in range(1):
    a = random.randint(0,20)
    if sayı< a:
        print("Sayıyı arttır")
        
    elif sayı> a:
        print("Sayıyı azalt")
    
    elif sayı == a:
        print("Doğru sayı")
        break
