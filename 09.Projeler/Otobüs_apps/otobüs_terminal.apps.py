import Otobüs_terminal_engine


print("Uygulamamıza Hoşgeldiniz")



while True:
    print("1/Şehir seçim yapmak isterseniz\n"
          "2/Firma seçim yapmak isterseniz\n"
          "3/Fatura Görmek isterseniz")
    selected = int(input("Yapmak istediğiniz işlemi seçiniz\n"))
    
    
    if selected == 1:
        Otobüs_terminal_engine.müşterinin_gitmek_istediği_şehir()
    
    if selected == 2:
        Otobüs_terminal_engine.müşterinin_seçtiği_otobüs()
        buss_selected = input("Seçiminizi yapınız\n")
        
    if selected == 3:
        Otobüs_terminal_engine.fatura(buss_selected,selected)      


    Otobüs_terminal_engine.otobüs_fatura(buss_selected)