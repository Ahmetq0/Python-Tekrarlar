number1 = int(input("Birinci notunuzu giriniz:"))
number2 = int(input("İkinci notunuzu giriniz:"))

total = 1


for i in range(1,number1,number2):
    total += number1
    divede = total / i
    print(divede)
