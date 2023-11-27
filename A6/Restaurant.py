import mysql.connector


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
        query = "SELECT * FROM foodItem WHERE name LIKE %s AND name IN (SELECT foodItemName FROM restaurantOffersFoodItem WHERE restaurantName = %s)"
        cursor.execute(query, ('%' + food_name + '%', self.name))
        item = cursor.fetchall()

        if item:
            print(f"\nItems related to '{food_name}' available at {self.name}:")
            for i in item:
                print("-", i['name'])
        else:
            print(f"\nNo items related to '{food_name}' found at {self.name}.\n")


    # Display restaurant's reviews.
    def view_reviews(self):
       
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM restauranthasreview WHERE restaurantName = %s"
        cursor.execute(query, (self.name,))
        reviews = cursor.fetchall()

        if reviews:
            print(f"\nReviews for {self.name}:")
            for review in reviews:
                print("-", review['reviewMessage'])
                
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
