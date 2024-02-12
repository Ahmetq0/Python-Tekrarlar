def sabah_namazı(student_basket,selected_false):
 dont_student = input("Gelmeyen Talebeleri yazınız\n") 
 student_basket.append(dont_student)
 print(selected_false,"Namazına","Gelmeyen öğrenciler:",student_basket)
 return (student_basket,selected_false)