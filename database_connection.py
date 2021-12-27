'''
@author: Shivam Mishra
@date: 26-12-21 6:56 PM
'''
from mysql.connector import connect, Error

try:
    with connect(
            host="localhost",
            user="root",
            password="root"
    ) as connection:
        print("Connection established successfully...")

except Error as e:
    print(e)