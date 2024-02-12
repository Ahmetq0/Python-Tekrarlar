import note_book_engine

note_add = "1"
note_eye = "2"
note_clear = "3"
quitt = "q"

while True:
    operation = input("1/Not Ekleme\n"
                      "2/Not Görme\n"
                      "3/Not Silme\n"
                      "q/Çıkış\n"
                      "Yapacağınız işlemi seçiniz\n")
    
    
    if operation == note_add:
        note_book_engine.not_ekleme()
        
    elif operation == note_eye:
        note_book_engine.notları_görme()
        
    elif operation == note_clear:
        note_book_engine.not_silme()
    
    elif operation == quitt:
        print("Uygulamadan çıkış yapıldı")
        print("Notlarınız:",note_book_engine.note_book)
        break
    