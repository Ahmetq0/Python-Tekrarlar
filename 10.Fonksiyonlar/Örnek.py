meyve_list = {"Elma":20, "Armut":30, "Portakal":50, "Mandalina":40, "Muz":70,  "Şeftali":80,  "Çilek":35,  "Karpuz":25,  "Kavun":30}

basket = []

total = 0

def print_dekor():
    print("--"*20)
    return print

def calculate_toplam_price():
    print("Toplam Fiyat:", total)
    return print    

def selected_fruit():
    print("Aldığınız meyve:",selected)
    return print
    
def basket_selected():
    print(basket.append(selected))
    return print

def print_baskett():
    print("Sepetiniz:",selected_meyve,"kg",basket)
    return print


while True:
    for name,price in meyve_list.items():
        print("Aldığınız meyve",name,"Fiyatı",price,"tldir")
    print_dekor()
    selected = input("Almak istediğiniz meyveyi giriniz (Çıkış yapmak istesiniz q veya Q  tıklayınız)\n")
    print_dekor()
    
    if selected == "q" and "Q":
        print("Uygulamadan çıkış yapıldı")
        print_dekor()
        print("Toplam Fiyat:",total)
        print_dekor()
        print("Sepetiniz:",selected_meyve,"kg",basket)
        print_dekor()
        print("Güle Güle")
        break
    
    selected_meyve = int(input("Kaç kilo almak istediğinizi giriniz\n"))
    
    
    
    
    if selected == "Elma":
        total =  selected_meyve * 20
        basket_selected()
        print_dekor()
        selected_fruit()
        print_dekor()
        calculate_toplam_price()
        print_dekor()
        print_baskett()
        print_dekor()
    
    
    
    elif selected == "Armut":
        total = selected_meyve * 30
        basket_selected()
        print_dekor()
        selected_fruit()
        print_dekor()
        calculate_toplam_price()
        print_dekor()
        print_baskett()
        print_dekor()
    
    
    elif selected == "Mandalina":
        total = selected_meyve * 40
        basket_selected()
        print_dekor()
        selected_fruit()
        print_dekor()
        calculate_toplam_price()
        print_dekor()
        print_baskett()
        print_dekor()
    
    
        
    elif selected == "Portakal":
        total = selected_meyve * 50
        basket_selected()
        print_dekor()
        selected_fruit()
        print_dekor()
        calculate_toplam_price()
        print_dekor()
        print_baskett()
        print_dekor()
    
    
        
    elif selected == "Muz":
        total = selected_meyve * 70
        basket_selected()
        print_dekor()
        selected_fruit()
        print_dekor()
        calculate_toplam_price()
        print_dekor()
        print_baskett()
        print_dekor()
        
    elif selected == "Şeftali":
        total = selected_meyve * 80
        basket_selected()
        print_dekor()
        selected_fruit()
        print_dekor()
        calculate_toplam_price()
        print_dekor()
        print_baskett()
        print_dekor()
        
    elif selected == "Çilek":
        total = selected_meyve *35
        basket_selected()
        print_dekor()
        selected_fruit()
        print_dekor()
        calculate_toplam_price()
        print_dekor()
        print_baskett()
        print_dekor()
        
    elif selected == "Karpuz":
        total = selected_meyve *25
        basket_selected()
        print_dekor()
        selected_fruit()
        print_dekor()
        calculate_toplam_price()
        print_dekor()
        print_baskett()
        print_dekor()
        
    elif selected == "Kavun":
        total = selected_meyve *30
        basket_selected()
        print_dekor()
        selected_fruit()
        print_dekor()
        calculate_toplam_price()
        print_dekor()
        print_baskett()
        print_dekor()