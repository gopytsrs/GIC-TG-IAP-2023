from logger import Logger
from statements import StatementBook


class InsufficientBalanceException(Exception):
    pass


class BankAccount:
    def __init__(self) -> None:
        self.balance = 0
        self.statements = StatementBook()

    def withdraw(self, amount: float) -> None:
        """Withdraws amount from the bank account

        Args:
            amount (float): Amount to withdraw

        Raises:
            InsufficientBalanceException: When the account has lesser balance than required withdrawal amount
        """
        if amount > self.balance:
            raise InsufficientBalanceException(
                f"Insufficient balance of ${self.balance:.2f} to withdraw ${amount:.2f}"
            )
        self.balance -= amount
        Logger.print_withdraw_success(amount)
        self.statements.add_withdraw_statement(amount, self.balance)

    def deposit(self, amount: float) -> None:
        """Deposits amount from the bank account

        Args:
            amount (float): Amount to deposit
        """
        self.balance += amount
        Logger.print_withdraw_success(amount)
        self.statements.add_deposit_statement(amount, self.balance)

    def get_statement(self) -> None:
        """Gets the full bank statement list of this account
        """
        self.statements.print_statements()

    def is_empty(self) -> bool:
        """Checks whether the account is empty

        Returns:
            bool: Whether the account is empty
        """
        return self.balance == 0
