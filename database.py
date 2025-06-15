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

#Creating the table for customer accounts
con,cur = openDb()
cur.execute("""CREATE TABLE IF NOT EXISTS customerAccounts(
            customerID INTEGER PRIMARY KEY,
            surname TEXT NOT NULL,
            forename TEXT NOT NULL,
            emailAddress STRING NOT NULL,
            password STRING NOT NULL)""")
closeDb()

#Creating all the functions for customer accounts
def addCustomer(surname,forename,email,password):
    con,cur = openDb()
    cur.execute("""INSERT INTO customerAccounts(surname,forename,emailAddress,password)
                VALUES (?,?,?,?)""", (surname,forename,email,password))
    con.commit()
    closeDb()

def removeCustomer(pkey):
    con,cur = openDb()
    cur.execute("DELETE FROM customerAccounts WHERE customerID = ?",
                (pkey,))
    con.commit()
    closeDb()

def updateCustomer(pkey, **kwargs):
    con,cur = openDb()
    for kwarg in kwargs:
        cur.execute(f"UPDATE customerAccounts SET {kwarg} = ? WHERE customerID =?",
                    (kwargs[kwarg],pkey))
        con.commit()
    closeDb()

def getAllCustomers():
    con,cur = openDb()
    cur.execute("SELECT * FROM customerAccounts")
    allCustomers = cur.fetchall()
    closeDb()
    return allCustomers

if __name__ == "__main__":
    print(getAllCustomers())
    addCustomer("testSurname","testName","test@gmail.com","Password123")
    addCustomer("testSurname2","TestFirstname","anotherTest@gmail.com","PasswordTesting1")
    print(getAllCustomers())
    updateCustomer(2,password = "NewPassword")
    print(getAllCustomers())
    removeCustomer(1)
    removeCustomer(2)
    print(getAllCustomers())