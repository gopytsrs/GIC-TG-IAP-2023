from src.command_handler import CommandHandler
from src.bank_account import BankAccount


def test_withdraw_command_when_empty(capfd):
    account = BankAccount()
    command_handler = CommandHandler(account)
    command_handler.withdraw_command()
    out, _ = capfd.readouterr()
    assert out == "You have zero balance in your account, deposit some money in order to withdraw\n"


def test_invalid_command_entered(monkeypatch, capfd):
    account = BankAccount()
    command_handler = CommandHandler(account)

    monkeypatch.setattr("builtins.input", lambda: "?")

    command_handler.accept_command()
    out, _ = capfd.readouterr()
    assert out == "Please enter a valid command [W/w], [D/d], [P/p] or [Q/q]\n"
