from bank_account import BankAccount, InsufficientBalanceException
from logger import Logger


class CommandHandler:
    def __init__(self, account: BankAccount) -> None:
        self.account = account

    def first_prompt(self) -> None:
        """Initial prompt when user first starts the application
        """
        Logger.print_welcome()
        Logger.print_options()
        self.accept_command()

    def run(self) -> None:
        """Continuously prompts user for command and accepts them
        """
        self.first_prompt()
        while True:
            Logger.print_prompt()
            Logger.print_options()
            self.accept_command()

    def accept_command(self) -> None:
        """Parses the command and performs the corresponding action
        """
        string = input().lower()
        if string == "w":
            self.withdraw_command()
        elif string == "d":
            self.deposit_command()
        elif string == "p":
            self.print_command()
        elif string == "q":
            Logger.print_exit()
            exit()
        else:
            Logger.print_invalid_command_message()

    def withdraw_command(self) -> None:
        """Performs a withdrawal command on the bank account
        """
        if self.account.is_empty():
            Logger.print_zero_balance_message()
            return
        while True:
            try:
                Logger.print_withdraw_amount_prompt()
                amount = float(input())
                self.account.withdraw(amount)
                break
            except InsufficientBalanceException as e:
                print(e)
            except:
                Logger.print_invalid_amount_messsage()

    def deposit_command(self) -> None:
        """Performs a deposit command on the bank account
        """
        while True:
            try:
                Logger.print_deposit_amount_prompt()
                amount = float(input())
                self.account.deposit(amount)
                break
            except:
                Logger.print_invalid_amount_message()

    def print_command(self) -> None:
        """Performs the print statements command on the bank account
        """
        self.account.get_statement()
