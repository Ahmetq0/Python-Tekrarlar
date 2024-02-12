

def sayı_gir():
 number1=float(input("Birinci sayiyi giriniz:\n"))
 number2=float(input("İkinci sayiyi giriniz:\n"))
 number3=float(input("Üçüncü sayiyi giriniz:\n"))
 return (number1,number2,number3)




def enbüyük_sayı_kontrol(number1,number2,number3):
 enbüyüksayi=max(number1,number2,number3)
 print("En büyük sayi",enbüyüksayi)
 
sayı_değer = sayı_gir()
enbüyük_sayı_kontrol(sayı_değer[0],sayı_değer[1],sayı_değer[2])