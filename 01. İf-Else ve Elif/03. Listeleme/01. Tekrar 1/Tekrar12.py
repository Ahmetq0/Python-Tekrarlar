onemli_telefonlar = ["Acil Çağrı Merkezi""112", "Polis İmdat""155", "Milli Eğitim Bakanlığı İletişim Merkezi""444 0 632" ]
onemli_telefonlar2=onemli_telefonlar.copy()


print(onemli_telefonlar)




onemli_telefonlar.clear()


onemli_telefonlar2.remove("Acil Çağrı Merkezi""112")
print(onemli_telefonlar2)


if "Sağlık Bakanlığı İletişim Merkezi" in onemli_telefonlar2:
    print("Var")
else:
    print("Yok")


onemli_telefonlar2.clear()
print(onemli_telefonlar2)