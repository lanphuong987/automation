from mysql.connector import MySQLConnection
import mysql.connector

from chotot.Object import Contact


def connect():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Phuong123%",
            database="car_db"
        )
    except:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Phuong123%"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE car_db DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;")
        car_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Phuong123%",
            database="car_db"
        )
        car_db_cursor = car_db.cursor()
        car_db_cursor.execute("CREATE TABLE contact (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, "
                                 "dealer LONGTEXT NOT NULL,"
                                 "brand LONGTEXT NULL, phone LONGTEXT NULL,"
                                 "c_source LONGTEXT NULL, city LONGTEXT NULL, district LONGTEXT NULL)")
    db_config = {
        'host': 'localhost',
        'database': 'car_db',
        'user': 'root',
        'password': 'Phuong123%'
    }
    conn = MySQLConnection(**db_config)

    if conn.is_connected():
        return conn


def insert_contact(c):
    query = "INSERT INTO contact(dealer, brand, phone, c_source, city, district) " \
            "VALUES(%s, %s, %s, %s, %s, %s)"
    args = (c.dealer, c.brand, c.phone, "chotot", c.city, c.district )
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, args)
    course_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    if course_id:
        return course_id
    else:
        return False

