# python banking_app.py
from datetime import date
# ok
def int_input(num):
    while True:
        try:
            int_number = int(input(num))
            if int_number > 0:
                return int_number
                # break
            else:
                print("Enter your positive number.")               
        except ValueError:
            print("Enter your integer value.")

# ok.
def withdraw_money(user_ID):
    with open("user_balance.txt", "r") as balance_file:
        a = balance_file.readlines()
    today_date = date.today()
    reason = input("enter the reason: ")
    user_balance = {}
    for i in a:
        get_user_ID = i.strip().split(",")[0]
        get_balance = int(i.strip().split(",")[1])
        
        user_balance[get_user_ID] = get_balance
        if user_ID == get_user_ID:
            balance = get_balance
    while True:
        withdrow_amount = int_input("Enter your withdrowal amount: ")
        if withdrow_amount <= balance:
            balance -= withdrow_amount
            print("new balance after the withdraw: ", balance)
            break
        else:
            print("Enter the correct value.")

    with open("transaction_history.txt", "a") as final:
        final.write(f"{user_ID}, {today_date}, withdraw, {reason}, {balance}\n")
    user_balance[user_ID] = balance

    j = 0
    for key, values in user_balance.items():
        if j == 0:
            j = 1
            with open("user_balance.txt", "w") as update:
                update.write(f"{key}, {values}\n")
        else:
            with open("user_balance.txt", "a") as update:
                update.write(f"{key}, {values}\n")
'''
    with open("user_balance.txt", "w") as update:
        for key, value in user_balance.items():
            update.write(f"{key}, {value}\n")
'''

# ok.
def deposit_money(user_ID):
    with open("user_balance.txt", "r") as get_balance:
        a = get_balance.readlines()
        today_date = date.today()
        reason = input("enter the reason: ")
        c = {}

        for i in a:
            b = i.strip().split(",")[0]
            d = i.strip().split(",")[1]
            
            c[b] = d
            if user_ID == b:
                balance = int(i.strip().split(",")[1])

    deposit_amount = int_input("Enter your deposit aount: ")
    balance += deposit_amount
    print("new balance after deposit: ", balance)
    with open("transaction_history.txt", "a") as final:
        final.write(f"{user_ID}, {today_date}, deposit, {reason}, {balance}\n")

    c[user_ID] = balance

    j = 0
    for key, values in c.items():
        if j == 0:
            j = 1
            with open("user_balance.txt", "w") as update:
                update.write(f"{key}, {values}\n")
        else:
            with open("user_balance.txt", "a") as update:
                update.write(f"{key}, {values}\n")
    

    '''
    with open("user_balance.txt", "w") as update:
        for key, value in balances.items():
            update.write(f"{key}, {value}\n")
    '''

# ok.
def register_user():
    name = input("name: ")
    address = input("address: ")
    phone_number = input("phone number: ")
    user_name = input("create user name: ")
    password = input("create password: ")
    amount = int_input("Enter ypur starting amount: ")
    today_date = date.today()
    try:
        with open("registration.txt", "r") as create_user_ID:
            user_ID_list = create_user_ID.readlines()
    except FileNotFoundError:
        user_ID_list = []
    if len(user_ID_list) == 0:
        user_ID = f"U1001"
    else:
        last_line = user_ID_list[-1].strip()
        z = int(last_line.split(",")[0].strip()[1:]) + 1
        user_ID = f"U{z}"

    with open("registration.txt", "a") as registration:
        registration.write(f"{user_ID}, name: {name}, address: {address}, phone number: {phone_number}\n")

    with open('user.txt', 'a') as user_login:
        user_login.write(f"{user_ID}, user name: {user_name}, password: {password}\n")

    with open("user_balance.txt", "a") as balance:
        balance.write(f"{user_ID}, {amount}\n")

    with open("transaction_history.txt", "a") as transaction:
        transaction.write(f"{user_ID}, {today_date}, initial deposit, account creation,{amount}\n")

def register_admin():
    name = input("name: ")
    address = input("address: ")
    phone_number = input("phone number: ")
    admin_name = input("create admin name: ")
    password = input("create admin password: ")
    try:
        with open("admin_registration.txt", "r") as create_admin_ID:
            admin_ID_list = create_admin_ID.readlines()

    except FileNotFoundError:
        admin_ID_list = []

    if len(admin_ID_list) == 0:
        admin_ID = f"A1001"
    else:
        last_line = admin_ID_list[-1].strip()
        z = int(last_line.split(",")[0].strip()[1:]) + 1
        admin_ID = f"A{z}"

    with open("admin_registration.txt", "a") as registration:
        registration.write(f"{admin_ID}, name: {name}, address: {address}, phone number: {phone_number}\n")

    with open('admin.txt', 'a') as user_login:
        user_login.write(f"{admin_ID}, user name: {admin_name}, password: {password}\n")

def check_balance(user_ID, name):
    with open("user_balance.txt", "r") as check_balance:
        check = check_balance.readlines()
        for i in check:
            a = i.strip().split(",")[0].strip()
            balance = i.strip().split(",")[1].strip()
            if a == user_ID:
                print(f"Hi {name}. your balance is: {balance}")

# ok
def user_login(user_ID, name, user_name, user_password):
    user_info =[user_ID, name, user_name, user_password]
    while True:
        print("1.Deposit.")
        print("2.Withdrow.")
        print("3.Check balance")
        print("4.Transaction History.")
        print("5.Exit")
        value = int_input("Enter your choice: ")
        if value == 1:
            deposit_money(user_info[0])
        elif value == 2:
            withdraw_money(user_info[0])
        elif value == 3:
            check_balance(user_info[0], user_info[1])
        elif value == 4:
            transaction_history(user_info[0])
        elif value == 5:
            break
        else:
            print("value select correct number")

    
           

def user_login_check():
    with open("user.txt","r") as get_user , open("registration.txt", "r") as get_name:
        a = get_user.readlines()
        name = get_name.readlines()

    while True:
        user_name = input("Enter the user name")
        password = input("Enter the password")
        for i in a:
            get_user_name = i.split(",")[1].strip().split(":")[1].strip() # user name
            get_password = i.split(",")[2].strip().split(":")[1].strip() #user password
            get_user_ID = i.split(",")[0].strip() # user ID

            if get_user_name == user_name and get_password == password:
                print("user login successful.")
                for j in name:
                    last_ID = j.strip().split(",")[0].strip() 
                    if get_user_ID == last_ID:
                        original_name = j.strip().split(",")[1].strip() # original name
                        user_login(get_user_ID, original_name, user_name, password)
                        return
        else:
            print("Invalid user name or password")

# ok
def change_user_name_password(user_ID):
    with open('user.txt', 'r') as change:
        x = change.readlines()
    user_data = {}
    b = 0
    for i in x:
        z = i.strip().split(",")[0].strip()
        user_data[z] =  [i.strip().split(",")[1].strip()[6:],  i.strip().split(",")[2].strip()[10:]]
        if user_ID == z:
            new_username = input("Enter the new user name: ")
            new_password = input("Enter the new password: ")
            user_data[user_ID] =[new_username,new_password]
        
    for key,values in user_data.items():
        if b == 0:
            with open('user.txt', 'w') as update:
                update.write(f"{key}, user name: {values[0]}, password: {values[1]}\n")
                b = 1
        else:
            with open('user.txt', 'a') as update:
                update.write(f"{key}, user name: {values[0]}, password: {values[1]}\n")
    print("Username and password successfully updatede...\n")

# ok
def change_admin_name_password(admin_ID):
    with open('admin.txt', 'r') as change:
        x = change.readlines()
    a = {}
    b = 0
    for i in x:
        z = i.strip().split(",")[0].strip()
        a[z] =  [i.strip().split(",")[1].strip()[6:],  i.strip().split(",")[2].strip()[10:]]
        if admin_ID == z:
            new_admin_name = input("Enter the new admin name: ")
            new_password = input("Enter the new password: ")
            a[admin_ID] =[new_admin_name,new_password]
        
    for key,values in a.items():
        if b == 0:
            with open('admin.txt', 'w') as update:
                update.write(f"{key}, user name: {values[0]}, password: {values[1]}\n")
            b = 1
        else:
            with open('admin.txt', 'a') as update:
                update.write(f"{key}, user name: {values[0]}, password: {values[1]}\n")
    print("finished admin update...")







def transaction_history(user_ID):
    with open("transaction_history.txt", "r") as transaction_file:
        records = transaction_file.readlines()
        transaction = []
        for i in records:
            get_user_ID = i.strip().split(",")[0].strip()
            if user_ID == get_user_ID:
                transaction.append(i.split(','))
    while True:
        print(user_ID)
        print('1.all transaction.')
        print('2.spesific date transaction.')
        print('3.Exit.')
        choice = int_input("Enter your choice: ")
        if choice < 3:
            if choice == 1:
                print(f"{'user_ID'.ljust(8, '-')} {'Date'.center(12, '-')} {'type'.center(20, '-')} {'reason'.center(20, '-')} {'balance'.rjust(12, '-')}")
                print("-"*80)
                for j in transaction:
                    print(f"{j[0].ljust(8, "-")} {j[1].ljust(12,"-")} {j[2].ljust(20,"-")} {j[3].ljust(20,"-")} {j[4].rjust(12,"0")}")
                print('finished'.center(80,'-'))
            # pending 
            elif choice == 2:
                date_input = input("Enter the spesific date: ")
                check = False
                print(f"{'user_ID'.ljust(8, '-')} {'Date'.center(12, '-')} {'type'.center(20, '-')} {'reason'.center(20, '-')} {'balance'.rjust(12, '-')}")
                print("-"*80)
                for k in transaction:
                    if date_input == k[1]:
                        check = True
                        print(f"{k[0].ljust(8, "-")} {k[1].ljust(12,"-")} {k[2].ljust(20,"-")} {k[3].ljust(20,"-")} {k[4].rjust(12,"0")}")
                if check == False:
                    print("record not found.")
                print('finished'.center(80,'-'))
        elif choice == 3:
            break
        else:
            print("Enter the correct value.")

def admin_ID_check():
    while True:
        admin_ID = input("Enter the admin ID: ")
        with open('admin.txt', 'r') as admins_ID:
            admins_ID_list = admins_ID.readlines()
        for i in admins_ID_list:
            Admin_ID = i.split(',')[0].strip()
            if Admin_ID == admin_ID:
                return admin_ID
        print('admin ID not found.')
        print('1.continue')
        print('2.break')
        choice = int_input("Enter the correct number: ")
        if choice < 2:
            if choice == 1:
                continue
        elif choice == 2:
            break
        else:
            print("Enter the correct value.")



def user_ID_check():
    while True:
        user_ID = input("Enter the user ID: ")
        with open('user.txt', 'r') as users_ID:
            users_ID_list = users_ID.readlines()
        with open('registration.txt','r') as user_name:
            user_name_list = user_name.readlines()
        for i in users_ID_list:
            User_ID = i.split(',')[0].strip()
            if User_ID == user_ID:
                for j in user_name_list:
                    get_user_ID = j.split(',')[0].strip()
                    name = j.split(',')[1].split(':')[1].strip()
                    if get_user_ID == user_ID:
                        return [user_ID, name]
        print('user ID not found.')
        print('1.continue')
        print('2.break')
        choice = int_input("Enter the correct number: ")
        if choice < 2:
            if choice == 1:
                continue
        elif choice == 2:
            break
        else:
            print("Enter the correct value.")



# modify user data
def admin_view(admin_ID):
    print(admin_ID)
    while True:
        user_data = user_ID_check() # user ID ,name
        print("1.Change user name and password.")
        print("2.deposit.")
        print("3.Withdrow.")
        print("4.Check balance")
        print("5.Transaction History.")
        print("6.Delete user.")
        print("7.Exit.")
        print("\n")
        choice = int_input("Enter your choice: ")
        if choice == 1:
            change_user_name_password(user_data[0])
        elif choice == 2:
            deposit_money(user_data[0])
        elif choice == 3:
            withdraw_money(user_data[0])
        elif choice == 4:
            check_balance(user_data[0],user_data[1])
        elif choice == 5:
            transaction_history(user_data[0])
        elif choice == 6:
            # delete_user(user_ID)
            pass
        elif choice == 7:
            break
        else:
            print("Enter the correct number.")





def admin_login(admin_ID, name, admin_name, admin_password):
    admin_info = [admin_ID, name, admin_name, admin_password] 
    print("Admin login successful.")
    while True:
        print("1.Register and create user.")
        print("2.modify user.")
        print("3.Exit.")
        print("\n")
        admin_value = int_input("Enter your choice: ")
        if admin_value == 1:
            register_user()
        elif admin_value == 2:
            admin_view(admin_info[0])
        elif admin_value == 3:
            break
        else:
            print("enter the correct number.")

# ok admin login
def admin_login_check():
    with open("admin.txt","r") as admin_user , open("admin_registration.txt", "r") as get_name:
        admin_lines = admin_user.readlines()
        name_lines = get_name.readlines()
    while True:
        admin_name = input("Enter the admin name: ")
        password = input("Enter the password: ")
        for i in admin_lines:
            get_admin_name = i.split(",")[1].strip().split(":")[1].strip() # admin name
            get_password = i.split(",")[2].strip().split(":")[1].strip() # admin password
            get_admin_ID = i.split(",")[0].strip() # admin ID
            if get_admin_name == admin_name and get_password == password:
                print("user login successful.")
                for j in name_lines:
                    last_ID = j.strip().split(",")[0].strip()
                    if get_admin_ID == last_ID:
                        last_name = j.strip().split(",")[1].strip() #real admin name
                        admin_login(get_admin_ID, last_name, admin_name, password)
        else:
            print("Invalid admin name or password.")

# ok super_admin_login
def super_admin_login():
    while True:
        super_admin_ID = "S1001"
        Super_admin_name = "S1001"
        Password = "S1001"
        super_admin_name = input("Enter the user name:(S1001) :- ")
        password = input("Enter the password:(S1001) :- ")
        if Super_admin_name == super_admin_name and password == Password: #check login name and password   
            print("Super admin login successful.")
            print("1.register admin.")
            print("2.Change admin name and password.")
            print("3.Change user name and password.")
            print("4.modify user.")
            print("5.Exit.")
            choice = int_input("Enter your choice: ") 
            if choice == 1:
                register_admin()
            elif choice == 2:
                admin_ID = admin_ID_check()
                change_admin_name_password(admin_ID)
            elif choice == 3:
                user_ID = user_ID_check()
                change_user_name_password(user_ID)
            elif choice == 4:
                admin_view(super_admin_ID)
            elif choice == 5:
                break
            else:
                print("Enter the correct value.")
        else:
            print("Invalid user name or password")
# ok Main function
def Main():
    while True:
        print("\n")
        print("-----mini banking app-----")
        print("1.User login.")
        print("2.Admin login.")
        print("3.super admin login.")
        print("4.Exit.")
        choice = int_input("Enter your choice: ")
        # if choice < 4:
        if choice == 1:
            user_login_check()
        elif choice == 2:
            admin_login_check()
        elif choice == 3:
            super_admin_login()
        elif choice == 4:
            break
        else:
            print("select correct number.")

Main()
print("bye")
