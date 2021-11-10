import self as self
from mysql.connector import MySQLConnection
import mysql.connector
from Object import *
from database import *


def get_all_from_db(cursor):
    cursor.execute("SELECT * FROM contact")
    result_set = cursor.fetchall()
    costumers_info = []
    if cursor.rowcount == 0:
        return False
    else:
        for row in result_set:
            costumer_info = Contact(row[1], row[2], row[3], row[4], row[5], row[6])
            costumers_info.append(costumer_info)
    return costumers_info



def get_all_phone_from_db(cursor):
    cursor.execute("SELECT phone FROM contact")
    result_set = cursor.fetchall()
    phones = []
    if cursor.rowcount == 0:
        return False
    else:
        for row in result_set:
           phones.append(row[0])
    return phones


def get_all_from_db_HN(cursor):
    cursor.execute("SELECT * FROM contact where city = 'Bình Dương'")
    result_set = cursor.fetchall()
    costumers_info = []
    if cursor.rowcount == 0:
        return False
    else:
        for row in result_set:
            costumer_info = Contact(row[1], row[2], row[3], row[4], row[5], row[6])
            costumers_info.append(costumer_info)
    return costumers_info