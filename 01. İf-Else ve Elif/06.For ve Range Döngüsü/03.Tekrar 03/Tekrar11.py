number = input("1 ile 5 arasında bir sayı giriniz:")


for i in number:
    if number == "3":
        print("3 sayısı girildi ve döngü sona erdi")
    break
else:
    print("Yanlış sayı girildi")
    