'''
@author: Shivam Mishra
@date: 27-12-21 12:57 PM
@desc: Performed all CURD operations in sql
'''
from database_connection import DBConnection


class DBOperations:
    """Contains methods to execute query, show databases, show data"""
    def __init__(self):
        self.connection = DBConnection.establish_connection()
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        """
        execute query by passing it to cursor method
        :param query: passed query
        :return:None
        """
        self.cursor.execute(query)
        self.connection.commit()

    def show_databases(self):
        """Shows all the databases"""
        self.cursor.execute('show databases')
        for database in self.cursor.fetchall():
            print(database)

    def show_tables(self):
        """Shows all the tables in particular database"""
        self.cursor.execute('show tables')
        for table in self.cursor.fetchall():
            print(table)

    def show_data(self,query):
        """
        Shows all the data for the query passed
        :param query: passed query
        :return: None
        """
        self.cursor.execute(query)
        for data in self.cursor.fetchall():
            print(data)


obj = DBOperations()

# CREATE NEW DATABASE
query = 'create database payroll_details'
obj.execute_query(query)
obj.show_databases()

# CREATE NEW TABLE
query = 'CREATE TABLE employee_payroll' \
      '(' \
      'id INT UNSIGNED NOT NULL AUTO_INCREMENT,' \
      'name VARCHAR(150) NOT NULL,' \
      'salary DOUBLE NOT NULL,' \
      'start DATE NOT NULL,' \
      'PRIMARY KEY (id))'
obj.execute_query(query)
obj.show_tables()

query = 'describe employee_payroll'
obj.describe_table(query)

# INSERT DATA IN TABLE
query = "INSERT INTO employee_payroll (name, salary, start) VALUES" \
        "('Bill',100000,'2010-01-03')," \
        "('Terisa',200000,'2019-11-13')," \
        "('Charlie',300000,'2020-05-20')"
obj.execute_query(query)

# RETRIEVE DATA FROM TABLE
obj.show_data('SELECT * FROM employee_payroll')
obj.show_data("SELECT salary FROM employee_payroll WHERE name='Bill'")

# UPDATING DATA IN EXISTING TABLE
# Adding new column
query = 'ALTER TABLE employee_payroll ADD gender CHAR(1) AFTER name'
obj.execute_query(query)

# UPDATING TABLE VALUES
query = "UPDATE employee_payroll SET gender='F' WHERE name='Terisa'"
obj.execute_query(query)

query = "UPDATE employee_payroll SET gender='M' WHERE name='Bill' OR name='Charlie'"
obj.execute_query(query)

query = "UPDATE employee_payroll SET salary=300000 WHERE name='Terisa'"
obj.execute_query(query)

# RETRIEVE DATA FROM TABLE
query = "SELECT AVG(salary) FROM employee_payroll WHERE gender='M' GROUP BY gender"
obj.show_data(query)

query = "SELECT gender, COUNT(name) FROM employee_payroll GROUP BY gender"
obj.show_data(query)

# DELETE DATA FROM TABLE
query = "DELETE FROM employee_payroll WHERE name = 'Zen'"
obj.execute_query(query)
obj.show_data('SELECT * FROM employee_payroll')

# INSERT DATA INTO TABLE
query = "INSERT INTO employee_payroll (name, salary, start) VALUES" \
        "('Zen',600000,'2010-05-03')"
obj.execute_query(query)
obj.show_data('SELECT * FROM employee_payroll')

# CREATING NEW TABLE EMPLOYEE_DETAILS
query = 'CREATE TABLE employee_details' \
      '(' \
      'id INT UNSIGNED NOT NULL ,' \
      'phone_no VARCHAR(15) NOT NULL,'\
      'address VARCHAR(200) NOT NULL,'\
      'FOREIGN KEY (id) REFERENCES employee_payroll (id))'
obj.execute_query(query)
obj.show_data('DESC employee_details')
obj.show_tables()

# INSERT DATA IN NEW TABLE EMPLOYEE_DETAILS
query = "INSERT INTO employee_details (id, phone_no, address) VALUES" \
        "(13,'8974512456','Delhi')," \
        "(15,'8745123658','Pune')," \
        "(24,'7458124586','Mumbai')"
obj.execute_query(query)
obj.show_data('SELECT * FROM employee_details')

# JOIN TWO TABLES
query = 'SELECT * FROM employee_payroll' \
      'INNER JOIN employee_details' \
      'ON employee_payroll.id = employee_details.id'
obj.show_data(query)

























