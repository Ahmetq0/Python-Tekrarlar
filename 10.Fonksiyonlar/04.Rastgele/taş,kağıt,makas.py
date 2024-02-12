import random
while True:
 def karşı_bilgisayar_liste():
  selected_liste = ["M","K","T","Kertenkele","Spoc"]
  return selected_liste





 print(karşı_bilgisayar_liste())
 def seçim_yapma():
  seçim = input("Seçiminizi yapınız\n")
  return (seçim)

   
 for i in random.choices(karşı_bilgisayar_liste()):
        karşı_pc = random.choices(karşı_bilgisayar_liste())
        print(i)

        def seçim_kontrol(seçim):
         if i == seçim:
            print("Berabere")
            
         if  seçim == "K" and  i == "T":
            print("Kazandınız")
         if seçim == "M" and  i == "K":
            print("Kzandınız")
         if seçim == "T" and i == "M":
            print("Kzandınız")    
            
            
        
        
         if seçim == "K" and i == "M":
            print("Karşı takım kazandı")
         if seçim == "M" and i == "T":
            print("Karşı takım kazandı")
         if seçim == "T" and i == "K":
            print("Karşı takım kazandı")
            
        
         if seçim == "T" and i ==  "Kartenkele":
            print("Kazandın")
         if seçim == "Kartenkele" and i == "Spoch":
            print("Kazandın")
         if seçim == "Spoch" and i == "M":
            print("Kazandın")
         if seçim == "M" and i == "Kartenkele":
            print("Kazandın")
         if seçim == "Kartenkele" and i == "K":
            print("Kazandın")
         if seçim == "K" and i == "Spoch":
            print("Kazandın")
         if seçim == "Spoch" and i == "T":
            print("Kazandın")
        
        
 karşı_bilgisayar_liste()
 seçim_değer = seçim_yapma()
 seçim_kontrol(seçim_değer)        
    

        