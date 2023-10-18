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
    
    def select_method():
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
                
                # Display all reviews with username and date
                while line_num < len(lines) and lines[line_num] != "":
                    print(lines[line_num].strip())
                    line_num += 1
                
                
        
        

            
        


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

# Load data into RestaurantBrowser
RestaurantBrowser.load_data()
