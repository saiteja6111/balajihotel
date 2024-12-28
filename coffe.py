#we are going to build a coffe shop
def orderlist():
    print("\n                ORDER LIST                   ")
    print("\n1. Idly      - 5$         2. Idlysambar    - 6$")
    print("\n3. Gare      - 7$         4. Dosa          - 6$")
    print("\n5. Bajji     - 8$         6. Puri          - 10$")
    print("\n7. Onion Dosa- 10$        8. Masala Dosa   - 12$")
    print("\n***            Choose your Order             ***")
    total = 0
    additem = input('Add items (y/n) : ')
    while additem.upper() == 'Y':
        a = int(input("Enter your choice : "))
        if a == 1:
            acost = 5
            print(f'Idly  - {acost}$')
            total += acost
            print(f'Total - {total}$')
            additem = input('add another (y/n) : ')
        elif a == 2:
            bcost = 6
            print(f'Idlysambar - {bcost}$')
            total += bcost
            print(f'Total      - {total}$')
            additem = input('add another (y/n) : ')
        elif additem.upper == 'N':
            break
        elif additem.upper() != 'Y' and additem.upper() != 'N' :
            print("Choose correctly")
            additem = 'y'
    print(f"Yout total is {total}$")


def orderdenaid():
    print('\n     Thank You...     ')
    exit()
def order():
    decision = input('Do you wanna order?(y/n) : ')
    if decision.upper() == 'Y':
        orderlist()
    elif decision.upper() == 'N':
        orderdenaid()

def welcome():
    print(f"Hello SaiTeja🙋🏻... ")
    print("\n***   WELCOME TO SRI BALAJI FAST FOODS   *** ")
    print("\n                ORDER LIST                   ")
    print("\n1. Idly      - 5$         2. Idlysambar    - 6$")
    print("\n3. Gare      - 7$         4. Dosa          - 6$")
    print("\n5. Bajji     - 8$         6. Puri          - 10$")
    print("\n7. Onion Dosa- 10$        8. Masala Dosa   - 12$")
    order()
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
        print(f'logged in...')
        welcome()

    else:
        print('Enter the correct credentials')
    login()

def signup():
    print('Server under working process....')
    login()

print("*** WELCOME TO BALAJI FAST FOODS ***")


while True:
    print("        1.LOGIN or 2.SIGNUP       ")
    l = input('Enter Your Option : ')
    if l == '1' or l.upper() == 'LOGIN':
        login()
        break
    elif l == '2' or l.upper() == 'SIGNUP':
        signup()
        continue
    else:
        print('Choose option correctly!!!')
        continue




