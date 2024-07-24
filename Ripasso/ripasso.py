#1

class Account:
    def __init__(self, account_id: str):
        self.account_id: str = account_id
        self.balance: float = 0.0

    def deposit(self, amount: float):
        self.balance += amount

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts: dict[str, Account] = {}

    def create_account(self, account_id: str):
        if account_id in self.accounts:
            raise ValueError("Account with this ID already exists")
        account = Account(account_id)
        self.accounts[account_id] = account
        return account

    def deposit(self, account_id: str, amount: float):
        if account_id not in self.accounts:
            raise ValueError("Account not found")
        self.accounts[account_id].deposit(amount)

    def get_balance(self, account_id: str):
        if account_id not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_id].get_balance()
   
    
# 2

def frequency_dict(elements: list) -> dict:
    dizionario = {}
    for item in elements:
        if item in dizionario:
            dizionario[item] += 1
        else:
            dizionario[item] = 1
    return dizionario


# 3

def transform(x: int) -> int:
    if x %2 == 0:
        x /= 2
        return x
    
    if x %2 != 0:
        x *= 3
        x -= 1
        return x
    
    
# 4



# 5

def print_seq(): 
    
    print("Sequenza a):")
    n = 0
    while (n<7):
        n += 1
        print (n)
    print()

    print("Sequenza b):")
    n = 3
    while (n<=23):
        print (n)
        n += 5
    print()

    print("Sequenza c):")
    n = 20
    x = 5
    while (x >= 0):
        x -= 1
        print (n)
        n -= 6
    print()

    print("Sequenza d):")
    n = 19
    while (n<=51):
        print (n)
        n += 8
    print()
    
    return


# 6



# 7

def print_seq(): 
    
    print("Sequenza a):")
    n = 0
    while (n<7):
        n += 1
        print (n)
    print()

    print("Sequenza b):")
    n = 3
    while (n<=23):
        print (n)
        n += 5
    print()

    print("Sequenza c):")
    n = 20
    x = 5
    while (x >= 0):
        x -= 1
        print (n)
        n -= 6
    print()

    print("Sequenza d):")
    n = 19
    while (n<=51):
        print (n)
        n += 8
    print()
    
    return


# 8