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

def removeStaff(pkey):
    con,cur = openDb()
    cur.execute("DELETE FROM staffAccounts WHERE staffID = ?",
                (pkey,))
    con.commit()
    closeDb()

def updateStaff(pkey, **kwargs):
    con,cur = openDb()
    for kwarg in kwargs:
        cur.execute(f"UPDATE staffAccounts SET {kwarg} = ? WHERE staffID = ?",
                    (kwargs[kwarg], pkey))
        con.commit()
    closeDb()

def getAllStaff():
    con,cur = openDb()
    cur.execute("SELECT * FROM staffAccounts")
    allStaff = cur.fetchall()
    closeDb()
    return allStaff

if __name__ == "__main__":
    print(getAllStaff())
    addStaff("Hackett-Mingsong","Siwakorn","Waiter/Bar Staff","testemail1@gmail.com","Password1")
    addStaff("Hackett-Mingsong","Natawood","Kitchen Porter","testemail2@gmail.com","Password2")
    print(getAllStaff())
    updateStaff(2,jobRole = "Kitchen Assistant")
    print(getAllStaff())
    removeStaff(1)
    removeStaff(2)
    print(getAllStaff())