print("Регистрация на сайте army.pro" ) 
print("Введите логин : ") 
login = input () 
print("Введите пароль: ") 
password = input () 

print("Введите пароль повторно: ") 
password_reheat = input () 
if password == password_reheat:
    print('Процесс регистрации на сайте army.pro прошёл успешно :)') 
    print('Авторизация на сайту army.pro ') 
    print('Введите логин при регистрации: ') 
    login_1 = input() 
    if login == login_1:
       print('Такой логин существует :)') 
       print('Введите пароль при регистрации на этот логин: ') 
       password_1 = input ()
       if password == password_1 :
           print("Вы успешно вошли в систему")
       else:
            print("Не правильно введен пароль")
    else: 
        print('Такой логин не существует ')
else:
    print("Повторный пароль веден не верно")
