n1= int(input("Birinci sayıyı giriniz:"))
n2= int(input("İkinci sayıyı giriniz:"))

total = 0

for i in range(n1,n2):
    total = (total + n1)
    n1 += 1
print(total)