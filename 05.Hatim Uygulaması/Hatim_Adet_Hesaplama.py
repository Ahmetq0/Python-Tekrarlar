print("Hatim Hesaplama Uygulamasına Hoşgeldiniz")

hatim=input("Hangi hatimi yaptırmak istersiniz:")
adet=float(input("Halkada kaç kişi var:"))

if hatim== "Yasini Şerif Hatmi":
    print("Yasin şerif hatimi için: ",adet /41)
elif hatim== "İhlas Hatimi":
    print(f"İhlas Hatimi için okunacak {adet}:",adet %100== 4)
elif hatim== "Ayetel Kürsi":
    print("Ayetel kürsi hatimi için:",adet /313)