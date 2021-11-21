def print_options():
  print(f'''
1 - list accounts
2 - transfer money
3 - open a new account
4 - logout
    ''')

def list_accounts(user):
  print('Your accounts: ')
  for i in range(3,len(user)):
    print(f'{i-2}.{user[i][0]} - Balance: {user[i][1]} RUB')

def transfer_money(user):
  if count_accounts(user) == 1:
    print('You need to have at least two accounts for this operation!')
  else:
    list_accounts(user)
    src_acc = request_input('Select the source account: ')
    target_acc = request_input('Select the target account: ')
    money_amount = request_input('Enter the amount to trandfer: ')
    if user[3][1] > money_amount:
      newValue = user[3][1] - money_amount
      user[3:user] = money_amount + newValue
      print(f'''
      Operation succeeded!
      Your accounts: 
      {user}
      ''')
    else:
      print('Insufficent funds on source account!')
      transfer_money(user)
      
def request_input(msg):
  return int(input(msg))

def count_accounts(user):
      return len(user) - 3

def input_credentials():
  username_input = input('Enter username: ')
  password_input = input('Enter password: ')
  return username_input, password_input

def enter_option():
  option = input('Choose an option: ')
  return option

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
              account_num = int(dt.split(";")[3])
          else:
              info.append(dt.strip().split(";"))
              account_num -= 1
              if account_num == 0:
                  output.append(info)
      return output

def data_check(l, p, data):
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
  authenticated, userData= data_check(login,password,db)
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
  else:print('Incorrect username/password!')

auth()