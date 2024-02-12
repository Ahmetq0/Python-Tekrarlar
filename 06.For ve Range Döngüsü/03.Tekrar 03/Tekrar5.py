number1= int(input("Birinci sayıyı giriniz:"))
number2= int(input("İkinci sayiyi giriniz:"))

total= 0


for i in range(number1,number2):
    total = (total + number1)
    number1 += 1
    print(total)
