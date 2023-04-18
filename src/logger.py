class Logger:
    def print_welcome() -> None:
        """Welcome message shown on first start
        """
        print("Welcome to AwesomeGIC Bank! What would you like to do?")

    def print_exit() -> None:
        """Exit message when user quits the program
        """
        print("Thank you for banking with AwesomeGIC Bank.\nHave a nice day!")

    def print_prompt() -> None:
        """Prompt message after successful actions
        """
        print("Is there anything else you'd like to do?")

    def print_options() -> None:
        """Options for available actions
        """
        print("[D]eposit\n" +
              "[W]ithdraw\n" +
              "[P]rint statement\n" +
              "[Q]uit")

    def print_withdraw_success(amount: float) -> None:
        """Message printed when withdraw command is succesful

        Args:
            amount (float): Amount withdrawn
        """
        print(f"Thank you. ${amount:.2f} has been withdrawn to your account.")

    def print_deposit_success(amount: float) -> None:
        """Message printed when deposit command is succesful

        Args:
            amount (float): Amount deposited
        """
        print(f"Thank you. ${amount:.2f} has been deposited to your account.")

    def print_zero_balance_message() -> None:
        """Message printed when trying to withdraw on zero balance
        """
        print(
            "You have zero balance in your account, deposit some money in order to withdraw")

    def print_invalid_command_message() -> None:
        """Message printed when an invalid command is entered during command parsing
        """
        print("Please enter a valid command [W/w], [D/d], [P/p] or [Q/q]")

    def print_invalid_amount_message() -> None:
        """Message printed when an invalid amount is entered when parsing amount to float
        """
        print("Please enter a valid amount e.g. 100, 100.00, 100.0")

    def print_withdraw_amount_prompt() -> None:
        """Message printed to prompt user to enter withdrawal amount
        """
        print("Please enter the amount to withdraw:")

    def print_deposit_amount_prompt() -> None:
        """Message printed to prompt user to enter deposit amount
        """
        print("Please enter the amount to deposit:")
