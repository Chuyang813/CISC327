"""
pytest test cases for OrderSystem.py
"""
import mysql.connector
import pytest
from OrderSystem import OrderSystem
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

# Test for adding to cart
def test_add_to_cart(db_connection):
    with patch('builtins.input', side_effect=['spaghetti', 'ravioli', 'k']):
        order_system = OrderSystem(db_connection)
        order_system.add_to_cart()
        assert order_system.items == ['spaghetti', 'ravioli']

# Test for placing an order with items
def test_place_order_with_items(db_connection):
    with patch('builtins.input', side_effect=['spaghetti', 'ravioli', 'k']):
        order_system = OrderSystem(db_connection)
        order_system.add_to_cart()
        with patch('builtins.print') as mock_print:
            order_system.place_order('test_user')
            # Add assertions to check database interactions or mock_print calls

# Test for placing an order with no items
def test_place_order_no_items(db_connection):
    order_system = OrderSystem(db_connection)
    with patch('builtins.print') as mock_print:
        order_system.place_order('test_user')
        # Add assertions to verify the behavior with an empty cart