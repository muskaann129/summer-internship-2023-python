import requests
a = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

users = {1: {"username": 'muskaann.29',
           "password": 'Sotu@123',
           "USD": 273849,
           "BTC": 0},
           2: {"username": 'tgyanani_xD',
           "password": 'Tarun123',
           "USD": 13324,
           "BTC": 0},
           3: {"username": 'iamkunal9',
           "password": 'hekar@9',
           "USD": 822533,
           "BTC": 0}}

user = None
login = False
while login!=True:   
    Username = input("Enter Username: ")
    Password = input("Enter Password: ")
    for i in range(1,4):
        if Username == users[i]["username"] and Password == users[i]["password"]:
            user = i
            login = True
            break        
    if login == False:
        print("Wrong username or Password! Please try again")

usdLeft = users[user]["USD"]
btcLeft = users[user]["BTC"]
if user!=None:
    print("Login succesfull!!")
    print(f'User details:\nUsername = {users[user]["username"]}\nBalance USD = {usdLeft}\nBalance BTC = {btcLeft}')

check = None
while check!=4 and login == True:
    print("\nWhat would you like to do?")
    print("1. Buy Bitcoin")
    print("2. Sell Bitcoin")
    print("3. Check balance")
    print("4. exit")
    try:
        check = int(input("Enter our choise (1,2,3): "))

        if check==1:
            btcRate = float((a["bpi"]["USD"]["rate"]).replace(",",""))
            print(f"Rate of 1 Bitcoin is ${btcRate}")
            amount = int(input("Enter your amount(in USD) to buy bitcoin: "))
            if amount>usdLeft:
                print("Insufficient balance! please try again")
                continue
            btcBuyed = amount/btcRate
            usdLeft = usdLeft - amount
            btcLeft = btcLeft + btcBuyed
            print(f'You have buyed {btcBuyed} bitcoin for ${amount}')

        elif check==2:
            sellBtcAmount = int(input("Enter the amount(in USD) of which you want to sell Bitcoin: "))
            if sellBtcAmount>usdLeft:
                print("Insufficient balance! please try again")
                continue
            btcLeft = btcLeft - (sellBtcAmount/btcRate)
            usdLeft = usdLeft+sellBtcAmount
            print(f'You have sold {sellBtcAmount/btcRate} Bitcoins for ${sellBtcAmount}')
        
        elif check==3:
            print(f'Your current balance is:\nBalance USD = {usdLeft}\nBalance BTC = {btcLeft}')

        elif check>4:
            print("Invalid Input! Please try again")
            continue
    except:
        print("Invalid Input! Please try again")
print("Thank you!!")