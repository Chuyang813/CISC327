import mysql.connector


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
        
        print("All Restaurants:\n")
        for restaurant in restaurants:
            print(f"Name: {restaurant['name']}")
            print(f"Street: {restaurant['street']}")
            print(f"City: {restaurant['city']}")
            print(f"Postal Code: {restaurant['pc']}")
            print(f"Website: {restaurant['url']}")
            print("\n----------------------------------------------------\n")