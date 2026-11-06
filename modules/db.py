import sqlite3
from sqlite3 import Error

class DB():
	def __init__(self, db_file):
		self.connection = None
		self.create_connection(db_file)
		self.create_table(""" CREATE TABLE IF NOT EXISTS transactions (
                              id integer PRIMARY KEY,
                              hash text,
                              amount integer,
                              timestamp integer
										
                         ); """)
		
		self.transactions = []

	def create_connection(self, db_file):
		""" create a database connection to a SQLite database """
		try:
			self.connection = sqlite3.connect(db_file)
			print("INFO: Database connected")
		except Error as e:
			print(e)
			
	def AddTransaction(self, transaction):
		cur = self.connection.cursor()
		cur.execute(''' INSERT INTO transactions(hash,amount,timestamp)
				  VALUES(?,?,?) ''', transaction)
		self.connection.commit()
		return cur.lastrowid
	
	def create_table(self, create_table_sql):
		try:
			c = self.connection.cursor()
			c.execute(create_table_sql)
		except Error as e:
			print(e)
	
	def disconnect(self):
		self.connection.close()
