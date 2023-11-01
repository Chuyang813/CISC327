import mysql.connector
from Payment import Payment
from RestaurantBrowser import RestaurantBrowser
from Restaurant import Restaurant
from UserLogin import UserLogin
from OrderSystem import OrderSystem
from ReviewSystem import ReviewSystem





def create_connection():
    connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="restaurant2db",
            port=3306  
        )
    return connection
    
    
    
def main():
    #the main method will call the functions from all 6 classes to test the functionalities
    #the program will call each of the classes in order, which simulates a user's experience of first using the program to order food from a restaurant. 
    #the user will input information like login info, then restaurant and food items, and finally payment information
    #the output will consist of messages showing either success or error in each step, and information such as order information and restaurant reviews 
    
    connection = create_connection()
    
    
    userLogin=UserLogin(connection)
    print("----------------------------------------------")
    print("Welcome to the Iber Eat Food Ordering System!")
    print("----------------------------------------------\n")
    
    
    selection = int(input("Enter the number of the option you would like to select: \n" +
          "1. Register Account\n" + 
          "2. Login\n" ))
    while True:
        if selection == 1:
            userLogin.register()
            if userLogin.login():
                break
        else:
            if userLogin.login():
                break
    
    

    browser=RestaurantBrowser(connection)
    browser.list_all()
    search_word = input("Enter the name of the restaurant or the type of food you would like to search: \n")
    found = browser.search_restaurant(search_word)
    while not found:
        search_word = input("Enter the name of the restaurant or the type of food you would like to search: \n")
        found = browser.search_restaurant(search_word)


    restaurant_name = input("Enter the name of the restaurant you would like to order from: \n")
    restaurant=Restaurant(connection, restaurant_name)
    while restaurant.view_menu() is False:
        restaurant_name = input("Enter the name of the restaurant you would like to order from: \n")
        restaurant=Restaurant(connection, restaurant_name)
        restaurant.view_menu()

    restaurant_instance = Restaurant(connection, restaurant_name)
    while True: 
        food_choice = input("Search food or press 'B' to continue: \n")

        if food_choice.upper() == "B":
            break
        else:
            restaurant.search_food(food_choice)

        restaurant_instance.search_food(food_choice)

        order_sys = OrderSystem(connection)
        order_option = input("Would you like to place an order? (Y/N) \n")
        if order_option.upper() == 'Y':
            order_sys.add_to_cart()
            order_sys.place_order(userLogin.username)
        else:
            print("Program ended.")
            return False
    
        
    pay = Payment(connection)
    if pay.initiate_payment(userLogin.username):
        # This point will be reached only if the payment is confirmed
        print("Payment processed successfully!")
    else:
        # This point will be reached if the payment is cancelled
        print("Payment was not processed!")
    #SQL statment to add customer
    restaurant.add_customer(userLogin.username)
    
    review = ReviewSystem(connection)
    review_option = input("Would you like to leave a review? (Y/N) \n")
    if review_option.upper() == 'Y':
        review.write_review(userLogin.username, restaurant_name)
    review.display_review(restaurant_name)
    

if __name__ == "__main__":
    main()