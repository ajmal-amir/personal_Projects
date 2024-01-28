from    BankAccount import BankAccount 

bank_account = BankAccount("Ajmal Amir", 500)


desposit = bank_account.desposit(300)

withdrew = bank_account.witdraw(200)
current_balanc = bank_account.get_balance()
print(current_balanc)
