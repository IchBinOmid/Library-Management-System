import sqlite3
from datetime import date

def get_connection():
    connection = sqlite3.connect('library.db')
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            year INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS borrowings (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            book_id INTEGER,
            borrow_date TEXT,
            return_date TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (book_id) REFERENCES books(id)
        )
    """)

    connection.commit()
    connection.close()

def add_book(connection, book_title, book_author, book_year):
    # book_title = input('Enter The Title Of The Book : ')
    # book_author = input('Enter The Name Of The Author : ')

    # try:
    #     book_year = int(input('Enter The Year That The Book Has Been Published : '))

    # except ValueError:
    #     print('Enter A Valid Number.')
    #     return


    cursor = connection.cursor()
    

    cursor.execute(""" INSERT INTO books (title, author, year) VALUES (?, ?, ?) """,
                                        (book_title, book_author, book_year))
    connection.commit()

    print("Book added successfully!")

def edit_book(connection, book_id, new_title, new_author, new_year):

    # try:
    #     book_id = int(input('Enter Book ID : '))

    # except ValueError:
    #     print('Enter A Valid Number.')
    #     return

    # new_title = input('Enter The New Title : ')
    # new_author = input('Enter The New Author : ')

    # try:
    #     new_year = int(input('Enter The New Year : '))

    # except ValueError:
    #     print('Enter A Valid Number.')
    #     return


    cursor = connection.cursor()

    cursor.execute(""" UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?""",
                                        (new_title, new_author, new_year, book_id))
    connection.commit()

    print("Book updated successfully!")

def delete_book(connection, book_id):

    # try:
    #     book_id = int(input('Enter Book ID : '))

    # except ValueError:
    #     print('Enter A Valid Number.')
    #     return

    cursor = connection.cursor()

    cursor.execute(" DELETE FROM books WHERE id = ?", (book_id,))
    connection.commit()

    print("Book Deleted Successfully")

def list_books(connection):


    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()

    if not books:
        print('No Books Found.')
        return

    for book in books:
        print(
            f"ID : {book[0]} | "
            f"Title : {book[1]} | "
            f"Author : {book[2]} | "
            f"Year : {book[3]} | "
        )

def search_book(connection, keyword):

    # keyword = input('Enter The Title Of The Book To Search : ')

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books WHERE title LIKE ?', (f'%{keyword}%',))

    books = cursor.fetchall()

    if not books:
        print('No Books Found.')
        return

    for book in books:
        print(
            f"ID : {book[0]} | "
            f"Title : {book[1]} | "
            f"Author : {book[2]} | "
            f"Year : {book[3]} | "
        )




# cursor.execute(""" CREATE TABLE IF NOT EXISTS users (
#                         id INTEGER PRIMARY KEY,
#                         name TEXT,
#                         email TEXT
#                         )
#                 """)
# connection.commit()


def add_user(connection ,user_name, user_email):

    # user_name = input('Enter Your Name : ')
    # user_email = input('Enter Your Email : ')


    cursor = connection.cursor()

    cursor.execute(" INSERT INTO users (name, email) VALUES (?, ?) ", (user_name, user_email))
    connection.commit()

    print("User added successfully!")


def edit_user(connection, user_id, new_name, new_email):

    # try:
    #     user_id = int(input('Enter User ID : '))

    # except ValueError:
    #     print('Enter A Valid Number.')
    #     return

    # new_name = input('Enter The New Name : ')
    # new_email = input('Enter The New Email : ')

    cursor = connection.cursor()

    cursor.execute(""" UPDATE users SET name = ?, email = ? WHERE id = ?""",
                                        (new_name, new_email, user_id))
    connection.commit()

    print("User updated successfully!")

def delete_user(connection, user_id):

    # try:
    #     user_id = int(input('Enter User ID : '))

    # except ValueError:
    #     print('Enter A Valid Number.')
    #     return

    cursor = connection.cursor()

    cursor.execute(" DELETE FROM users WHERE id = ?", (user_id,))
    connection.commit()

    print("User Deleted Successfully")

def list_users(connection):

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if not users:
        print('No User Found.')
        return

    for user in users:
        print(
            f"ID : {user[0]} | "
            f"Name : {user[1]} | "
            f"Email : {user[2]} | "
        )

def search_user(connection, keyword):

    # keyword = input('Enter The Email Of The User To Search : ')

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE email LIKE ?', (f'%{keyword}%',))

    users = cursor.fetchall()

    if not users:
        print('No User Found.')
        return        

    for user in users:
        print(
            f"ID : {user[0]} | "
            f"Name : {user[1]} | "
            f"Email : {user[2]} | "
        )



# cursor.execute(""" CREATE TABLE IF NOT EXISTS borrowings  (
#                         id INTEGER PRIMARY KEY,
#                         user_id INTEGER,
#                         book_id INTEGER,
#                         borrow_date TEXT,
#                         return_date TEXT,
#                         FOREIGN KEY (user_id) REFERENCES users(id),
#                         FOREIGN KEY (book_id) REFERENCES books(id)
#                         )
#                 """)
# connection.commit()


def borrowing(connection, book_id, user_id):

    # try:
    #     book_id = int(input('Enter The ID Of The Book That You Want To Borrow : '))

    # except ValueError:
    #     print('Enter A Valid Number.')
    #     return

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    book = cursor.fetchone()

    if not book:
        print('Book Not Found.')
        return
    
    cursor.execute('SELECT * FROM borrowings WHERE book_id = ? AND return_date IS NULL', (book_id,))
    borrowing = cursor.fetchone()

    if borrowing:
        print('This Book Has Been Borrowed.')
        return

    # try:
    #     user_id = int(input('Enter The ID Of The User : '))

    # except ValueError:
    #     print('Enter A Valid Number.')
    #     return

    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()

    if not user:
        print('User Not Found.')
        return


    borrow_date = date.today()

    cursor.execute('''INSERT INTO borrowings (user_id, book_id, borrow_date)
                      VALUES (?, ?, ?)''', (user_id, book_id, borrow_date))
    
    connection.commit()
    print("Book Borrowed Successfully.")



ALLOWED_DAYS = 14
FINE_PER_DAY = 5000

def return_book(connection, book_id):

    # try:
    #     book_id = int(input('Enter The ID Of The Book : '))

    # except ValueError:
    #     print('Enter A Valid Number.')
    #     return

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM borrowings WHERE book_id = ? AND return_date IS NULL', (book_id,))

    borrowing = cursor.fetchone()

    if not borrowing:
        print('This Book Is Not Borrowed.')
        return


    return_date = date.today()

    cursor.execute('UPDATE borrowings SET return_date = ? WHERE id = ?', (return_date, borrowing[0]))
    connection.commit()

    print('Book Returned Successfully.')


    borrow_date = date.fromisoformat(borrowing[3])

    days = (return_date - borrow_date).days

    late_days = days - ALLOWED_DAYS

    if late_days > 0:
        fine = late_days * FINE_PER_DAY

    else:
        fine = 0

    print(f"Late Days: {late_days if late_days > 0 else 0}")
    print(f"Fine: {fine} Toman")


# connection.close()