import sqlite3

con = sqlite3.connect("test_db.db")

cursor_obj = con.cursor()

cursor_obj.execute("CREATE TABLE if not exists cool_peeps(id integer PRIMARY KEY, name text, age integer)")

con.commit()

cursor_obj.execute("INSERT INTO cool_peeps(name, age) VALUES('Matt', 27)")

cursor_obj.execute("INSERT INTO cool_peeps(name, age) VALUES('Marty', 34)")

# cursor_obj.execute("SELECT * FROM cool_peeps")

# [print(row) for row in cursor_obj.fetchall()]

cursor_obj.execute("CREATE TABLE if not exists other_cool_peeps(id INTEGER PRIMARY KEY, name text, age integer)")

# cursor_obj.execute("SELECT name from sqlite_master where type='table'")

# [print(row) for row in cursor_obj.fetchall()]

cursor_obj.execute("DROP table if exists other_cool_peeps")

# cursor_obj.execute("SELECT name from sqlite_master where type='table'")

# [print(row) for row in cursor_obj.fetchall()]

data = [("Jon", 27), ("Nic", 28), ("Raye", 29), ("Alex", 27), ("Kate", 29)]

cursor_obj.executemany("INSERT INTO cool_peeps(name, age) VALUES (?, ?)", data)

cursor_obj.execute("SELECT * from cool_peeps")

[print(row) for row in cursor_obj.fetchall()]

cursor_obj.execute("DROP table if exists cool_peeps")

con.commit()