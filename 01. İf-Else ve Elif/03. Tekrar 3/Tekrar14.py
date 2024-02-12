
def number_selected():
 number1=float(input("Birinci sayiyi giriniz:\n"))
 number2=float(input("İkinci sayiyi giriniz:\n"))
 number3=float(input("Üçüncü sayiyi giriniz:\n"))
 return (number1,number2,number3)


def number_control(number1,number2,number3):
 enbüyüksayi=max(number1,number2,number3)
 if enbüyüksayi:
    print("En büyük sayi",enbüyüksayi)
    
number_değer = number_selected()
number_control(number_değer[0],number_değer[1],number_değer[2])