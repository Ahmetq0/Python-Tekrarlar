def parkingmoney():
    x = int(input("Kaç saat kalackasınız\n"))
    return x

def selected_money():
    if parkingmoney <1:
        total =  + 5
        print("Ödemeniz gereken ücret:",total)
        return selected_money

parkingmoney()
selected_money()