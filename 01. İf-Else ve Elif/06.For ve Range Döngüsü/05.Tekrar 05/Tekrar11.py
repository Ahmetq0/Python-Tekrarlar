sayı = input("1 ile 5 arasında rakam giriniz:")

for i in sayı:
    if sayı == "3":
        print("3 rakamı girildiği için döngüden çıkıldı")
        break
    else:
        print("Yanlış rakamı girdiniz")
        break