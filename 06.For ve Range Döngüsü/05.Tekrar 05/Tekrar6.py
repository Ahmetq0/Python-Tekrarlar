n1 = int(input("Birinci notunuzu giriniz:"))
n2 = int(input("İkinci notunuzu giriniz:"))

total = 1

for i in range(1,n1,n2):
    total += n1
    divide = total / n1
    print(total)