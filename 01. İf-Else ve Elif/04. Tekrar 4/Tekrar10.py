otopark=float(input("Otoparkta kaç saat kalacaksınız:"))

if otopark<=1:
    print("Ödemeniz gerek ücret 5 tl")
elif otopark<5:
    print("Ödemeniz gereken ücret:",otopark*4)
elif otopark>5:
    print("Ödemeniz gereken ücret:",otopark*3)