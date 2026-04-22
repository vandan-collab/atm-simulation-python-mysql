from auth import register, login
from operations import check_balance, deposit, withdraw, view_transactions, change_password


def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("✍️Enter choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            user = login()

            if user:
                acc_no = user[3]
                print("☑️Login Successful")

                while True:
                    print("\n1. Balance\n2. Deposit\n3. Withdraw\n4. View Transactions\n5. Change Password\n6. Logout")
                    opt = input("🔆Choose: ")

                    if opt == "1":
                        check_balance(acc_no)

                    elif opt == "2":
                        deposit(acc_no)

                    elif opt == "3":
                        withdraw(acc_no)

                    elif opt == "4":
                        view_transactions(acc_no)

                    elif opt == "5":
                        change_password(acc_no)

                    elif opt == "6":
                        print("👋Logged out successfully👋")
                        break

                    else:
                        print("❌ Invalid option")

            else:
                print("❌Invalid Credentials")

        elif choice == "3":
            print("bye 👋")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()