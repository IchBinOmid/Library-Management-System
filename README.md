# Library Management System

A Python-based Library Management System built with **Python and SQLite**.

> 🚧 **Project Status: In Development**
>
> This project is currently under active development. New features, tests, error handling, and documentation improvements are being added progressively.

## 📌 About The Project

The Library Management System is a command-line application designed to manage books, users, and borrowing records.

The project is being developed as a practical Python portfolio project to strengthen skills in:

* Python programming
* SQL and SQLite
* Database design
* Software testing
* Exception handling
* Git and GitHub

## ✨ Current Features

### 📚 Book Management

* Add books
* Edit book information
* Delete books
* List all books
* Search for books

### 👤 User Management

* Add users
* Edit user information
* Delete users
* List all users
* Search for users

### 📖 Borrowing Management

* Borrow books
* Prevent borrowing an already borrowed book
* Check whether a book exists before borrowing
* Check whether a user exists before borrowing
* Return books
* Track borrowing and return dates

### 💰 Late Fee Calculation

* Calculate overdue days
* Calculate late fees based on the number of overdue days
* Configurable allowed borrowing period
* Configurable fine per late day

### 🗄️ Database

The project uses **SQLite** for data storage.

Current database tables:

* `books`
* `users`
* `borrowings`

The `borrowings` table uses foreign keys to connect users and books with borrowing records.

## 🧪 Testing

The project uses Python's built-in **unittest** framework.

Current automated tests cover:

* Book Management
* User Management

Tests use an in-memory SQLite database (`:memory:`) to keep the test environment isolated from the main database.

Additional tests for Borrowing, Returning, and Late Fee Calculation are planned.

## 🛠️ Technologies & Skills

* Python
* SQLite
* SQL
* `sqlite3`
* `unittest`
* Git & GitHub

## 🗂️ Project Structure

```text
Library-Management-System/
│
├── main.py
├── test_main.py
├── README.md
└── .gitignore
```

> Database files such as `library.db` and test database files are excluded from Git using `.gitignore`.

## ▶️ How To Run

### 1. Clone the repository

```bash
git clone https://github.com/IchBinOmid/Library-Management-System.git
```

### 2. Open the project directory

```bash
cd Library-Management-System
```

### 3. Run the application

```bash
python main.py
```

### 4. Run the tests

```bash
python -m unittest test_main.py
```

## 📊 Database Schema

### `books`

| Column   | Type    | Description      |
| -------- | ------- | ---------------- |
| `id`     | INTEGER | Primary Key      |
| `title`  | TEXT    | Book title       |
| `author` | TEXT    | Book author      |
| `year`   | INTEGER | Publication year |

### `users`

| Column  | Type    | Description |
| ------- | ------- | ----------- |
| `id`    | INTEGER | Primary Key |
| `name`  | TEXT    | User name   |
| `email` | TEXT    | User email  |

### `borrowings`

| Column        | Type    | Description    |
| ------------- | ------- | -------------- |
| `id`          | INTEGER | Primary Key    |
| `user_id`     | INTEGER | User reference |
| `book_id`     | INTEGER | Book reference |
| `borrow_date` | TEXT    | Borrowing date |
| `return_date` | TEXT    | Return date    |

## 📈 Development Progress

* [x] Database Design
* [x] Book Management
* [x] User Management
* [x] Borrowing Management
* [x] Book Return
* [x] Late Fee Calculation
* [ ] Borrowing & Return Tests
* [ ] Improved Error Handling
* [ ] Final Documentation

---

**Author:** Omid Norouznezhad

**Project:** Library Management System

**Status:** 🚧 In Development
