"""
pytest test cases for Restaurant.py
"""
import mysql.connector
import pytest
from Restaurant import Restaurant
from unittest.mock import patch

@pytest.fixture(scope='module')
def db_connection():
    connection = mysql.connector.connect(
        host='127.0.0.1',    
        user='root',      
        password='',  
        database='restaurant2db',
        port=3306
    )
    yield connection
    connection.close()

def test_view_menu(db_connection):
    restaurant = Restaurant(db_connection, 'Burger Barn')
    with patch('builtins.print') as mock_print:
        restaurant.view_menu()
        assert mock_print.call_count == 4
        
def test_view_menu_invalid(db_connection):
    restaurant = Restaurant(db_connection, 'Invalid Restaurant')
    assert restaurant.view_menu() == False
    
def test_search_food(db_connection):
    restaurant = Restaurant(db_connection, 'Burger Barn')
    with patch('builtins.print') as mock_print:
        restaurant.search_food('burger')
        assert mock_print.call_count == 4

def test_search_food_invalid(db_connection):
    restaurant = Restaurant(db_connection, 'Burger Barn')
    assert restaurant.search_food('pasta') == None
    
    
"""def test_view_reviews(db_connection):
    restaurant = Restaurant(db_connection, 'Burger Barn')
    with patch('builtins.print') as mock_print:
        restaurant.view_reviews()
        assert mock_print.call_count == 2"""
        
def test_add_customer(db_connection):
    restaurant = Restaurant(db_connection, 'Burger Barn')
    restaurant.add_customer('test_user')
    cursor = restaurant.connection.cursor()
    cursor.execute("SELECT * FROM customer WHERE username = 'test_user'")
    result = cursor.fetchall()
    assert len(result) == 1