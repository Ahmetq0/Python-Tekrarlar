todo_liste = []
     

ad_select = "1"
munite_select = "2"
resul_select = "3"
     
     
while True:
 def operation_selected():
      operation = input("1/Listeye Görev Ekler\n"
                       "2/Listeden Görev Siler\n"
                       "3/Listeyi Gösterir\n"
                       "Hangisini seçmek istersiniz\n")
      return operation

 
 def ad_selected(operation):
  if operation == ad_select:
          add_task = input("Eklemek istediğiniz görevi giriniz\n")
          todo_liste.append(add_task)
          print("Görev Listeye Eklendi")
          
          
 def munite_selected(operation):     
  if operation == munite_select:
          clear_task = int(input("Kaç numaralı görevi silmek istersiniz\n"))
          todo_liste.pop(clear_task)
          
 def resul_selected(operation):     
  if operation == resul_select:
          print("Görevleriniz:",todo_liste)
          
 def dekor():
       print("--"*20)
       return print
          
          
          
          
 operation_selected_değer = operation_selected()
 ad_selected_değer = ad_selected(operation_selected_değer)
 munite_selected_değer = munite_selected(operation_selected_değer)
 resul_selected_değer = resul_selected(operation_selected_değer)
          