import sqlite3
import unittest
from main import (add_book,
                   delete_book,
                     edit_book,
                       list_books,
                         search_book,
                           add_user,
                             edit_user,
                               delete_user,
                                list_users,
                                  search_user, )
from unittest.mock import patch



class TestBooks(unittest.TestCase):

    def test_add_book(self):

        connection = sqlite3.connect(":memory:")
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                ID INTEGER PRIMARY KEY,
                                title TEXT,
                                author TEXT,
                                year INTEGER
                            )
                        ''')
        connection.commit()

        add_book(connection, 'Python', 'Mark', 2026)

        cursor.execute(
            "SELECT * FROM books WHERE title = ?",
            ("Python",)
        )

        book = cursor.fetchone()

        self.assertIsNotNone(book)

        connection.close()


    def test_delete_book(self):
        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()

        cursor.execute(""" CREATE TABLE IF NOT EXISTS books (
                            ID INTEGER PRIMARY KEY,
                            title TEXT,
                            author TEXT,
                            year INTEGER
                        )
                    """)
        connection.commit()

        cursor.execute(""" INSERT INTO books (title, author, year) VALUES (?, ?, ?) """, 
                                            ('Python', 'Mark', 2026))
        
        connection.commit()

        book_id = cursor.lastrowid

        delete_book(connection, book_id)

        cursor.execute(""" SELECT * FROM books WHERE id = ? """, (book_id,))
        connection.commit()

        book = cursor.fetchone()

        self.assertIsNone(book)

        connection.close()


    def test_edit_book(self):

        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()

        cursor.execute(""" CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY,
                            title TEXT,
                            author TEXT,
                            year INTEGER
                        )
                """)

        cursor.execute(''' INSERT INTO books (title, author, year) VALUES (?, ?, ?) ''', ('Python', 'Mark', 2024))
        connection.commit()

        book_id = cursor.lastrowid

        edit_book(connection, book_id,'Django', 'William', 2026)

        cursor.execute(''' SELECT * FROM books WHERE id = ? ''', (book_id,))

        book = cursor.fetchone()

        self.assertEqual(book[1], 'Django')
        self.assertEqual(book[2], 'William')
        self.assertEqual(book[3], 2026)

        connection.close()


    def test_list_books(self):

        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                id INTEGER PRIMARY KEY,
                                title TEXT,
                                author TEXT,
                                year INTEGER
                            )
                    ''')

        cursor.execute(''' INSERT INTO books (title, author, year) VALUES(?, ?, ?)''', ('Python', 'Mark', 2024))
        connection.commit()

        with patch("builtins.print") as mock_print:
            list_books(connection)

        self.assertTrue(mock_print.called)

        printed_text = str(mock_print.call_args)

        self.assertIn('Python', printed_text)
        self.assertIn('Mark', printed_text)
        self.assertIn('2024', printed_text)

        connection.close()


    def test_search_book(self):
        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()

        cursor.execute(''' CREATE TABLE IF NOT EXISTS books(
                                    id INTEGER PRIMARY KEY,
                                    title TEXT,
                                    author TEXT,
                                    year INTEGER
                            )
                    ''')

        cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', ('Python', 'Mark', 2024))
        cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', ("Django", "William", 2025))

        connection.commit()

        with patch('builtins.print') as mock_print:
            search_book(connection, "Python")

            self.assertTrue(mock_print.called)

            printed_text = str(mock_print.call_args)

            self.assertIn("Python", printed_text)
            self.assertIn('Mark', printed_text)
            self.assertIn('2024', printed_text)

            connection.close()


class TestUsers(unittest.TestCase):

    def test_add_user(self):

        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            email TEXT
                        )
                ''')

        add_user(connection, 'Omid', 'Omid@gmail.com')

        cursor.execute('SELECT * FROM users WHERE email = ?', ('Omid@gmail.com',))

        user = cursor.fetchone()
        self.assertIsNotNone(user)

        connection.close()

    def test_edit_user(self):

        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            email TEXT
                        )
                ''')

        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Omid', 'Omid@gmail.com'))
        connection.commit()

        user_id = cursor.lastrowid

        edit_user(connection, user_id, 'Amir', 'Amir@gmail.com')

        cursor.execute('SELECT * FROM users WHERE email = ?', ('Amir@gmail.com',))

        user = cursor.fetchone()

        self.assertEqual(user[1], 'Amir')
        self.assertEqual(user[2], 'Amir@gmail.com')

        connection.close()

    def test_delete_user(self):
        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            email TEXT
                        )
                ''')

        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Omid', 'Omid@gmail.com'))
        connection.commit()

        user_id = cursor.lastrowid

        delete_user(connection, user_id)

        cursor.execute('SELECT * FROM users WHERE email = ?', ('Omid@gmail.com',))

        user = cursor.fetchone()

        self.assertIsNone(user)

        connection.close()

    def test_list_users(self):

        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            email TEXT
                        )
                ''')

        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Omid', 'Omid@gmail.com'))
        connection.commit()

        with patch('builtins.print') as mock_print:
            list_users(connection)

        self.assertTrue(mock_print.called)
        printed_text = str(mock_print.call_args)

        self.assertIn('Omid', printed_text)
        self.assertIn('Omid@gmail.com', printed_text)

        connection.close()


    def test_search_user(self):

        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            email TEXT
                        )
                ''')

        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Omid', 'Omid@gmail.com'))
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Amir', 'Amir@gmail.com'))
        connection.commit()

        with patch('builtins.print') as mock_print:
            search_user(connection, 'Omid')

        self.assertTrue(mock_print.called)

        printed_text = str(mock_print.call_args)

        self.assertIn('Omid', printed_text)
        self.assertIn('Omid@gmail.com', printed_text)

        connection.close()
        


            

if __name__ == '__main__':
    unittest.main() 