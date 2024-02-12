number1=int(input("Birinci sayiyi giriniz:"))
number2=int(input("İkinci sayiyi giriniz:"))


total = 1



for number in range(1,number1 + number2):
    total += number
    divide = total / number
print(divide)