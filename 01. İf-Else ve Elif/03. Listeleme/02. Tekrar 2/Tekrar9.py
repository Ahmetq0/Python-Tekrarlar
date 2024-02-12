Sayılar=["35","26","81","64"]
Sayılar2=Sayılar.copy()
ondalıklı_sayılar=["1.4","6.8"]

Sayılar.sort()
print(Sayılar)

Sayılar.reverse()
print(Sayılar)


say=Sayılar.count("26")
print(say)

Sayılar.remove("81")
print(Sayılar)

Sayılar.clear()
print(Sayılar)

print(Sayılar2.index("64"))

Sayılar2.extend(ondalıklı_sayılar)
print(Sayılar2)

