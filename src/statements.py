import datetime


class Statement:
    """This class represents a statement that lives in the statement book/list
    """

    def __init__(self, amount: float, balance: float, action_datetime: str) -> None:
        self.message = f"{action_datetime:24} | {amount:18.2f} | {balance:18.2f}"

    def __repr__(self) -> str:
        return self.message


class StatementBook:
    """This class represents a statement book/list, you can add statements and view all statements
    """

    def __init__(self) -> None:
        self.statements = []

    def get_formatted_date(self) -> str:
        """Helper function to format date according to format in statement book.

        Returns:
            str: date formatted such as "8 Jul 2022 11:14:15AM"
        """
        now = datetime.datetime.now()
        formatted_date = now.strftime("%d %b %Y %I:%M:%S%p")
        return formatted_date

    def add_deposit_statement(self, amount: float, balance: float) -> None:
        """Adds a deposit statement to the statement book

        Args:
            amount (float): The amount deposited
            balance (float): The account balance after depositing the amount
        """
        self.statements.append(
            Statement(amount, balance, self.get_formatted_date()))

    def add_withdraw_statement(self, amount: float, balance: float) -> None:
        """Adds a withdraw statement to the statement book

        Args:
            amount (float): The amount withdrawn
            balance (float): The account balance after withdrawing the amount
        """
        self.statements.append(
            Statement(-amount, balance, self.get_formatted_date()))

    def print_statements(self) -> None:
        """Prints all the statements in the book in the order they were added
        """
        print(f"{'Date':24} | {'Amount':18} | {'Balance':18}")
        for statement in self.statements:
            print(statement)
