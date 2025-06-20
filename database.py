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

def getStaff(pkey):
    con,cur = openDb()
    cur.execute("SELECT * FROM staffAccounts WHERE staffID = ?",
                (pkey,))
    staff = cur.fetchall()
    closeDb()
    return staff

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

def getCustomer(pkey):
    con,cur = openDb()
    cur.execute("SELECT * FROM customerAccounts WHERE customerID = ?",
                (pkey,))
    customer = cur.fetchall()
    closeDb()
    return customer

con,cur = openDb()
cur.execute("""CREATE TABLE IF NOT EXISTS menu(" 
            dishID INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            ingredients TEXT NOT NULL,
            allergens TEXT NOT NULL,
            price FLOAT NOT NULL)""")
closeDb()

def addDish(name,ingredients,allergens,price):
    con,cur = openDb()
    cur.execute("""INSERT INTO menu(name, ingredients,allergens,price)
                VALUES (?,?,?,?)""", (name,ingredients,allergens,price))
    con.commit()
    closeDb()

def removeDish(pkey):
    con,cur = openDb()
    cur.execute("DELETE FROM menu WHERE dishID = ?",
                (pkey,))
    con.commit()
    closeDb()

def updateDish(pkey, **kwargs):
    con,cur = openDb()
    for kwarg in kwargs:
        cur.execute(f"UPDATE menu SET {kwarg} = ? WHERE dishID = ?",
                    (kwargs[kwarg],pkey))
        con.commit()
        closeDb()

def getMenu():
    con,cur = openDb()
    cur.execute("SELECT * FROM menu")
    menu = cur.fetchall()
    closeDb()
    return menu

def getDish(pkey):
    con,cur = openDb()
    cur.execute("SELECT * FROM menu WHERE dishID = ?",
                (pkey,))
    dish = cur.fetchall()
    closeDb()
    return dish

if __name__ == "__main__":
    print(getAllCustomers())
    print(getAllStaff())
    addStaff("test1","testFirstname1","TestRole1","Test1@testmail.com","Password1")
    addStaff("test2","testFirstname2","TestRole2","Test2@testmail.com","Password2")
    addCustomer("test3","testFirstname3","Test3@testmail.com","Password3")
    addCustomer("test4","testFirstname4","Test4@testmail.com","Password4")
    print(getCustomer(2))
    print(getStaff(1))
    removeCustomer(1)
    removeCustomer(2)
    removeStaff(1)
    removeStaff(2)
    print(getAllCustomers())
    print(getAllStaff())
