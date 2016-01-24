"""import sqlite3

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	print "1-AVG(),2-MAX(),3-MIN(),4-SUM(),5-EXIT"
	choice = raw_input("Enter the number of assignment.")

	while True:

		if choice == "1":
			c.execute("SELECT AVG(num) FROM numbers")
			
			raw = c.fetchall()

			for r in raw:
				print "AVG: " + str(r[0])
			break
		elif choice == "2":
			c.execute("SELECT MAX(num) FROM numbers")
			raw = c.fetchall()

			for r in raw:
				print "MAX: " + str(r[0])
			break
		elif choice == "3":
			c.execute("SELECT MIN(num) FROM numbers")
			raw = c.fetchall()

			for r in raw:
				print "MIN: " + str(r[0])
			break
		elif choice == "4":
			c.execute("SELECT SUM(num) FROM numbers")
			raw = c.fetchall()

			for r in raw:
				print "SUM: " + str(r[0])
			break
		else: 
			print "Exit"
			break

		"""

# Assignment 3b - prompt the user


# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("newnum.db")

# create a cursor object used to execute SQL commands
cursor = conn.cursor()

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

# loop until user enters a valid operation number [1-5]
while True:
    # get user input
    x = raw_input(prompt)

    # if user enters any choice from 1-4
    if x in set(["1", "2", "3", "4"]):
        # parse the corresponding operation text
        operation = {1: "avg", 2:"max", 3:"min", 4:"sum"}[int(x)]

        # retrieve data
        cursor.execute("SELECT {}(num) from numbers".format(operation))

        # fetchone() retrieves one record from the query
        get = cursor.fetchone()

        # just for better output
        output = {"avg": "Average", "max": "Maximum", "min": "Minimum", "sum": "Sum"}

        # output result to screen
        print
        print output[operation] + ":  %f" % get[0]
        print

    # if user enters 5
    elif x == "5":
        print "Exit"

        # exit loop
        break

