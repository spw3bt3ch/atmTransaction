# A skeletal view of how ATM user experience code runs
# Bank serces in a List
services = ['1. WITDRAWAL','2. CHECK ACCOUNT BALANCE','3. CARDLESS WITHDRAWAL','4. FUND TRANSFER','5. UTILITY BILLS']

userPIN = 2023
accountBalance = 20000000
print(' ')
print('WLECOME TO SMI BUSINESS PLACE ATM')
print(' ')

# A for loop to display the values of the list in a vertical arrangement - hence making the for loop a function.
def opening():
    for s in services:
        print(s)
print(' ')

opening() # calling the for...loop function

print(' ')
service = int(input('Choose a service: '))
print(' ')

# Functions for each services in the list
def withdrawal(): # Withdrawal function
    userP = 2023
    enterPIN = int(input('Enter your PIN: '))
    checkW = int(input('Enter Amount in 1000 denomination: '))
    global bal 
    bal = accountBalance - checkW
    if enterPIN == userP:
        if checkW <= 900 or checkW >= 150000:
            print(' ')
            print('Amount is out available range dispensable.')
            print(' ')
        else:
            sure = input('Are you sure of the amount you just entered? ')
            if sure == 'Yes':
                print(' ')
                print('Wait while we process your cash...')
                print(' ')
                print('Take your cash.')
                print(' ')
                print(f'AVAILABLE BALANCE: =N={bal}.00')
                print(' ')
                print('Thank you for your time.')
                print(' ')
            elif sure == 'No':
                print('Thank you for using our ATM.')
    else:
        print('Invalid PIN. Try again later.')

def balance():  # Function to check account balance
    while (True):
        pin = int(input('Enter PIN: ')) 
        if pin == userPIN:
            return bal
            #print(f'The Amount Available in your account is =N={bal}.00')
            break
        else:
            print(pin)
            continue

def cardless(): # Functio for cardless transaction - Cardless Withdrawal
    cardlP = int(input('Enter your OTP for withdrawal: '))
    if cardlP == 1234567890:
        confirmA = int(input('Please confirm the Amount: '))
        if confirmA >= 100000:
            print('Amount Cannot be dispensed.')
        else:
            print('Please while we process your cash.')
            print('Take your cash. Thank you')
    else:
        print('Please check OTP validation and try again later. Thank you!')

def transfer(): # Function to make a bank transfer
    amount = int(input('Enter Amount to Trasnfer: '))
    beneficiary = int(input('Enter Beneficiary Accoutn Number: '))
    confirmPIN = int(input('Please confirm your account PIN to proceed:'))
    if amount >= 250000 and confirmPIN == 2023:
        print('Beware that transfer of fund greater than =N=250,000 is not allowed over the network for security purposes.')
        proceed = input('Do you want to proceed with this transaction: ')
        if proceed == 'Yes':
            print('Processing Transfer...')
            print(' ')
            print('...')
            print(' ')
            print('Transfer Conpleted.')
        else:
            anyOther = input('Do you want to perform any other transaction? ')
            if anyOther == 'Yes':
                opening()
            else:
                print('Take your card')
                print('Thank you for your time.')
    else:
        print('Processing Transaction...')
        print('Transaction completed.')
        print(' Thank you.')

def bills(): # Function to pay bills via ATM
    bills = ['1. IKEDC', '2. AIRTIME', '3. INTERNET DATA', '4. CHURCH DONATIONS', '5. SCHOOL FEES', 
             '6. LIRS', '7. FIRS', '8. SUPPLIERS', '9 LAGOS WATER COOPORATION', '10. LAWMA']
    print('Use assigned numbers to choose BIll from the options below: ')
    for b in bills:
        print(b)
    print(' ')
    
    while (True):
        print(' ')
        enterBill = int(input('Choose a Bill to process: ')) # This is just to check for the available options.........
  
        if enterBill == 1:
            print('This is Ikeja Electric Distribution Company')
            print(' ')
            continue
        elif enterBill == 2:
            print('Airtime available is Glo NG.')
            print(' ')
            continue
        elif enterBill == 3:
            print('Internet data available on this network is 9mobile.')
            print(' ')
            continue
        elif enterBill == 4:
            print('Church donation available is toward the RCCG redemption city at Shimawa, Ogun state.')
            print(' ')
            continue
        elif enterBill == 5:
            print('Pay for your Redeemers University (RUN) school fees here and Now.')
            print(' ')
            continue
        elif enterBill == 6:
            print('This is Lagos State Inland Revenue Service')
            print(' ')
            continue
        elif enterBill == 7:
            print('This is Federal Inland Revenue Service')
            print(' ')
            continue
        elif enterBill == 8:
            print('SMI BUsiness Place is the only supplier of any goods in Lagos State and Nigeria at large.')
            print(' ')
            continue
        elif enterBill == 9:
            print('Pay for your water supplied by Lagos State water coporation.')
            print(' ')
            continue
        elif enterBill == 10:
            print('Pay Lagos State Waste Management Agency for your waste disposal.')
            print(' ')
            continue
        elif enterBill == 'done':
            break
        else:
            print('You have entered an Invalid data! Try again please.')
            print(' ')
            continue
    print(' ')
    
# Calling the functions based on the services in the list chosen.
if service == 1:
    withdrawal()

if service == 2:
    balance()

if service == 3:
    cardless()

if service == 4:
    transfer()

if service == 5:
    bills()