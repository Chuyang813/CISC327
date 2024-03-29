import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="restaurant2db",
            port=3306  
        )
    
    if connection.is_connected():
        print("Successful connect to database")
        return connection
    else:
        print("Fail to connect to database")
        return None


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
        else:
            return "Debit Card"
        
        
    def has_payment_info(self, username, method):
        
        ### Access SQL database and check if the user has payment info ###
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT creditCardNumber FROM customer WHERE username = %s", (username,))
            credit_info=cursor.fetchone()
            if credit_info and method=="Credit Card":
                return True
            else:
                cursor.execute("SELECT debitCardNumber FROM customer WHERE username = %s", (username,))
                debit_info=cursor.fetchone()
                if debit_info:
                    return True
                else:
                    print("Payment info not found\n")
                    return False

        except mysql.connector.Error as err:
            print("Error: {}".format(err))
        finally:
            cursor.close()
        
        """with open("C:/CISC327/CISC327/A2/user_data.txt", "r") as f:
            lines = f.readlines()
        
        # Find the username
        user_line = next((i for i, line in enumerate(lines) if f"Username: {username}" in line), None)
        
        # If username is not found, return False
        if user_line is None:
            print("Username not found\n")
            return False

        # If username is found, search for the payment method under this username
        for i in range(user_line, len(lines)):
            if lines[i+2].strip() == method + ":":
                print("Payment info found\n")
                return True
            elif "Username:" in lines[i]:
                break
"""
        
        
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
                
            """# If all information is correct, write the information to the file
                with open("C:/CISC327/CISC327/A2/user_data.txt", "r+") as f:
                    lines = f.readlines()
                    line_num = next((i for i, line in enumerate(lines) if f"Username: {username}" in line), None)
                    if line_num is not None:
                        # Find the line after the Password
                        while "Password:" not in lines[line_num]:
                            line_num += 1
                        line_num += 1
                        
                        # Insert the payment info at the found position
                        lines.insert(line_num, f"{method}:\n")
                        lines.insert(line_num + 1, f"- Card Number: {card_num}\n")
                        lines.insert(line_num + 2, f"- Expiration Date: {exp_date}\n")
                        lines.insert(line_num + 3, f"- CVV: {cvv_num}\n")
                        
                        f.seek(0)
                        f.writelines(lines)
                        f.truncate()
                            
                print(f"Saved payment info for {username}\n")
                
                return True"""

        
        
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


## Payment class test
"""payment = Payment()
username = "bob456"
method = payment.select_method()
if payment.has_payment_info(username, method):
    payment.confirm_payment()
else:
    payment.validate_info(username, method)
    payment.confirm_payment()
"""
        
        
    





class ReviewSystem:
    """
    This Class has three functions:
    1. init()
        - This function establishes a connection with the database.
    2. write_review
        - This function allows the user to write a review
            to a particular restaurant
    3. display_review
        - This function allows the user to display the
            reviews of a particular restaurant
    
    """
    def __init__(self, connection):
        self.connection = connection
    
    def write_review(self, username, restaurant_name):
        """
        Args:
            username (str): username for the review
            restaurant_name (str): name of the restaurant
        """
        from datetime import datetime
    
        content = str(input("Please enter your review: \n"))
        while(content == ""):
            print("Review cannot be empty\n")
            content = str(input("Please re-enter your review: \n"))
        
        now=datetime.now()
        review_date=now.strftime("%Y-%m-%d")
        
        
        ### Access SQL database and write review to the database ###
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO review (message, customerName, reviewDate) VALUES (%s, %s, %s)", (content, username, review_date))
            cursor.execute("INSERT INTO restauranthasreview (restaurantName, reviewMessage) VALUES (%s, %s)", (restaurant_name, content))
            self.connection.commit()
            print("Review successfully added!")
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
        finally:
            cursor.close()
        
        """file_path = "C:/CISC327/CISC327/A2/restaurants_test_data.txt"
        
        #Get the review from the user
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
                f.writelines(lines)"""
            
      
            
    
    def display_review(self, restaurant_name):
        """
        Args:
            restaurant_name (str): name of the restaurant
        """
        cursor = self.connection.cursor()
        ### Access SQL database and display reviews for the restaurant ###
        try:
            query = """
            SELECT message FROM `review` join restauranthasreview join restaurant on restaurantName=restaurant.name and 
            message=reviewMessage where restaurant.name=%s
            """
            cursor.execute(query, (restaurant_name,))
            review = cursor.fetchall()
            if review:
                print("Reviews for",restaurant_name)
                for reviews in review:
                    print(reviews)
            else:
                print("No reviews found.")
                return

          
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
        finally:
            cursor.close()
        """file_path = "C:/CISC327/CISC327/A2/restaurants_test_data.txt"
        
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
                    line_num += 1"""
                
                
## ReviewSystem class test       
"""reviews = ReviewSystem()
reviews.write_review("John", "Pasta Place")  
reviews.write_review("John", "Burger Barn") 
reviews.write_review("John", "Veggie Villa") 
reviews.display_review("Pasta Place")
reviews.display_review("Burger Barn")
reviews.display_review("Veggie Villa")"""
       

        

    

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
                print("Login successful! Redirecting to the main page.\n")
            else:
                print("Login error. Wrong username or password.\n")
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
        finally:
            cursor.close()
            




class OrderSystem:
   """
      This Class has 3 functions:
      1. init()
        - This function establishes a connection with the database.
      2. add_to_cart()
           -This function asks the user to add a food item from the menu to the shopping cart.
      3. place_order
           -This function helps confirm and place the order
       This Class has 1 variable:
       1.items - stores the list of food items in the order
   """
        
   def __init__(self, connection):
        self.connection = connection
        self.items=[]
       
  
   def add_to_cart(self):
       item=""
       while(item!="k"):
           print("Please enter the food item you would like to add to the shopping cart.(enter k to stop)")
           item=input()
           self.items.append(item)
       self.items.remove("k")
       
   def place_order(self, username):
        ### Access SQL database and add order information to the database ###
        cursor = self.connection.cursor()
        from datetime import datetime
        import random
        order_id = random.randint(100000,999999)
        price = random.randint(0,200)
        tip = random.randint(0,20)

        now = datetime.now()
        order_time = now.strftime("%H:%M:%S")
    
        try:
            cursor.execute("INSERT INTO order1 (id,price,tip,placementTime, customerUserName) VALUES (%s, %s, %s, %s, %s)", 
                        (order_id, price, tip, order_time, username))
            self.connection.commit()
            print("Order is placed successfully!")
        except Exception as e:
            print(f"Error while placing order: {e}")
        finally:
            cursor.close()


       
        """print("Please confirm the following ordered food items:")
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
           f.close()"""
       #elif answer=="N":
       #else:
       #    print("Redirecting to order page.")



class RestaurantBrowser:

    """
    This class will have 2 main functions: 
        1. search_restaurant(name: str, food_type: str): Searches for restaurants based on name or food type.
        2. list_all(): Lists all available or relevant restaurants.
    """

    def __init__(self, connection):
        self.connection = connection
        
        
    #Search restaurants either by name or by a type of food
    
    def search_restaurant(self, search_input=""):
        cursor = self.connection.cursor(dictionary=True)

        if not search_input:
            print("Please provide a search input.")
            return

        query = """
        SELECT r.*, f.name as food_name 
        FROM restaurant r
        LEFT JOIN restaurantOffersFoodItem rofi ON r.name = rofi.restaurantName
        LEFT JOIN foodItem f ON rofi.foodItemName = f.name
        WHERE r.name LIKE %s OR f.name LIKE %s
        """

        search_filter = "%" + search_input + "%"
        cursor.execute(query, (search_filter, search_filter))

        results = cursor.fetchall()

        if results:
            last_restaurant_name = ""
            for restaurant in results:
                if restaurant['name'] != last_restaurant_name:
                    print(f"\nName: {restaurant['name']}")
                    print(f"Street: {restaurant['street']}")
                    print(f"City: {restaurant['city']}")
                    print(f"Postal Code: {restaurant['pc']}")
                    print(f"Website: {restaurant['url']}")
                    print("\nRelated Food Items:")
                    last_restaurant_name = restaurant['name']

                if restaurant['food_name']:
                    print(f"- {restaurant['food_name']}")
            print("\n----------------------------------------------------\n")
        else:
            print("No matching results found.\n")


    
    def list_all(self):
        cursor = self.connection.cursor(dictionary=True)
    
        cursor.execute("SELECT * FROM restaurant")
        restaurants = cursor.fetchall()
        
        if not restaurants:
            print("No restaurants found.\n")
            return
        
        for restaurant in restaurants:
            print(f"Name: {restaurant['name']}")
            print(f"Street: {restaurant['street']}")
            print(f"City: {restaurant['city']}")
            print(f"Postal Code: {restaurant['pc']}")
            print(f"Website: {restaurant['url']}")
            print("\n----------------------------------------------------\n")

class Restaurant:

    
    """This class will have 3 main functions:
        1. view_menu(): Displays the menu for the restaurant.
        2. search_food(): Search for a particular food in the menu.
        3. view_reviews(): Displays reviews for the restaurant
        4. add_customer(): Adds a new customer to the restaurant
    """

    # Initialize restaurant object with menu and reviews from the data
    def __init__(self, connection, name):
        self.connection = connection
        self.name = name
    
    # Display the restaurant's menu
    def view_menu(self):
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM foodItem WHERE name IN (SELECT foodItemName FROM restaurantOffersFoodItem WHERE restaurantName = %s)"
        cursor.execute(query, (self.name,))
        items = cursor.fetchall()

        if items:
            print(f"\nMenu for {self.name}:")
            for item in items:
                print("-", item['name'])
        else:
            print(f"No menu items found for {self.name}.")
            return False

    # Check if a food item exists in menu
    def search_food(self, food_name):
        
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM foodItem WHERE name = %s AND name IN (SELECT foodItemName FROM restaurantOffersFoodItem WHERE restaurantName = %s)"
        cursor.execute(query, (food_name, self.name))
        item = cursor.fetchone()

        if item:
            print(f"\n{food_name} is available at {self.name}\n")
        else:
            print(f"\n{food_name} is not available at {self.name}\n")
    # Display restaurant's reviews.
    def view_reviews(self):
       
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM review WHERE restaurantName = %s"
        cursor.execute(query, (self.name,))
        reviews = cursor.fetchall()

        if reviews:
            print(f"\nReviews for {self.name}:")
            for review in reviews:
                print("Rating:", review['rating'])
                print("Comment:", review['comment'])
                print("----------------------------------------------------")
        else:
            print(f"No reviews found for {self.name}.")
    def add_customer(self, username1):
        cursor=self.connection.cursor()
        try:
            #checks if the customer is already in the database
            cursor.execute("SELECT * FROM restaurantservescustomer WHERE restaurantName= %s and username = %s", (self.name, username1))
            result=cursor.fetchall()
            if result:
                unique=False
            else:
                unique=True
            if unique:
                cursor.execute("INSERT INTO restaurantservescustomer (restaurantName, username) VALUES (%s, %s)", (self.name, username1))
            self.connection.commit()

        except mysql.connector.Error as err:
            print("Error: {}".format(err))

        finally:
            cursor.close()

        



# Load data into RestaurantBrowser
#RestaurantBrowser.load_data()
def main():
    #the main method will call the functions from all 6 classes to test the functionalities
    #the program will call each of the classes in order, which simulates a user's experience of first using the program to order food from a restaurant. 
    #the user will input information like login info, then restaurant and food items, and finally payment information
    #the output will consist of messages showing either success or error in each step, and information such as order information and restaurant reviews 
    
    connection = create_connection()
    
    
    userLogin=UserLogin(connection)
    print("Welcome to the Food Ordering System!")
    selection = int(input("Enter the number of the option you would like to select: \n" +
          "1. Register Account\n" + 
          "2. Login\n" ))
    if selection == 1:
        userLogin.register()
        userLogin.login()
    else:
        userLogin.login()
    
    

    browser=RestaurantBrowser(connection)
    browser.list_all()
    search_word = input("Enter the name of the restaurant or the type of food you would like to search: \n")
    browser.search_restaurant(search_word)

    restaurant_name = input("Enter the name of the restaurant you would like to order from: \n")
    restaurant=Restaurant(connection, restaurant_name)
    while restaurant.view_menu() is False:
        restaurant_name = input("Enter the name of the restaurant you would like to order from: \n")
        restaurant=Restaurant(connection, restaurant_name)
        restaurant.view_menu()
    food_search = input("Search food or press 'B' to continue: \n")
    if food_search.upper() == "B":
        order_sys = OrderSystem(connection)
        order_option = input("Would you like to place an order? (Y/N) ")
        if order_option.upper() == 'Y':
            order_sys.add_to_cart()
            order_sys.place_order(userLogin.username)
    else:
        restaurant.search_food(food_search)
    #abc=OrderSystem()
    #abc.add_to_cart()
    #abc.place_order()
    

    #pay=Payment()
    #pay.select_method()
    #pay.validate_info()
    #pay.confirm_payment()
    pay = Payment(connection)
    if pay.initiate_payment(userLogin.username):
        # This point will be reached only if the payment is confirmed
        print("Payment processed successfully!")
    else:
        # This point will be reached if the payment is cancelled
        print("Payment was not processed!")
    #SQL statment to add customer
    restaurant.add_customer(userLogin.username)


    #review=ReviewSystem()
    #review.write_review(userLogin.username)
    #review.display_review(restaurant.name)
    review = ReviewSystem(connection)
    review_option = input("Would you like to leave a review? (Y/N) ")
    if review_option.upper() == 'Y':
        review.write_review(userLogin.username, restaurant_name)
    review.display_review(restaurant_name)

    

if __name__ == '__main__':
    
    
    main()
    

