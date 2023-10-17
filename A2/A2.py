class Payment:
    """
    This Class has three functions:
    1. select_method 
        - This function ask the user to select a payment
            method and return the selected payment method
    2. validate_info
        - This function ask the user to enter the payment
            information and validate the information
    3. confirm_payment
        - This function ask the user to confirm the payment
            and return the confirmation
    """
    
    def select_method():
        """
        This function ask the user to select a payment
        method and return the selected payment method
        """
        
        # Ask the user to select a payment method
        print("Please select a payment method:")
        print("1. Credit Card")
        print("2. Debit Card")
        # Get the user's input
        payment_method = input("Enter the number of the payment method: ")
        # Return the selected payment method
        return payment_method
    
    def validate_info():
        """
        This function ask the user to enter the payment details and validate them 
        """
        while True:
            # Ask the user to enter the payment details
            card_num = input("Please enter your card number:\n")
            if card_num < 0 or card_num > 9999999999999999:
                print("Invalid card number")
                break
            
            exp_date = input("Please enter your card expiration date (MM/YY):\n")
            if exp_date[:2] < 1 or exp_date > 12:
                print("Invalid expiration date")
                break
            
            elif exp_date[2:] < 23:
                print("Invalid expiration date")
                break
            
            cvv_num = input("Please enter your card CVV number:\n")
            if cvv_num < 0 or cvv_num > 999:
                print("Invalid CVV number")
                break
            
            
            # If all infomation is correct, write the information to the file with
            # the corresponding user
            
            ## CODE HERE ##
            
            # Return True if all the information is valid
            return True
        
        # Return False if any of the information is invalid
        return False
        
    def confirm_payment():
        """
        This function ask the user to confirm the payment
        and return the confirmation
        """
        
        # Ask the user to confirm the payment
        confirm = input("Confirm payment? (Y/N): ")
        # Return the confirmation
        return confirm    


class ReviewSystem:
    """
    
    """


class UserLogin:
   """
      This Class has 2 functions:
      1. register
           -This function asks the user to register for an account with username and password.
      2. login
           -This function asks the user to login with valid credentials
       This Class has 2 variables
       1. username- username of the account
       2. password - password of the account
   """

   username=""
   password=""
   def register(self):
       #This function asks the user to register for an account with username and password.
       print("Please create a username.")
       username=input()
       self.username=username

       print("Please create a password for your account.")
       password = input()
       while (len(password)<8):
           # error checking
           print("Registration error. Password must be at least 8 characters long.")#error checking
           password = input()
       self.password=password
       print("Registration successful! Proceeding to the login page.")


   def login(self):
       #This function asks the user to login with valid credentials
       print("Please enter your username.")
       username=input()
       while (self.username!=username):
           # error checking
           print("Login error. Wrong username.")
           username = input()
       print("Please enter your password.")
       password=input()
       while (self.password!=password):
           # error checking
           print("Login error. Wrong username.")
           password = input()
       print("Login successful! Redirecting to the main page.")




class OrderSystem:
   """
      This Class has 2 functions:
      1. add_to_cart()
           -This function asks the user to add a food item from the menu to the shopping cart.
      2. place_order
           -This function helps confirm and place the order
       This Class has 1 variable:
       1.items - stores the list of food items in the order
   """
   items=[]
   def add_to_cart(self):
       item=""
       while(item!="k"):
           print("Please enter the food item you would like to add to the shopping cart.(enter k to stop)")
           item=input()
           self.items.append(item)
       self.items.remove("k")
   def place_order(self):
       print("Please confirm the following ordered food items:")
       print(self.items)
       answer=input("Is this the order you want? (Y/N)")
       if answer=="Y":
           print("Order is placed successfully!")
           print("Order ID: 1")
           print("Order date: 2017-12-12 00:00:00")
           print("Order total: 100")
           print("Order payment method: Credit Card")
       #elif answer=="N":
       else:
           print("Redirecting to order page.")

