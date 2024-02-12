Sözlük=["Bilim İnsanı""Aziz Sancar", "Şair","Mehmet Akif Ersoy", "Astronom""Ali Kuşçu"]

meslekler=Sözlük.copy()



print(meslekler)


print(Sözlük)


Sözlük.clear()
print(Sözlük)

meslekler.append("Matematikçi: Cahit Arf")
print(meslekler)


if "Sanatçı" in meslekler:
    print("Sanatçı var")

else:
    print("Öyle bir kelime yok")


meslekler[0]= "Canan Dağdeviren"
print(meslekler)

if "Şair" in meslekler:
    print("Mehmet Akif Ersoy")