from collections import defaultdict

class Operation:
    def __init__(self, amount: int, date: str, account: int):
        self.amount = amount
        self.date = date
        self.account = account

class Statement:
    def __init__(self, balance: int, operations: list[Operation]) -> None:
        self.balance = balance
        self.operations = operations

class Debt:
    def __init__(self, amount: int, start: str, end: str):
        self.amount = amount
        self.start = start
        self.end = end

class Bank:
    def __init__(self):
        self.balances = defaultdict(int)

    def add_operation(self, operation: Operation):
        pass

    def get_balance(self, account: int) -> int:
        return self.balances[account]

    def get_statement(self) -> dict[str, Statement]:
        pass
    
    def get_debt_periods(self) -> list[Debt]:
        pass

bank = Bank()
assert bank.get_balance(1) == 0
