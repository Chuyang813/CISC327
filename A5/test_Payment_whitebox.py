import pytest
from Payment import Payment
from unittest import mock
import mysql.connector


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
    
def test_select_method(db_connection):
    payment = Payment(db_connection)
    with mock.patch('builtins.input', side_effect=['1']):
        assert payment.select_method() == "Credit Card"
    with mock.patch('builtins.input', side_effect=['2']):
        assert payment.select_method() == "Debit Card"
    with mock.patch('builtins.input', side_effect=['3', '1']):
        assert payment.select_method() == "Credit Card"
    with mock.patch('builtins.input', side_effect=['3', '2']):
        assert payment.select_method() == "Debit Card"
        
def test_has_payment_info(db_connection):
    payment = Payment(db_connection)
    assert payment.has_payment_info("alice123", "Credit Card") == True
    assert payment.has_payment_info("bob456", "Credit Card") == True
    assert payment.has_payment_info("bob456", "Debit Card") == True
    assert payment.has_payment_info("charlie789", "Credit Card") == True
    assert payment.has_payment_info("charlie789", "Debit Card") == False
    assert payment.has_payment_info("johnwick55", "Credit Card") == True
    assert payment.has_payment_info("johnwick55", "Debit Card") == False
    
    
def test_validate_info(db_connection, capfd):
    payment = Payment(db_connection)
    with mock.patch('builtins.input', side_effect=['1234567890123456', '0324', '123']):
        payment.validate_info("alice123","Credit Card")
        out, err = capfd.readouterr()
        assert "Payment info successfully added!" in out
    with mock.patch('builtins.input', side_effect=['1234567890123456', '0324', '123']):
        payment.validate_info("alice123","Debit Card")
        out, err = capfd.readouterr()
        assert "Payment info successfully added!" in out
    with mock.patch('builtins.input', side_effect=['9764567890123456', '0329', '656']):
        payment.validate_info("test_user","Credit Card")
        out, err = capfd.readouterr()
        assert "Payment info successfully added!" in out
    with mock.patch('builtins.input', side_effect=['1234569468123456', '0226', '875']):
        payment.validate_info("test_user","Debit Card")
        out, err = capfd.readouterr()
        assert "Payment info successfully added!" in out
    


        
