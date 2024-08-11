import random

from config_handler import load_data, save_data

print("\nWelcome to Dank memer playground")

while True:
    playing = input("\nDo you want to play? ( Yes or No ) ").lower()

    if playing == "yes":
        print("\nOkay let's play!")
        break

    elif playing == "no":
        quit()

    else:
        print("\nInvalid Input!\nPlease try again.")

while True:
    data = load_data()  # Load data at the start of each iteration
    print("\n1. Get started")
    print("2. Show balance")
    print("3. Beg")
    print("4. Bankrob")
    print("5. Quit\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        get_started = random.randint(1, 1000)
        data["balance"] += get_started
        save_data(data)  # Save the changes
        print(f"\nYou got started with {get_started} coins!")

    elif choice == "2":
        print(f"\nYour balance is {data["balance"]}")

    elif choice == "3":
        beg = random.randint(1, 1000)
        data["balance"] += beg
        save_data(data)  # Save the changes
        print(f"\nOh you little poor soul, here have {beg}")

    elif choice == "4":
        outcome = random.choice(['successful', 'unsuccessful'])

        if outcome == 'successful':
            bankrob = random.randint(1, 100000)
            data["balance"] += bankrob
            save_data(data)  # Save the changes
            print(f"\nYou robbed the bank successfully and found {bankrob}")

        else:
            print("\nYou got caught and arrested :(")

    elif choice == "5":
        print("\nThanks for playing")
        quit()

    else:
        print("\nInvalid Input!\nPlease try again.")