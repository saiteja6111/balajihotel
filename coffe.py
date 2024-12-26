#we are going to build a coffe shop
def order():
    pass

def login():
    global username 
    global password
    print('*** ENTER LOGIN DETAILS ***')
    username = input('    USER NAME : ')
    password = input('    PASSWORD  : ')
    checklogin()

def checklogin():
    global username
    global password
    if username.upper() == 'RAMSAITEJA' and password == '123456789':
        print('logged in')
    else:
        print('Enter the correct credentials')
    pass
    

def signup():
    pass

print("*** WELCOME TO BALAJI FAST FOODS ***")

print("        1.LOGIN or 2.SIGNUP       ")
while True:
    l = input('Enter Your Option : ')
    if l == '1' or l.upper() == 'LOGIN':
        login()
        break
    elif l == '2' or l.upper() == 'SIGNUP':
        signup()
        break
    else:
        print('Choose option correctly!!!')
        continue




