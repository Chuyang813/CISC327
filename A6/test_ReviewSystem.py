import mysql.connector
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

def test_review_data():
    review=ReviewSystem(create_connection())
    cursor=review.connection.cursor()
    cursor.execute("select * from review")
    rs=cursor.fetchall()
    assert len(rs)==4

def test_write_review(monkeypatch):
    review=ReviewSystem(create_connection())
    cursor=review.connection.cursor()
    info="good!"
    monkeypatch.setattr('builtins.input', lambda username="": info)
    review.write_review("Alice","Burger Barn")
    cursor.execute("select * from review where customerName= 'Alice' and message='good!'")
    rs=cursor.fetchall()
    assert len(rs)==1

def test_display_review(capsys):
    review=ReviewSystem(create_connection())
    result=review.display_review("Burger Barn")
    output=capsys.readouterr()
    all_output=output.out.split('\n')
    last_line=all_output[-3]

    assert last_line=="('good!',)"