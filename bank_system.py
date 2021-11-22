def print_options():
    print('''
1 - list accounts
2 - transfer money
3 - open a new account
4 - logout
    ''')

def list_accounts(user):
    print('Your accounts:')
    for i in range(3, len(user)):
        print(f'{i - 2}. {user[i][0]} - Balance: {user[i][1]} RUB')
    
def count_accounts(user):
    return len(user) - 3

def transfer_money(user):
    acc_number = count_accounts(user)
    if acc_number == 1: 
        print('You need to have at least two accounts for this operation')
    else: 
        list_accounts(user)
        src_acc, target_acc = request_accounts()
        src_acc, target_acc = check_accounts(src_acc, target_acc, acc_number)
        money_amount = request_input('Enter the amount to transfer: ')

def request_accounts():
        return request_input('Select the source account: '), request_input('Select the target account: ')

def check_accounts(src, tgt, number):
    while src <= 0 or src > number or tgt <= 0 or tgt > number:
        print('You are referencing non-existing account(s)')
        src, tgt = request_accounts()
    
    while tgt == src: 
        print('You are trying to transfer money between same accounts')
        src, tgt = request_accounts()
    return src, tgt

def check_amount():
    pass

def request_input(msg):
    return int(input(msg))

def enter_option():
    option = input('Choose an option: ')
    return option

def input_credentials():
    username_input = input('Enter username: ').strip()
    while True:
        if username_input == '':
            print('You have entered empty string or spaces. Please enter username again')
            username_input = input('Enter username: ').strip()
        else: break
    password_input = input('Enter password: ').strip()
    while True:
        if password_input == '':
            print('You have entered empty string or spaces. Please enter password again')
            password_input = input('Enter password: ').strip()
        else: break
    return username_input, password_input

def read_data():
  with open ('./bankdata.txt','r') as user:
      constData = user.readlines()
      output = list()
      info = list()
      account_num = int()
      for dt in constData:
          if account_num == 0:
              info = []
              info += dt.split(";")[0:3]
              account_num = int(dt.strip().split(";")[3])
          else:
              info.append(dt.strip().split(";"))
              account_num -= 1
              if account_num == 0:
                  output.append(info)
      return output

def check_data(l, p, data):
    for datum in data:
        if l == datum[1] and p == datum[2]: 
            return [True, datum]
    return [False, None]

def logout():
    print('Welcome to the online bank!')
    auth()

def auth():
    login, password = input_credentials()
    db = read_data()
    authenticated, userData  = check_data(login, password, db)
    if authenticated: 
        print(f'Welcome, {userData[0]}!')
        print_options()
        option = enter_option()
        if option == '1':
            list_accounts(userData)
        elif option == '2':
            transfer_money(userData)
        elif option == '4':
            logout()
    else: print('Incorrect username/password!')

auth()




