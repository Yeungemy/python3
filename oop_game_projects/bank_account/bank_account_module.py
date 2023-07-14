class BankAccount:
    def __init__(self, owner, balance = 0) -> None:
        self.owner = owner
        self.balance = balance

    # print the class object
    def _str_(self):
        return f"account owner: {self.owner}\nAccount balance: {self.balance}"
    
    # delet the class object
    def _delete_(self):
        print("The account has been deleted!")

    # deposit money to the account
    def deposit(self, amount):
        self.balance += amount

        print("You have deposit ${} into your account and current balance is ${}".format(amount, self.balance))
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Funds Unavailable")
        else:
            self.balance -= amount
            print("You have withdrawn ${} from your account and current balance is ${}".format(amount, self.balance))
    
