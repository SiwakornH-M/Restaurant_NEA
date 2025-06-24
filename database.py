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

#Creating the menu table and all associated functions
con,cur = openDb()
cur.execute("""CREATE TABLE IF NOT EXISTS menu( 
            dishID INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            ingredients TEXT NOT NULL,
            allergens TEXT NOT NULL,
            price FLOAT NOT NULL)""")
closeDb()

#Creating the functions for the menu table 
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

#Creating the table for orders
con,cur = openDb()
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
            orderID INTEGER PRIMARY KEY,
            account TEXT,
            details TEXT NOT NULL, 
            cost FLOAT NOT NULL)""") #details is what dishes are in the order
closeDb()

def addOrder(account,dishes):
    con,cur = openDb()
    dishes = dishes.split("|")
    totalCost = 0
    tempList = []
    #Finds the total cost of everything in the order
    for dish in dishes:
        #Retrieves price of each item from database
        cur.execute("SELECT price FROM menu WHERE name = ?",
                    (dish,))
        price = cur.fetchone()
        for num in price:
            cost = float(num)
        totalCost += cost #adds the price to the total
        #Retrieves the primary key of each item
        cur.execute("SELECT dishID FROM menu WHERE name = ?",
                    (dish,))
        id = cur.fetchmany()
        #Adds the primary key of each dish to a list
        for tuple in id:
            for pkey in tuple:
                tempList.append(pkey)
                tempList.append("|")
    #Checks to see if the last item in the list is "|"
    if tempList[-1] == "|":
        tempList.pop()
    details = ""
    #Adds every dishes primary key to details
    for char in tempList:
        details += char
    cur.execute("INSERT INTO orders(account,details,cost) VALUES (?,?,?)",
                (account,details,totalCost))
    con.commit()
    closeDb()
    
def removeOrder(pkey):
    con,cur = openDb()
    cur.execute("DELETE FROM orders WHERE orderID = ?",
                (pkey,))
    con.commit()
    closeDb()

def updateOrder(pkey,**kwargs):
    con,cur = openDb()
    for kwarg in kwargs:
        cur.execute(f"UPDATE orders SET {kwarg} = ? WHERE orderID = ?",
                    (kwargs[kwarg],pkey))
        con.commit()
    closeDb()

def allOrders():
    con,cur = openDb()
    cur.execute("SELECT * FROM orders")
    orders = cur.fetchall()
    closeDb()
    return orders

def getOrder(pkey):
    con,cur = openDb()
    cur.execute("SELECT * FROM orders WHERE orderID = ?",
                (pkey,))
    order = cur.fetchall()
    closeDb()
    return order

if __name__ == "__main__":
    print(allOrders())
    print(getMenu())
    addDish("egg rolls","eggs","eggs",4.99)
    addDish("pork belly","pork","none",9.99)
    print(getMenu())
    addOrder(None,"egg rolls")
    addOrder(None,"egg rolls|pork belly")
    print(allOrders())
    print(getOrder(1))
    removeOrder(1)
    removeOrder(2)
    removeDish(1)
    removeDish(2)
    print(getMenu())
    print(allOrders())