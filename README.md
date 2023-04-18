# GIC TG IAP Test

---

## About this project:

This project is done as the take-home assignment for the GIC Technology Group Industrial Attachment Program (TG IAP).

Deadline: `21 Apr 2023 6pm`

The programming language of choice is `Python 3`

## Getting started:

1. The project can be started using main.py

```
$ python main.py
```

2. The user is able to select options and perform actions as they desire. Enter any of the letters to select an option.

```
Welcome to AwesomeGIC Bank! What would you like to do?
[D]eposit
[W]ithdraw
[P]rint statement
[Q]uit
```

## Testing:

Some unit tests have been written for some of the key functionalities of the application.

Before you run the unit tests, make sure you have `pytest` installed, if not run:

```
$ pip install pytest
```

Run the unit tests using this command while in the root folder:

```
$ pytest -v
```

## Application and architectural design:

The programming paradigm of choice in this application is Object-Oriented Programming.

This choice was made due to intuition of modelling the relevant classes to their related functionality, which also allowed for separation of concerns.

The application contains of five main code files and their corresponding classes defined within.

-   `bank_account.py`
    -   `BankAccount`
        -   Represents a bank account of the user.
        -   Performs actions to update the balance and view statements
-   `command_handler.py`
    -   `CommandHandler`
        -   Handles the input entered by the user and invokes the corresponding commands on `BankAccount` provided.
-   `logger.py`
    -   `Logger`
        -   Handles logging of output to the console interface
-   `statements.py`
    -   `Statement`
        -   Represents a statement in the statement book, can be deposit or withdraw, or possibly others
    -   `StatementBook`
        -   Represents the list of statements inside a statement book of a user
        -   Performs actions append statements, and print the current statement list.
-   `main.py`
    -   Main entrypoint of the application

##### Error handling:

-   To ensure robustness of the application, exception handling is added into the code in several places
    -   `CommandHandler`
        -   Exceptions are handled for cases where users enter invalid input when entering deposit/withdraw amount
    -   `BankAccount`
        -   A custom exception `InsufficientBalanceException` is created, and it is raised when withdraw amount is more than balance

##### Possible extensions and improvements:

-   Adding a database for persistent storage, which would allow for:
    -   User accounts creation and selection with username and password
    -   Storing the state and balance of accounts between sessions
-   Adding more unit and integration tests, require mocking for some.
-   Refactoring of code to make it more decoupled (Would use functional style instead)

## Authors:

-   [Goh Chen Kang, Sean](mailto:seangohck@gmail.com)
