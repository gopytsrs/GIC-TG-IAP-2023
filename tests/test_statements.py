from src.statements import StatementBook


def test_add_deposit_statement():
    statement_book = StatementBook()
    statement_book.add_deposit_statement(100, 100)
    assert len(statement_book.statements) == 1


def test_add_withdraw_statement():
    statement_book = StatementBook()
    statement_book.add_deposit_statement(100, 100)
    assert len(statement_book.statements) == 1
