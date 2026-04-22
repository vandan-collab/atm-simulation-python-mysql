from db import get_connection
from utils import log_info
import hashlib
import random
import string


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def generate_account_number():
    return random.randint(100000000, 999999999)


def generate_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))


def register():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("✍️Enter Name: ")

    acc_no = generate_account_number()
    raw_password = generate_password()
    hashed_password = hash_password(raw_password)

    balance = int(input("💰Enter Initial Deposit: "))

    cursor.execute(
        "INSERT INTO data (my_name, pass_word, balance, account_no) VALUES (%s,%s,%s,%s)",
        (name, hashed_password, balance, acc_no)
    )
    conn.commit()

    print("\n🎉 Account Created Successfully!")
    print(f"Account Number: {acc_no}")
    print(f"Password: {raw_password}")
    print("⚠️ Please save these details securely!")

    log_info(f"New account created: {acc_no}")

def login():
    conn = get_connection()
    cursor = conn.cursor()

    acc_no = int(input("✍️Enter Account Number: "))
    password = hash_password(input("Enter Password: "))

    cursor.execute(
        "SELECT * FROM data WHERE account_no=%s AND pass_word=%s",
        (acc_no, password)
    )

    return cursor.fetchone()
