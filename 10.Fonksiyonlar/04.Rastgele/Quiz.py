import random

soru1 = [{"soru": "Hangisi Osmanlı devletinin kurucusudur\n",
         "Cevaplar": "A:Osman Bey  B:Melikşah  C:Alparslan  D:SüleymanŞah\n",
         "Doğru Cevap": "A:Osman Bey"},
        {"soru": "Hangisi türk arabasıdır\n",
         "Cevaplar": "A:Togg  B:Bugatti  C:Ferrari  D:Mustang\n",
         "Doğru Cevap": "A:Togg"},   
        {"soru": "Hangisi Güneşe en yakın gezegendir\n",
         "Cevaplar": "A:Venüs  B:Satürn  C:Jüpiter  D:Neptün\n",
         "Doğru Cevap": "C:Jüpiter"}]


total_puan = 0
correct_problems = 0
selected_problems = 0

one_select = "1"
tuo_select = "2"


while True:
    operatin = input("1/Yeni soru için\n"
                     "2/Performans puanı görmek için\n"
                     "Hangi seçeneği seçmek istersiniz\n")
    
    if operatin == tuo_select:
        print("Puanınız:",total_puan)
        print("Doğru Yapılan Sorular:",correct_problems)
        print("Toplam Çözülen Sorulan:",selected_problems)
    
    if operatin == one_select:
     print(soru1)
     print("--"*20)
     reply_selected = input("Cevabı giriniz\n")
     if reply_selected == "A":
         print("Cevabınız Doğru")
         correct_problems + 1
         selected_problems + 1
         total_puan + 1
     else:
         print("Cevabınız Yanlış")
         selected_problems + 1
         
    if operatin == one_select:
        print(soru2)
        print("--"*20)
        reply_selected = input("Cevabı giriniz\n")
        if reply_selected == "A":
            print("Cevabınız Doğru")
            correct_problems + 1
            selected_problems + 1
            total_puan + 1
        else:
            print("Cevabınız Yanlış")
            selected_problems + 1
     