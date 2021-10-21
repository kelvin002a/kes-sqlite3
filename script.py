import sqlite3


connection = sqlite3.connect("test.db")

Cursor = connection.cursor()

table1 = """CREATE TABLE IF NOT EXISTS
Movies(movie_name TEXT,Actor_name Text ,actress_name TEXT ,Director_Name TEXT ,Year_of_release INTEGER); """

Cursor.execute(table1)


Cursor.execute("INSERT INTO Movies VALUES ('PIE','Arun','Bony','Cathy',2001)")
Cursor.execute("INSERT INTO Movies VALUES ('PEL','Anto','Benson','Catherin',2001)")

Cursor.execute("SELECT * FROM Movies")

Cursor.execute("SELECT * FROM Movies WHERE actor_name='Anto' ")

result = Cursor.fetchall()
print(result)