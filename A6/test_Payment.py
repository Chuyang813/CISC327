import mysql.connector
import pytest
from Payment import Payment

def create_connection():
    connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="restaurant2db",
            port=3306  
        )
    return connection

def test_select_method(monkeypatch):
    payment=Payment(create_connection())
    option="1"
    monkeypatch.setattr('builtins.input', lambda username="": option)
    result = payment.select_method()
    assert result=="Credit Card"

def test_has_payment_info():
    payment=Payment(create_connection())
    result=payment.has_payment_info("charlie789","Credit Card")
    assert result==True

def test_validate_info(monkeypatch,capsys):
    payment=Payment(create_connection())
    info=iter(["1234567898765432","1023","123"])
    monkeypatch.setattr('builtins.input', lambda _="": next(info))
    payment.validate_info("johnwick55","Credit Card")
    output=capsys.readouterr()
    assert output[0]=="Payment info successfully added!\n"



'''def test_wrong_info(monkeypatch):
    payment=Payment(create_connection())
    info=iter(["1010101010101010","0000","999"])
    monkeypatch.setattr('builtins.input', lambda _="": next(info))
    with pytest.raises(ValueError, match="Invalid expiration date"):
         payment.validate_info("johnwick55","Credit Card")'''

def test_confirm_payment(monkeypatch):
    payment=Payment(create_connection())
    info="Y"
    monkeypatch.setattr('builtins.input', lambda _="": info)
    result=payment.confirm_payment()
    assert result==True

    