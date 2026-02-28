class CryptoWallet:
    def __init__(self, wallet_id):
        self._walletId = wallet_id
        self._balance = 0.0
        self._transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
        self._balance += amount
        self._transactions.append(f"Deposited {amount}")
        print(f"Deposited {amount}.\n")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
        if amount > self._balance:
            print("Insufficient balance.")
            return
        self._balance -= amount
        self._transactions.append(f"Withdrew {amount}")
        print(f"Withdrew {amount}.\n")

    def check_balance(self):
        return self._balance

    def transaction_history(self):
        return self._transactions

    def get_wallet_id(self):
        return self._walletId