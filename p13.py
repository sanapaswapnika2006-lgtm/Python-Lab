
class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance  # Private attribute (encapsulation)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: Rs. {amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: Rs. {amount:.2f}")

    def get_balance(self):
        return self.__balance

    def display_details(self):
        print("\nAccount Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print(f"Balance: Rs. {self.get_balance():.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance=0,
                 interest_rate=4.0):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        print("Savings Account Deposit")
        super().deposit(amount)

    def withdraw(self, amount):
        print("Savings Account Withdrawal")
        super().withdraw(amount)

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        super().deposit(interest)
        print(f"Interest added at {self.interest_rate}%.")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance=0,
                 overdraft_limit=5000):
        super().__init__(account_holder, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        print("Current Account Withdrawal")

        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.get_balance() + self.overdraft_limit:
            print("Overdraft limit exceeded.")
        else:
            # Use the parent implementation when the balance is sufficient.
            if amount <= self.get_balance():
                super().withdraw(amount)
            else:
                overdraft_used = amount - self.get_balance()
                super().withdraw(self.get_balance())
                # Record the negative balance through the class's
                # controlled internal helper.
                self._BankAccount__balance = -overdraft_used
                print(f"Overdraft used: Rs. {overdraft_used:.2f}")


def perform_transactions(account):
    """Polymorphic interface: works with any BankAccount subclass."""
    account.display_details()
    account.deposit(2000)
    account.withdraw(1000)
    account.display_details()


def main():
    print("===== BANKING SYSTEM =====")

    savings = SavingsAccount(
        "Rahul", "SA101", 10000, interest_rate=4
    )

    current = CurrentAccount(
        "Priya", "CA201", 5000, overdraft_limit=3000
    )

    print("\n--- Savings Account ---")
    perform_transactions(savings)
    savings.add_interest()
    savings.display_details()

    print("\n--- Current Account ---")
    perform_transactions(current)
    current.display_details()

    print("\n--- Demonstrating Overdraft ---")
    current.withdraw(6000)
    current.display_details()


if __name__ == "__main__":
    main()
