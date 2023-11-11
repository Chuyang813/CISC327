import mysql.connector
from RestaurantBrowser import RestaurantBrowser

def create_connection():
    connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="restaurant2db",
            port=3306  
        )
    return connection
def test_restaurant_data():
    #original code changed to no argument for the class, connection becomes create_connection()
    restaurant=RestaurantBrowser(create_connection())
    cursor=restaurant.connection.cursor()
    cursor.execute("select * from restaurant")
    rs=cursor.fetchall()
    assert len(rs)==3

def test_search_restaurant():
    restaurant=RestaurantBrowser(create_connection())
    #cursor=restaurant.connection.cursor()
    result=restaurant.search_restaurant("Pasta Place")
    assert result==True

def test_list_all(capsys):
    restaurant=RestaurantBrowser(create_connection())
    result=restaurant.list_all()
    output=capsys.readouterr()
    all_output=output.out.split('\n')
    last_line=all_output[-5]

    assert last_line=="Website: www.veggievilla.com"