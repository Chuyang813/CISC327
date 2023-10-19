class Payment:
    """
    This Class has three functions:
    1. select_method() 
        - This function ask the user to select a payment
            method and return the selected payment method
    2. validate_info()
        - This function ask the user to enter the payment
            information and validate the information
    3. confirm_payment()
        - This function ask the user to confirm the payment
            and return the confirmation
    """
    
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
        else:
            return "Debit Card"
        
        
    
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
                
                # If all information is correct, write the information to the file
                with open("C:/CISC327/CISC327/A2/user_data.txt", "r+") as f:
                    lines = f.readlines()
                    if any(username in line for line in lines):
                        line_num = next((i for i, line in enumerate(lines) 
                                         if f"{username} - {method}" in line), None)
                        if line_num is not None:
                            while "Password:" not in lines[line_num]:
                                line_num += 1
                            line_num += 1  # move to the line after Password

                            # Insert the payment info at the found position
                            lines.insert(line_num, f"{method}:\n")
                            lines.insert(line_num + 1, f"- Card Number: {card_num}\n")
                            lines.insert(line_num + 2, f"- Expiration Date: {exp_date}\n")
                            lines.insert(line_num + 3, f"- CVV: {cvv_num}\n")
                        
                            f.seek(0)
                            f.writelines(lines)   
                            f.truncate()
                            
                print(f"Saved payment info for {username}")
                
                return True
            except ValueError as e:
                print(e)
                continue
        
        return False
        
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

payment = Payment()
username = "bob456"
method = payment.select_method()
with open("C:/CISC327/CISC327/A2/user_data.txt", "r") as f:
    lines = f.readlines()
    
    if any(username in line for line in lines):
        line_num = next((i for i, line in enumerate(lines) if f"{username} - {method}" in line), None)
        if line_num is not None:
            payment.confirm_payment()
        else:
            payment.validate_info(username, method)
            payment.confirm_payment()
            
        
        
    





class ReviewSystem:
    """
    This Class has two functions:
    1. write_review
        - This function allows the user to write a review
            to a particular restaurant
    2. display_review
        - This function allows the user to display the
            reviews of a particular restaurant
    
    """
    
    def write_review(self, username, restaurant_name):
        """
        Args:
            username (str): username for the review
            restaurant_name (str): name of the restaurant
        """
        from datetime import datetime
        
        file_path = "C:/CISC327/CISC327/A2/restaurants_test_data.txt"
        
        # Get the review from the user
        content = str(input("Please enter your review: \n"))
        if content == "":
            print("Review cannot be empty\n")
            content = str(input("Please re-enter your review: \n"))
        
        # Create review string
        review_str = f"- [{username}, {datetime.today().date()}]: {content}\n"
        
        # Open the file and write the review content to the file
        with open(file_path, "r+") as f:
            lines = f.readlines()
            
            # Find the restaurant
            if any(restaurant_name in line for line in lines):
                line_num = next((i for i, line in enumerate(lines) if restaurant_name in line), None)
                while "Reviews" not in lines[line_num]:
                    line_num += 1
                lines.insert(line_num + 1, review_str)
                f.seek(0)
                f.writelines(lines)
            
      
            
    
    def display_review(self, restaurant_name):
        """
        Args:
            restaurant_name (str): name of the restaurant
        """
        
        file_path = "C:/CISC327/CISC327/A2/restaurants_test_data.txt"
        
        with open(file_path, "r") as f:
            lines = f.readlines()
            
            # Find the restaurant
            if any(restaurant_name in line for line in lines):
                line_num = next((i for i, line in enumerate(lines) if restaurant_name in line), None)
                while "Reviews" not in lines[line_num]:
                    line_num += 1
                line_num += 1
                # Display all reviews with username and date
                print("\n" + restaurant_name + " Reviews: ")
                while line_num < len(lines) and lines[line_num].startswith("-"):
                    print(lines[line_num].strip())
                    line_num += 1
                
                
        
"""reviews = ReviewSystem()
reviews.write_review("John", "Pasta Place")  
reviews.write_review("John", "Burger Barn") 
reviews.write_review("John", "Veggie Villa") 
reviews.display_review("Pasta Place")
reviews.display_review("Burger Barn")
reviews.display_review("Veggie Villa")"""
       

            
        


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
       file_path="C:/CISC327/CISC327/A2/user_data.txt"
       f=open(file_path,"a")
       f.write("username: ")
       f.write(self.username)
       f.write("\n")
       f.write("password: ")
       f.write("")
       f.write(self.password)
       f.write("\n")
       f.close()

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
           print("Login error. Wrong password.")
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
           file_path="C:/CISC327/CISC327/A2/user_data.txt"
           f=open(file_path,"a")
           f.write("Order is placed successfully!")
           f.write("\n")
           f.write("Order ID: 1")
           f.write("\n")
           f.write("Order date: 2017-12-12 00:00:00")
           f.write("\n")
           f.write("Order total: 100")
           f.write("\n")
           f.write("Order payment method: Credit Card")
           f.close()
       #elif answer=="N":
       else:
           print("Redirecting to order page.")



class RestaurantBrowser:

    """
    This class will have 2 main functions: 
        1. search_restaurant(name: str, food_type: str): Searches for restaurants based on name or food type.
        2. list_all(): Lists all available or relevant restaurants.
    """

    # List for storing all the restaurant objects
    restaurants = []

    # Load restaurant data and create restaurant objects
    @classmethod
    def load_data(cls, filename="restaurant_test_data.txt"):
       
        with open(filename, 'r') as file:
            data = file.read().split("----------------------------------------------------")
            
            for restaurant_data in data:
                # Check if data exists and then put it in restaurant list
                if restaurant_data.strip():
                    cls.restaurants.append(Restaurant(restaurant_data.strip()))

    #Search restaurants either by name or by a type of food
    @classmethod
    def search_restaurant(cls, name="", food_type=""):
        
        results = []
        for restaurant in cls.restaurants:
            # Search by restaurant name
            if name and name in restaurant.name:
                results.append(restaurant)
            elif food_type:
                # Search by food type in the restaurant's menu
                for food in restaurant.menu:
                    if food_type.lower() in food.lower():
                        results.append(restaurant)
                        break
        
        # Display search results
        if results:
            for restaurant in results:
                restaurant.display_info()
                print("\n----------------------------------------------------\n")
        else:
            print("No matching results found.\n")

    @classmethod
    def list_all(cls):
        """
        Display information of all restaurants.
        """
        for restaurant in cls.restaurants:
            restaurant.display_info()
            print("\n----------------------------------------------------\n")


class Restaurant:

    """
    This class will have 3 main functions:
        1. view_menu(): Displays the menu for the restaurant.
        2. search_food(): Search for a particular food in the menu.
        3. view_reviews(): Displays reviews for the restaurant
    """

    # Initialize restaurant object with menu and reviews from the data
    def __init__(self, data):
        
        lines = data.split("\n")
        self.name = lines[0].split(":")[0]
        # Extract menu items
        self.menu = [item.strip() for item in lines[2:lines.index("Reviews:")]]
        # Extract reviews
        self.reviews = lines[lines.index("Reviews:") + 1:]
    
    # Display the restaurant's menu
    def view_menu(self):
        
        print("\nMenu for", self.name)
        for item in self.menu:
            print("-", item)

    # Check if a food item exists in menu
    def search_food(self, food_name):
        
        if food_name in self.menu:
            print(f"\n{food_name} is available at {self.name}\n")
        else:
            print(f"\n{food_name} is not available at {self.name}\n")

    # Display restaurant's reviews.
    def view_reviews(self):
       
        print("\nReviews for", self.name)
        for review in self.reviews:
            print(review)



"""# Load data into RestaurantBrowser
RestaurantBrowser.load_data()
def main():
    #the main method will call the functions from all 6 classes to test the functionalities
    #the program will call each of the classes in order, which simulates a user's experience of first using the program to order food from a restaurant. 
    #the user will input information like login info, then restaurant and food items, and finally payment information
    #the output will consist of messages showing either success or error in each step, and information such as order information and restaurant reviews 
    
    userLogin=UserLogin()
    userLogin.register()
    userLogin.login()

    browser=RestaurantBrowser()
    browser.search_restaurant()

    restaurant=Restaurant()
    restaurant.view_menu()
    restaurant.search_food()

    abc=OrderSystem()
    abc.add_to_cart()
    abc.place_order()

    pay=Payment()
    pay.select_method()
    pay.validate_info()
    pay.confirm_payment()

    review=ReviewSystem()
    review.write_review(userLogin.username)
    review.display_review(restaurant.name)"""

    

"""if __name__ == '__main__':
    main()"""
    

