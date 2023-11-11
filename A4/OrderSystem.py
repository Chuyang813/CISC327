import mysql.connector


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
       
        if self.items==[]:
            return False
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


       
       
       
       
