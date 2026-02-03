from coin_acceptor_CLI import CoinAcceptor

def main():
    print("Program starting.")
    print("Welcome to coin acceptor program.")
    print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")
    acceptor = CoinAcceptor()
    while True:
        coin = float(input("\nInsert coin(0 return, -1 exit): "))
        if coin == -1:
            print("Exiting program.")
            break
        elif coin == 0:
            print("Returning coins...")
            amount, value = acceptor.returnCoins()
            print(f"{amount} coins with {value}€ value returned.")
            amount, value = acceptor.getStatus()
            print(f"Inserted coins = {amount}, value = {value}€")
        else:
            print("Inserting...")
            acceptor.insertCoin(coin)
            amount, value = acceptor.getStatus()
            print(f"Inserted coins = {amount}, value = {value}€")
    print("\nProgram ending.")

if __name__ == "__main__":
    main()
