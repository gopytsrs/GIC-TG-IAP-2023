from logger import Logger
from statements import StatementBook


class InsufficientBalanceException(Exception):
    def __init__(self, amount, balance):
        self.message = f"Insufficient balance of ${balance:.2f} to withdraw ${amount:.2f}"
        super().__init__(self.message)


class InvalidAmountException(Exception):
    def __init__(self):
        self.message = "Please enter an amount greater than $0.00!"
        super().__init__(self.message)


class BankAccount:
    def __init__(self) -> None:
        self.balance = 0
        self.statements = StatementBook()

    def check_amount(self, amount: float) -> None:
        """Checks whether the amount is valid amount to deposit/withdraw, otherwise, raise an Exception

        Args:
            amount (float): The amount to deposit/withdraw

        Raises:
            InvalidAmountException: When the amount is lesser than or equal to zero
        """
        if amount <= 0:
            raise InvalidAmountException()

    def withdraw(self, amount: float) -> None:
        """Withdraws amount from the bank account

        Args:
            amount (float): Amount to withdraw

        Raises:
            InsufficientBalanceException: When the account has lesser balance than required withdrawal amount
        """
        self.check_amount(amount)
        if amount > self.balance:
            raise InsufficientBalanceException(
                amount, self.balance
            )
        self.balance -= amount
        Logger.print_withdraw_success(amount)
        self.statements.add_withdraw_statement(amount, self.balance)

    def deposit(self, amount: float) -> None:
        """Deposits amount from the bank account

        Args:
            amount (float): Amount to deposit
        """
        self.check_amount(amount)
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
