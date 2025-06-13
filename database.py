import sqlite3 as sq

#Creating a way to connect to and disconnect from the database
def openDb():
    con = sq.connect("restaurant.db")
    cur = con.cursor()
    return con, cur

def closeDb():
    con.close()

#Creating the table for staff accounts
con,cur = openDb()
cur.execute("""CREATE TABLE IF NOT EXISTS staffAccounts(
            staffID INTEGER PRIMARY KEY,
            surname TEXT NOT NULL,
            forename TEXT NOT NULL,
            jobRole TEXT NOT NULL,
            emailAddress STRING NOT NULL,
            password STRING NOT NULL)""")
con.commit()
closeDb()

#Creating all the functions for the staff table
def addStaff(surname,forename,role,email,password):
    con,cur = openDb()
    cur.execute("""INSERT INTO staffAccounts(surname,forename,jobRole,emailAddress,password) 
                VALUES (?,?,?,?,?)""", (surname,forename,role,email,password))
    con.commit()
    closeDb()

if __name__ == "__main__":
    pass