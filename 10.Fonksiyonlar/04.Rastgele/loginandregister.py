users = {}

def login(usurname,password):
    if usurname not in users.keys():
        print("Kullanıcı adı hatalı")
        return False
    
    correct_password = users[usurname]
        
    if password != correct_password:
        print("Şifreniz hatalı")
        return False
    
    return True


def register(usurname,password):
   if usurname in users.keys():
       print("Böyle bir kullanıcı var")
       return False
   
   users[usurname] = password
   return True
    