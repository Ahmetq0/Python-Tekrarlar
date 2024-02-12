liste=["B","İ","L","İ","Ş","İ","M"]
liste2=liste.copy()

liste.sort()
print(liste)


liste.reverse()
print(liste)



say=liste.count("İ")
print(say)

liste2.remove("Ş")
print(liste2)

liste.extend(liste2)
print(liste2)

liste2.clear()
print(liste2)

print(liste.index("L"))
