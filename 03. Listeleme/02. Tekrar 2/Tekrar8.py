Ders=["B","İ","L","İ","Ş","İ","M"]
ders2=Ders.copy()
alanlistesi=Ders.copy()

Ders.sort()
print(Ders)


Ders.reverse()
print(Ders)


say=Ders.count("İ")
print(say)


ders2.remove("Ş")


ders2.pop(4)
print(ders2)

print(alanlistesi)


alanlistesi.clear()
print(alanlistesi)


print(ders2.index("L"))
