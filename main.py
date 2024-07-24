from user import User
print('welcome to alibaba')

users_list=[]
inp = ''
flag = 0
while True:
    inp = input('what do you want to do?  sign in | sign up: ')
    if inp == 'sign in':
        user_name = input('give me your username :')
        password = input('give me your password : ')
        for user in users_list:
            if user.username == user_name and user.password == password :
                print('successfull login')
                flag = 1
                break
        if flag == 1:
            break
        else :
            print('incorrect')

        
    elif inp == 'sign up':
        user_name = input('give me your username :')
        password = input('give me your password : ')
        this_user = User(user_name, password)
        users_list.append(this_user)
    else:
        print('wrong approach')


