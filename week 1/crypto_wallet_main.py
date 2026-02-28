from crypto_wallet import CryptoWallet

def main():
    wallets = {}
    while True:
        print("Crypto Wallet\n")
        print("1 - Create Wallet")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Check Balance")
        print("5 - Transaction History")
        print("0 - Exit")
        choice = input("\nChoose an option: ")

        if choice == "1":
            wallet_id = input("Enter Wallet ID: ")
            if wallet_id in wallets:
                print("Wallet already exists.")
            else:
                wallets[wallet_id] = CryptoWallet(wallet_id)
                print(f"Wallet '{wallet_id}' created successfully.\n")

        elif choice == "2":
            wallet_id = input("Enter Wallet ID: ")
            if wallet_id not in wallets:
                print("Wallet not found.")
                continue
            try:
                amount = float(input("Enter amount to deposit: "))
                wallets[wallet_id].deposit(amount)
            except ValueError:
                print("Invalid amount.")

        elif choice == "3":
            wallet_id = input("Enter Wallet ID: ")
            if wallet_id not in wallets:
                print("Wallet not found.")
                continue
            try:
                amount = float(input("Enter amount to withdraw: "))
                wallets[wallet_id].withdraw(amount)
            except ValueError:
                print("Invalid amount.")

        elif choice == "4":
            wallet_id = input("Enter Wallet ID: ")
            if wallet_id not in wallets:
                print("Wallet not found.")
                continue
            balance = wallets[wallet_id].check_balance()
            print(f"Current balance: {balance}\n")

        elif choice == "5":
            wallet_id = input("Enter Wallet ID: ")
            if wallet_id not in wallets:
                print("Wallet not found.")
                continue
            history = wallets[wallet_id].transaction_history()
            if not history:
                print("No transactions yet.")
            else:
                print("\nTransaction History:")
                for transaction in history:
                    print(f"{transaction}\n")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid menu choice.")

if __name__ == "__main__":
    main()