import mysql.connector


class UserLogin:
    """
    This Class has three functions:
    1. init()
        - This function establishes a connection with the database.
    2. register
        -This function asks the user to register for an account with username and password.
    3. login
        -This function asks the user to login with valid credentials
    This Class has 2 variables
    1. username- username of the account
    2. password - password of the account
    """
    
    
    def __init__(self, connection):
        self.connection = connection
        self.username=""
        self.password=""
        
        
    def register(self):
        cursor = self.connection.cursor()
        
        #This function asks the user to register for an account with username and password.
        print("Please create a username.")
        username=input().strip()

        try:
            cursor.execute("SELECT username FROM customer WHERE username = %s", (username,))
            existing_user = cursor.fetchone()
            if existing_user:
                print("Registration error. Username already exists. Please choose a different username.")
                return

            print("Please create a password for your account.")
            password = input().strip()
            while len(password) < 8:
                print("Registration error. Password must be at least 8 characters long.")
                password = input().strip()
            
            self.username=username
            self.password=password
            cursor.execute("INSERT INTO customer (username, password) VALUES (%s, %s)", (username, password))
            self.connection.commit()
            print("Registration successful! Proceeding to the login page.")
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
        finally:
            cursor.close()




    def login(self):
        cursor = self.connection.cursor()
        
        #This function asks the user to login with valid credentials
        print("Please enter your username.")
        username = input().strip()

        print("Please enter your password.")
        password = input().strip()

        try:
            cursor.execute("SELECT * FROM customer WHERE username = %s AND password = %s", (username, password))
            account = cursor.fetchone()
            if account:
                self.username=username
                self.password=password
                print("\nLogin successful! Redirecting to the main page.\n")
                return True
            else:
                print("\nLogin error. Wrong username or password.\n")
                return False
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
        finally:
            cursor.close()