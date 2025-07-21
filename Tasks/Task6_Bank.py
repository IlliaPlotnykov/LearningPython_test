class BankAccount:
    def __init__(self, account_number: int, balance: int = 0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: int):
        if amount > 0:
            self.balance += amount
            print(f'На рахунку: {self.balance}')
        else:
            print('Помилка: сума має бути більшою за 0')

    def withdraw(self, amount: int):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'На рахунку: {self.balance}')
        else:
            print('Помилка: недостатньо коштів або неправильна сума')

    def get_balance(self) -> int:
        return self.balance


# Приклад використання
acc1 = BankAccount(12345678)
acc1.deposit(1000)      # На рахунку: 1000
acc1.withdraw(300)      # На рахунку: 700
print("Поточний баланс:", acc1.get_balance())  # Поточний баланс: 700
