from bank_account import BankAccount
from command_handler import CommandHandler

if __name__ == "__main__":
    bank_account = BankAccount()
    command_handler = CommandHandler(bank_account)
    command_handler.run()
