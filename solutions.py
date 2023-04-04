"""
1. Set the variable test1 to the string &#39;This is a test of the emergency text system,&#39; and save test1 to a
file named test.txt.

ANSWER..

To set the variable test1 to the string 'This is a test of the emergency text system,' and save test1 to a file named test.txt:

test1 = 'This is a test of the emergency text system,'
with open('test.txt', 'w') as file:
    file.write(test1)


---------------------------------------------------------------------------------------------------


2. Read the contents of the file test.txt into the variable test2. Is there a difference between test 1
and test 2?

ANSWER..

To read the contents of the file test.txt into the variable test2 and check if there is any difference between test1 and test2:

with open('test.txt', 'r') as file:
    test2 = file.read()

print(test1 == test2)   # will print True


---------------------------------------------------------------------------------------------------


3. Create a CSV file called books.csv by using these lines:
title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992

ANSWER..

To create a CSV file called books.csv:

import csv

data = [    ['title', 'author', 'year'],
    ['The Weirdstone of Brisingamen', 'Alan Garner', 1960],
    ['Perdido Street Station', 'China Miéville', 2000],
    ['Thud!', 'Terry Pratchett', 2005],
    ['The Spellman Files', 'Lisa Lutz', 2007],
    ['Small Gods', 'Terry Pratchett', 1992]
]

with open('books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


---------------------------------------------------------------------------------------------------


4. Use the sqlite3 module to create a SQLite database called books.db, and a table called books with
these fields: title (text), author (text), and year (integer).

ANSWER..

To create a SQLite database called books.db using the sqlite3 module and a table called books with these fields:

import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE books
                  (title TEXT, author TEXT, year INTEGER)''')

conn.close()


---------------------------------------------------------------------------------------------------


5. Read books.csv and insert its data into the book table.

ANSWER..

To read books.csv and insert its data into the book table:

import csv
import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

with open('books.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header row
    for row in reader:
        cursor.execute('INSERT INTO books VALUES (?, ?, ?)', row)

conn.commit()
conn.close()


---------------------------------------------------------------------------------------------------


6. Select and print the title column from the book table in alphabetical order.

ANSWER..

To select and print the title column from the book table in alphabetical order:

import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('SELECT title FROM books ORDER BY title ASC')

for row in cursor:
    print(row[0])

conn.close()


---------------------------------------------------------------------------------------------------


7. From the book table, select and print all columns in the order of publication.

ANSWER..

To select and print all columns in the order of publication:

import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM books ORDER BY year ASC')

for row in cursor:
    print(row)

conn.close()

---------------------------------------------------------------------------------------------------


8. Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in
exercise 6.

ANSWER..

To use the sqlalchemy module to connect to the sqlite3 database books.db:

from sqlalchemy import create_engine

engine = create_engine('sqlite:///books.db')

---------------------------------------------------------------------------------------------------


9. Install the Redis server and the Python redis library (pip install redis) on your computer. Create a
Redis hash called test with the fields count (1) and name (&#39;Fester Bestertester&#39;). Print all the fields for
test.

ANSWER..

To create a Redis hash called test with the fields count (1) and name ('Fester Bestertester') and print all the fields for test:

import redis

r = redis.Redis()

r.hset('test', 'count', 1)
r.hset('test', 'name', 'Fester Bestertester')

print(r.hgetall('test'))

---------------------------------------------------------------------------------------------------


10. Increment the count field of test and print it.

ANSWER..

To increment the count field of test and print it:

import redis

r = redis.Redis()

r.hincrby('test', 'count', 1)
print(r.hget('test', 'count'))

---------------------------------------------------------------------------------------------------

"""