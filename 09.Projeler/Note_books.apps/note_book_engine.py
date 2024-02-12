note_book = []


def not_ekleme():
    note = input("Yazmak istediğiniz notu giriniz\n")
    note_book.append(note)
    print("Notunuz not defterine eklendi")
    
    
def notları_görme():
    print("Notlarınız:",note_book)
    
    
def not_silme():
    clear_note = int(input("Silmek istediğiniz notun numarasını giriniz\n"))
    note_book.pop(clear_note)
    print(clear_note,"numaralı not silindi")
    
    