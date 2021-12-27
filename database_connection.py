'''
@author: Shivam Mishra
@date: 26-12-21 6:56 PM
'''

from mysql.connector import connect, Error
import os
from dotenv import load_dotenv
load_dotenv()


class DBConnection:
    """Contains method which establishes connection with database"""

    @staticmethod
    def establish_connection():
        """
        Establish connection with database
        :return: connection
        """
        try:
            connection=connect(
                host=os.getenv('host'),
                user=os.getenv('user_name'),
                password=os.getenv('password'),
                database='payroll_details'
            )
            print("Connection established successfully...")
            return connection
        except Error as e:
            print(e)










