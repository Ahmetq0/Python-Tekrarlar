sayılar=[35,26,81,64]
sayılar2=sayılar.copy()
ondalıklı_sayılar=[1.4]
ondalıklı_sayılar2=[6.8]



sayılar.sort()
print(sayılar)



sayılar.reverse()
print(sayılar)


say=sayılar.count(26)
print(say)


sayılar.remove(81)
print(sayılar)


sayılar.clear()
print(sayılar)


print(sayılar2.index(64))


ondalıklı_sayılar.extend(ondalıklı_sayılar2)
print(ondalıklı_sayılar)