import secrets
import string
from cryptography.fernet import Fernet, InvalidToken
import getpass
import os
import json
import pymysql
import pandas as pd
from sshtunnel import SSHTunnelForwarder

# Your SSH and database connection parameters
ssh_host = ""
ssh_port = 22
ssh_username = "root"
ssh_password = ""
database_username = "root"
database_password = ""
database_name = "test"
localhost = "127.0.0.1"


def load_key_from_input():
    key_input = getpass.getpass(prompt="Enter your encryption key: ")
    return key_input.encode()


def open_ssh_tunnel(verbose=False):
    global tunnel
    tunnel = SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address=("127.0.0.1", 3306),
    )
    tunnel.start()


def mysql_connect():
    global connection
    connection = pymysql.connect(
        host="127.0.0.1",
        user=database_username,
        passwd=database_password,
        db=database_name,
        port=tunnel.local_bind_port,
    )


def mysql_disconnect():
    connection.close()


def close_ssh_tunnel():
    tunnel.close()


def run_query(sql):
    return pd.read_sql_query(sql, connection)


def main():
    print(
        """
    ____                                                 __
   / __ \ ____ _ _____ _____ _      __ ____   _____ ____/ /
  / /_/ // __ `// ___// ___/| | /| / // __ \ / ___// __  / 
 / ____// /_/ /(__  )(__  ) | |/ |/ // /_/ // /   / /_/ /  
/_/     \__,_//____//____/  |__/|__/ \____//_/    \__,_/   
       __  ___                                             
      /  |/  /____ _ ____   ____ _ ____ _ ___   _____      
     / /|_/ // __ `// __ \ / __ `// __ `// _ \ / ___/      
    / /  / // /_/ // / / // /_/ // /_/ //  __// /          
   /_/  /_/ \__,_//_/ /_/ \__,_/ \__, / \___//_/           
                                /____/
          """
    )

    # Load the encryption key from user input
    key = load_key_from_input()
    fernet = Fernet(key)

    # Validate the key
    try:
        if os.path.exists("demo.txt"):
            with open("demo.txt", "r") as file:
                line = file.readline().strip()
                if line:
                    fernet.decrypt(line.encode())
        print("Key validation successful!")
    except InvalidToken:
        print("Invalid encryption key. Exiting...")
        return

    open_ssh_tunnel()
    mysql_connect()

    while True:
        choice = input(
            "\nCommands:\n[store: -s] [generate: -g] [retrieve -r] [update -u] or [exit] -> "
        )

        if choice == "exit":
            print("\nGoodbye!\n")
            break

        elif choice == "-s":
            description = input(
                "\nEnter the account description (e.g Outlook, Discord, etc): "
            )
            username = input("\nEnter the account username (usually an email): ")
            password = input("\nEnter the password you want to store: ")

            # Assign an ID to the new password entry
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM passwords;")
            entry_id = cursor.fetchone()[0] + 1

            # Encrypt the password
            pass_dict = {
                "ID": entry_id,
                "Description": description,
                "Username": username,
                "Password": password,
            }
            encMessage = fernet.encrypt(json.dumps(pass_dict).encode()).decode()

            # Prepare and execute the insert SQL
            insert_sql = "INSERT INTO passwords (id, description, username, password) VALUES (%s, %s, %s, %s);"
            cursor.execute(insert_sql, (entry_id, description, username, encMessage))
            connection.commit()  # Commit the transaction

            cursor.close()
            print("Password stored in the database.")

        elif choice == "-g":

            def generate_password(length=12):
                alphabet = string.ascii_letters + string.digits + string.punctuation
                password = "".join(secrets.choice(alphabet) for i in range(length))
                return password

            print(f"\nGenerated password: {generate_password()}")

        elif choice == "-r":
            select_sql = "SELECT * FROM passwords;"
            df = run_query(select_sql)
            for _, row in df.iterrows():
                decMessage = fernet.decrypt(row["password"].encode()).decode()
                pass_dict = json.loads(decMessage)
                print(
                    f"ID: {pass_dict['ID']} | Description: {pass_dict['Description']} | Username: {pass_dict['Username']} | Password: {pass_dict['Password']}"
                )

        elif choice == "-u":
            update_id = input("Type the ID of the password you would like to update: ")

            cursor = connection.cursor()
            select_sql = "SELECT * FROM passwords;"
            df = run_query(select_sql)
            found = False

            for _, row in df.iterrows():
                decMessage = fernet.decrypt(row["password"].encode()).decode()
                pass_dict = json.loads(decMessage)
                if str(pass_dict["ID"]) == update_id:
                    found = True
                    # Prompt for new password details
                    description = input("Enter a new description: ")
                    username = input("Enter a new username: ")
                    password = input("Enter a new password: ")
                    pass_dict["Description"] = description
                    pass_dict["Username"] = username
                    pass_dict["Password"] = password
                    encMessage = fernet.encrypt(json.dumps(pass_dict).encode()).decode()

                    update_sql = "UPDATE passwords SET description=%s, username=%s, password=%s WHERE id=%s;"
                    cursor.execute(
                        update_sql, (description, username, encMessage, update_id)
                    )
                    connection.commit()  # Commit the transaction
                    print("Password updated")
                    break

            if not found:
                print("ID not found")

            cursor.close()

    mysql_disconnect()
    close_ssh_tunnel()


if __name__ == "__main__":
    main()
