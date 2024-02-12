n1 = int(input("Birinci sayıyı giriniz:"))
n2 = int(input("İkinci sayiyi giriniz:"))

Total = 1

for i in range(1,n1,n2):
    Total += n1
    divide = Total / i
    print(divide)