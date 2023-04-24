import mysql.connector

connection = mysql.connector.connect(user = "root", database = "bank_info", password = "Hero Time!616")

cursor = connection.cursor()

 

testQuery = ('SELECT * FROM bank_info')

 

cursor.execute(testQuery)

 

for item in cursor:

    print(item)

 
def login(username):
    password = input("Enter your password.")                                  
    cursor.execute(f"SELECT password FROM bank_info where username = '{username}'") 
    actualpassword = cursor.fetchall()
    return password == actualpassword[0][0]

def makeanaccount(username):
    password = input('Plese create a password:')
    addacount = (f"INSERT INTO bank_info (password, total_money, username) VALUES ('{password}', '{'0'}', '{username}')")
    cursor.execute(addacount)
def viewcash(username):
    cursor.execute(f"SELECT total_money FROM bank_info where username = '{username}'")
    return int(cursor.fetchall()[0][0].replace(",",""))

name = input('Hello! Welcome to Oreo Bank. Please put your name: ')
print(f'Hi {name}, nice to meet you!')
welcome = input('Would you like to Log In or Make an Account?')
signin = False
if welcome == 'Log In':
    print('Please log in.')
    username = input('Enter your username.')
    signin = login(username)
    if signin == False:
        print('Please enter your password again')
        signin = login(username)
    if signin == True:
        money_amount = viewcash(username)
elif welcome == 'Make an Account':
    print('Please create a username and password.')
    username = input('Enter your username.')
    makeanaccount(username)
    money_amount = viewcash(username)
    signin = True
elif welcome == 'No':
    print('Okay, Have a nice day')

questions = ''
Res = ''
if signin == True:
    questions = input('Would you like to Make a Deposit, Withdraw From Your Account, or View the Mone in Your Account. Please answer the question with an uppercase Yes or No.')

if questions == 'No':
    print(f'Ok have a nice rest of your day {name}! Come back soon!')


if questions =='Yes':
    print('provided responses: Withdraw, Deposit, View Amount.')
    Res = input('What would you like to do: ')
if Res == 'View Amount':
    print(money_amount)
elif Res == 'Withdraw':
    withdraw = input('How much money would you like to withdraw?')
    money_amount -= int(float(withdraw))
    cursor.execute(f"UPDATE bank_info SET total_money = '{str(money_amount)}' where username = '{username}'") 
    print(money_amount)
elif Res == 'Deposit':
    deposit = input('How much money would you like to deposit?')
    money_amount += int(float(deposit)) 
    print(f"UPDATE bank_info SET total_money = '{str(money_amount)}' where username = '{username}'")
    cursor.execute(f"UPDATE bank_info SET total_money = '{str(money_amount)}' where username = '{username}'")
    print(money_amount)

connection.commit()
cursor.close()

connection.close()