from src.logger import Logger


def test_print_withdraw_success_message(capfd):
    Logger.print_withdraw_success(100)
    out, _ = capfd.readouterr()
    assert out == f"Thank you. ${100:.2f} has been withdrawn to your account.\n"


def test_print_deposit_success_message(capfd):
    Logger.print_deposit_success(100)
    out, _ = capfd.readouterr()
    assert out == f"Thank you. ${100:.2f} has been deposited to your account.\n"
