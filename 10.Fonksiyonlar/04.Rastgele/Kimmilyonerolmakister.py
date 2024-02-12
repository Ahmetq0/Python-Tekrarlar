soru = [{"Soru:" "Hangi renk trafik ışığının ortasında yer alır:""A:Yeşil B:Kırmızı  C:Mavi D:Sarı\n"
         "Soru2:" "Hangi gezegen güneş sistemindeki en büyük gezegendir:""A:Mars B:Jupiter C:Satürn D:Venüs\n"
         "Soru3:" "Hangi araba türk arabasıdır:""A:Togg B:Mustang C:BMW D:Supra\n"
         "Soru4:" "Hangi ders sayısaldır:""A:Matematik B:Türkçe C:Sosyal D:Coğrafya\n"}]
print("Sorular:",soru)

for i in range(4):
    soru = input("Sorunun cevabını giriniz\n")
    if soru == "D" or soru == "D" or soru == "A" or soru == "A":
            print("Tebrikler soruyu bildiniz")
    else:
        print("Cevabınız Yalnış")
    
