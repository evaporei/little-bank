from collections import defaultdict
from datetime import datetime

class Operation:
    def __init__(self, amount: int, date: str):
        self.amount = amount
        self.date = date

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
        self.operations = defaultdict(list)

    def add_operation(self, account: int, operation: Operation):
        self.operations[account].append(operation)

    def balance(self, account: int) -> int:
        return self.balances[account]

    def statements(self, account: int, start: str, end: str) -> dict[str, Statement]:
        return {}
    
    def debt_periods(self, account: int) -> list[Debt]:
        return []

bank = Bank()
assert bank.balance(1) == 0
assert bank.statements(1, '2023-01-01', '2023-12-31') == {}
bank.add_operation(1, Operation(100000, '2050-01-01'))
# operations in the future shouldn't affect current balance
assert bank.balance(1) == 0
assert bank.debt_periods(1) == []
