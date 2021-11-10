from mysql.connector import MySQLConnection
import mysql.connector

def connect():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Phuong123%",
            database="courses_db"
        )
    except:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Phuong123%"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE courses_db DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        course_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Phuong123%",
            database="courses_db"
        )
        course_db_cursor = course_db.cursor()
        course_db_cursor.execute("CREATE TABLE course (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, "
                                 "course_name LONGTEXT NOT NULL,system_id LONGTEXT NOT NULL ,"
                                 "description LONGTEXT NULL, course_url LONGTEXT NULL, picture_url LONGTEXT NULL,"
                                 "intro LONGTEXT NULL)")
        course_db_cursor.execute("CREATE TABLE chapter (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, "
                                 "chapter_name LONGTEXT NOT NULL, course_id INT NOT NULL, "
                                 " FOREIGN KEY (course_id) REFERENCES courses_db.course(id) )")
        course_db_cursor.execute("CREATE TABLE lesson (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, "
                                 "lesson_name LONGTEXT NOT NULL, lesson_url LONGTEXT NULL, chapter_id INT NOT NULL, content LONGTEXT NULL, "
                                 " FOREIGN KEY (chapter_id) REFERENCES courses_db.chapter(id) )")
    db_config = {
        'host': 'localhost',
        'database': 'courses_db',
        'user': 'root',
        'password': 'Phuong123%'
    }
    conn = MySQLConnection(**db_config)

    if conn.is_connected():
        return conn





