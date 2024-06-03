use std::collections::{BTreeMap, HashMap};
use chrono::prelude::*;

#[derive(Debug, PartialEq)]
pub struct Operation {
    amount: i64,
    date: String,
}

impl Operation {
    fn new(amount: i64, date: String) -> Self {
        Self { amount, date }
    }
}

#[derive(Debug, PartialEq)]
pub struct Statement {
    balance: i64,
    operations: Vec<Operation>,
}

impl Statement {
    fn new(balance: i64, operations: Vec<Operation>) -> Self {
        Self { balance, operations }
    }
}

#[derive(Default)]
pub struct Bank {
    // account -> { '2024-05-29' -> [20, -80, ...] }
    kv: HashMap<usize, BTreeMap<String, Vec<i64>>>,
}

impl Bank {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn add_operation(&mut self, account: usize, amount: i64, date: String) {
        let acc = self.kv.entry(account).or_default();
        acc.entry(date).or_default().push(amount);
    }

    pub fn balance(&self, account: usize) -> i64 {
        let today = Local::now();
        let date = format!("{}-{}-{}", today.year(), today.month(), today.day());
        self.kv.get(&account)
            .map(|acc|
                 acc.range(..=date)
                 .map(|(_, v)| v.iter().sum::<i64>()).sum()
            )
            .unwrap_or_default()
    }

    pub fn statements(&self, account: usize, start: String, end: String) -> HashMap<String, Statement> {
        let mut res = HashMap::new();
        if let Some(acc) = self.kv.get(&account) {
            for (day, amounts) in acc.range(start..=end) {
                let balance = amounts.iter().sum();
                let operations = amounts.iter().map(|a| Operation::new(*a, day.clone())).collect();
                res.insert(day.clone(), Statement::new(balance, operations));
            }
        }
        res
    }
}

#[test]
fn test_stuff() {
    let mut bank = Bank::new();
    assert_eq!(bank.balance(1), 0);
    assert_eq!(bank.statements(1, "2023-01-01".into(), "2023-12-31".into()), HashMap::new());
    bank.add_operation(1, 100000, "2050-01-01".into());
    // operations in the future shouldn't affect current balance
    assert_eq!(bank.balance(1), 0);
    bank.add_operation(1, 100000, "2024-04-15".into());
    assert_eq!(bank.balance(1), 100000);
    bank.add_operation(1, 10000, "2024-04-15".into());
    assert_eq!(bank.balance(1), 110000);
    bank.add_operation(1, 1000, "2010-01-01".into());
    assert_eq!(bank.balance(1), 111000);
}
