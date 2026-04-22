from db import get_connection
from utils import log_info, log_error
from auth import hash_password

def deposit(acc_no):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        amount = int(input("✍️Enter Amount: "))

        cursor.execute("UPDATE data SET balance = balance + %s WHERE account_no=%s", (amount, acc_no))

        cursor.execute("INSERT INTO transactions (account_no, type, amount) VALUES (%s, %s, %s)",
                       (acc_no, "DEPOSIT", amount))

        conn.commit()
        log_info(f"Deposit: {amount} to {acc_no}")
        print("😍Deposit Successful")

    except Exception as e:
        log_error(str(e))
        print("😥Error occurred during deposit")


def check_balance(acc_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM data WHERE account_no=%s", (acc_no,))
    print("💰Balance:", cursor.fetchone()[0])




def withdraw(acc_no):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT balance FROM data WHERE account_no=%s", (acc_no,))
        balance = cursor.fetchone()[0]

        amount = int(input("Enter Amount: "))

        if amount > balance:
            print("😒Insufficient Balance")
        else:
            cursor.execute("UPDATE data SET balance = balance - %s WHERE account_no=%s", (amount, acc_no))

            cursor.execute("INSERT INTO transactions (account_no, type, amount) VALUES (%s, %s, %s)",
                           (acc_no, "WITHDRAW", amount))

            conn.commit()
            log_info(f"Withdraw: {amount} from {acc_no}")
            print("👍Withdraw Successful")

    except Exception as e:
        log_error(str(e))
        print("😥Error occurred during withdrawal")
def view_transactions(acc_no):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT type, amount, created_at FROM transactions WHERE account_no=%s",
        (acc_no,)
    )

    rows = cursor.fetchall()

    print("\n----- 📜TRANSACTION HISTORY📜 -----")

    for row in rows:
        t_type, amount, date = row
        print(f"{date} | {t_type} | ₹{amount}")

    print("--------------------------------")

def change_password(acc_no):
    conn = get_connection()
    cursor = conn.cursor()

    old_pass = input("✍️Enter OLD password: ")
    new_pass = input("🔆Enter NEW password: ")

    old_hashed = hash_password(old_pass)
    new_hashed = hash_password(new_pass)

    # verify old password
    cursor.execute(
        "SELECT * FROM data WHERE account_no=%s AND pass_word=%s",
        (acc_no, old_hashed)
    )

    if cursor.fetchone():
        cursor.execute(
            "UPDATE data SET pass_word=%s WHERE account_no=%s",
            (new_hashed, acc_no)
        )
        conn.commit()
        print("✅ Password changed successfully")
    else:
        print("❌ Incorrect old password")
