import pytest
from src.bank_account import *


def test_account_starts_empty():
    account = BankAccount()
    assert account.balance == 0


def test_withdraw_empty():
    account = BankAccount()
    with pytest.raises(InsufficientBalanceException):
        account.withdraw(10)


def test_deposit():
    account = BankAccount()
    account.deposit(10)
    assert account.balance == 10


def test_withdraw_after_deposit():
    account = BankAccount()
    account.deposit(10)
    account.withdraw(5)
    assert account.balance == 5
