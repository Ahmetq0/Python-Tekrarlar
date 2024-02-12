bagajhakki=float(input("Eşyalarinizin ağirliğini giriniz:\n"))

if bagajhakki<20:
    print("Herhangi bir ücret ödemenize gerek yok")
if bagajhakki>20:
    print("Ödemeniz gereken ek ücret:",bagajhakki +10)