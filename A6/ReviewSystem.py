import mysql.connector

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