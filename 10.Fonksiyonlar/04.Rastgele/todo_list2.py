
def operation_list():
     operation = input("Eğer görev eklemek isterseniz /e/\n"
                      "Eğer görev silmek isterseniz /s/\n"
                      "Eğer görevlerinizi görmek isterseniz /g/\n"
                      "Eğer uygulamadan çıkış yapmak isterseniz /q/ tıklayınız\n")
     return operation
 
def operation_ekleme(operation): 
     if operation == 1
     selected = input("Eklemek istediğiniz görevi girin\n")
     todo_liste.append(selected)
     return selected
    
    
def operation_görevler(operation):    
     if operation == "g":
        print("Görevleriniz:",todo_liste)
    
    
def operation_silmek(operation):     
     if operation == "s":
        selected2 = int(input("Silmek istediğiniz görevin numarasını giriniz\n"))
        todo_liste.pop(selected2)
        return selected2
    
def operation_quit(operation):   
     if operation == "q":
        print("Çıkış Yapıldı")
        
    