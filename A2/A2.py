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
    