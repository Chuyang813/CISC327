import mysql.connector

class Payment:
    """
    This Class has five functions:
    1. init()
        - This function establishes a connection with the database.
    2. select_method() 
        - This function ask the user to select a payment
            method and return the selected payment method
    3. validate_info()
        - This function ask the user to enter the payment
            information and validate the information
    4. has_payment_info()
        - This function checks if the database has the stored payment info for the customer.
    5. confirm_payment()
        - This function ask the user to confirm the payment
            and return the confirmation
    """
    def __init__(self, connection):
        self.connection = connection
    
    def select_method(self):
        """
        This function ask the user to select a payment
        method and return the selected payment method
        """
        
        # Ask the user to select a payment method
        print("Please select a payment method: \n" + 
                "1. Credit Card \n" +
                "2. Debit Card \n")
        # Get the user's input
        payment_method = input("Enter the number of the payment method: ")
        
        # Return the selected payment method
        if payment_method == "1":
            return "Credit Card"
        elif payment_method == "2":
            return "Debit Card"
        else:
            print("Invalid input. Please enter 1 or 2.")
            return self.select_method()
        
        
    def has_payment_info(self, username, method):
        
        ### Access SQL database and check if the user has payment info ###
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT creditCardNumber FROM customer WHERE username = %s", (username,))
            credit_info = cursor.fetchone()

            cursor.execute("SELECT debitCardNumber FROM customer WHERE username = %s", (username,))
            debit_info = cursor.fetchone()

            if credit_info and credit_info[0] and method == "Credit Card":
                return True
            elif debit_info and debit_info[0] and method == "Debit Card":
                return True
            else:
                print("Payment info not found\n")
                return False


        except mysql.connector.Error as err:
            print("Error: {}".format(err))
        finally:
            cursor.close()

    def validate_info(self, username, method):
            while True:
                try:
                    card_num = int(input("Please enter your card number (aaaabbbbccccdddd):\n"))
                    if card_num < 0 or card_num > 9999999999999999:
                        raise ValueError("Invalid card number")
                    
                    exp_date = input("Please enter your card expiration date (MMYY):\n")
                    month, year = int(exp_date[:2]), int(exp_date[2:])
                    if month < 1 or month > 12:
                        raise ValueError("Invalid expiration date")
                    elif year < 23:
                        raise ValueError("Invalid expiration date")
                    
                    cvv_num = int(input("Please enter your card CVV number:\n"))
                    if cvv_num < 0 or cvv_num > 999:
                        raise ValueError("Invalid CVV number")
                    break
                except ValueError as e:
                    print(e)
                    continue
                    
            ### Access SQL database and write the payment info to the database ###
            cursor = self.connection.cursor()
            try:
                if method=="Credit Card": 
                    cursor.execute("UPDATE customer SET creditCardNumber=%s, creditExpirationDate=%s, creditCVV=%s WHERE username=%s", (card_num, exp_date, cvv_num, username))
                    self.connection.commit()
                    print("Payment info successfully added!")
                else:
                    cursor.execute("UPDATE customer SET debitCardNumber=%s, debitExpirationDate=%s, debitCVV=%s WHERE username=%s", (card_num, exp_date, cvv_num, username))
                    self.connection.commit()
                    print("Payment info successfully added!")

            except mysql.connector.Error as err:
                print("Error: {}".format(err))
            finally:
                cursor.close()
                
    def confirm_payment(self):
        while True:
            confirm = input("Confirm payment? (Y/N): ").lower()
            if confirm == "y":
                print("Payment confirmed\n")
                return True
            elif confirm == "n":
                print("Payment cancelled\n")
                return False
            else:
                print("Invalid input. Please enter Y or N.")

    def initiate_payment(self, username1):
        #username1 is used to avoid confusion
        method = self.select_method()
        
        if self.has_payment_info(username1, method):
            use_saved = input(f"Do you want to use saved {method} information? (Y/N): ").lower()
            if use_saved == 'n':
                self.validate_info(username1, method)
        else:
            self.validate_info(username1, method)
        
        return self.confirm_payment()