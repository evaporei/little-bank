from collections import defaultdict
from datetime import date

class Operation:
    def __init__(self, amount: int, d: str):
        self.amount = amount
        self.date = date.fromisoformat(d)

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
        b = 0
        t = date.today()
        for op in self.operations[account]:
            if t >= op.date:
                b += op.amount
        return b

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

bank.add_operation(1, Operation(100000, '2024-04-15'))
assert bank.balance(1) == 100000
assert bank.debt_periods(1) == []
