
class BankAccount:

    def __init__(self, account_name, starting_balance ):
        self.account_name = account_name
        self.starting_balance = starting_balance
    
    def desposit(self, amount):
        self.starting_balance += amount
        return f"Deposited ${amount}. New balance. ${self.starting_balance}"
    
    def witdraw(self, amount):
        if amount <= self.starting_balance:
            self.starting_balance -= amount
            return f"withdrew ${amount}. New Balance: ${self.starting_balance}"
        else:
            return "Insufficient funds."
        
    def get_balance(self):
        return f"{self.account_name} has a balance of  ${self.starting_balance}."