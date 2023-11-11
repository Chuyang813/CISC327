"""
pytest for UserLogin.py
"""      
from UserLogin import UserLogin
import mysql.connector
import pytest
from unittest.mock import patch
            
@pytest.fixture(scope="module")
def db_connection():
    # Set up database connection
    connection = mysql.connector.connect(
        host='127.0.0.1',    
        user='root',      
        password='',  
        database='restaurant2db',
        port=3306     
    )
    yield connection
    # Close the database connection after the tests
    connection.close()

# Test for registering a new user
@patch('builtins.input', side_effect=['test_user', 'TestPassword123!'])
@patch('builtins.print')
def test_register_new_user(mock_print, mock_input, db_connection):
    user_login = UserLogin(db_connection)
    user_login.register()
    # Add code to verify if the user was added to the database

# Test for registering with an existing username
@patch('builtins.input', side_effect=['existing_user', 'Password123'])
@patch('builtins.print')
def test_register_existing_user(mock_print, mock_input, db_connection):
    user_login = UserLogin(db_connection)
    user_login.register()
    # Add code to verify the correct handling of existing user

# Test for successful login
@patch('builtins.input', side_effect=['johnwick55', 'john!!!'])
@patch('builtins.print')
def test_login_successful(mock_print, mock_input, db_connection):
    user_login = UserLogin(db_connection)
    assert user_login.login() == True

# Test for login with invalid username
@patch('builtins.input', side_effect=['invalid_user', 'password'])
@patch('builtins.print')
def test_login_invalid_user(mock_print, mock_input, db_connection):
    user_login = UserLogin(db_connection)
    assert user_login.login() == False

# Test for login with wrong password
@patch('builtins.input', side_effect=['johnwick55', 'WrongPassword'])
@patch('builtins.print')
def test_login_wrong_password(mock_print, mock_input, db_connection):
    user_login = UserLogin(db_connection)
    assert user_login.login() == False