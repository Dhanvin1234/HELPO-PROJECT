import sqlite3

connection=sqlite3.connect("helpo.db")
crsr=connection.cursor()
#crsr.execute( """CREATE TABLE details (
  #  name text,
   # email varchar(255) PRIMARY KEY,
    #password varchar(255))""")


#connection.commit()
#connection.close()
def pdetails():
    connection=sqlite3.connect("helpo.db")
    crsr = connection.cursor()
    crsr.execute("INSERT INTO details VALUES (:name, :email, :password)")
connection.commit()