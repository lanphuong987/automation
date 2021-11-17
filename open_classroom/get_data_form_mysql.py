import self as self
from mysql.connector import MySQLConnection
import mysql.connector
from open_classroom.Courses import Courses, Lesson, Chapter


def make_cursor():
    self.conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Phuong123%",
        database="courses_db"
    )
    return self.conn.cursor()


def get_course(id, mycursor):
     mycursor.execute("SELECT * FROM course WHERE id="+str(id))
     result_set = mycursor.fetchall()
     course = Courses
     if mycursor.rowcount == 0:
         return False
     else:
         for row in result_set:
             course.name = row[1]
             course.url = row[4]
             course.description = row[3]
             course.system_id = row[2]
             course.picture_url = row[5]
             course.intro = row[6]
     return course


def get_chapter(course_id, mycursor):
    mycursor.execute("SELECT * FROM chapter WHERE course_id=" + str(course_id))
    results_set = mycursor.fetchall()
    chapters = []
    if mycursor.rowcount == 0:
        return False
    else:
        for row in results_set:
            chapter = Chapter(row[1], row[2], row[0])
            chapters.append(chapter)
    return chapters


def get_lesson(chapter_id, mycursor):
    mycursor.execute("SELECT * FROM lesson WHERE chapter_id=" + str(chapter_id))
    results_set = mycursor.fetchall()
    lessons = []
    if mycursor.rowcount == 0:
        return False
    else:
        for row in results_set:
            lesson = Lesson(row[1], row[3], row[2], row[4])
            lessons.append(lesson)
    return lessons


def get_last_course_id( mycursor):
     sql = "SELECT id FROM course ORDER BY id DESC LIMIT 1"
     mycursor.execute(sql)
     last_id = mycursor.fetchone()
     if last_id:
         for lastID in last_id:
             return lastID
     else:
        return 0


def get_last_course_id(mycursor):
    sql = "SELECT id FROM course ORDER BY id DESC LIMIT 1"
    mycursor.execute(sql)
    last_id = mycursor.fetchone()
    if last_id:
        for lastID in last_id:
            return lastID
    else:
        return 0


def get_last_chapter_id(mycursor):
    sql = "SELECT id FROM chapter ORDER BY id DESC LIMIT 1"
    mycursor.execute(sql)
    last_id = mycursor.fetchone()
    if last_id:
        for lastID in last_id:
            return lastID
    else:
        return 0


def get_last_lesson_id(mycursor):
    sql = "SELECT id FROM lesson ORDER BY id DESC LIMIT 1"
    mycursor.execute(sql)
    last_id = mycursor.fetchone()
    if last_id:
        for lastID in last_id:
            return lastID
    else:
        return 0


def get_course_by_system_id(id, mycursor):
    mycursor.execute("SELECT * FROM course WHERE system_id=" + str(id))
    result_set = mycursor.fetchall()
    course = Courses
    if mycursor.rowcount == 0:
        return False
    else:
        for row in result_set:
            course.name = row[1]
            course.description = row[3]
            course.system_id = row[2]
            course.url = row[4]
    return course






