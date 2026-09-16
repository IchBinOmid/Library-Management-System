# Library Management System

A Python-based library management system built with **Python, Object-Oriented Programming (OOP), and SQLite**.

> 🚧 **Project Status: In Development**
>
> This project is currently under active development. More features and improvements will be added as development continues.

## 📌 About The Project

The Library Management System is a command-line application designed to manage books, users, and borrowing records in a library.

The main purpose of this project is to practice and demonstrate Python programming, object-oriented programming, database management with SQLite, exception handling, and software testing through a practical project.

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

### 🗄️ Database

The project uses **SQLite** for data storage.

Current database tables:

* `books`
* `users`
* `borrowings`

### 🧪 Testing

The project includes automated tests using Python's built-in `unittest` framework.

The tests currently cover the implemented Book Management and User Management features.

Tests use an in-memory SQLite database (`:memory:`) to keep the test environment separate from the project's main database.

## 🛠️ Technologies & Skills

* Python
* Object-Oriented Programming (OOP)
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

## 🚧 Planned Features

The following features are planned for the next development stages:

* Borrowing Management

  * Borrow books
  * Prevent borrowing an already borrowed book
  * Return books
  * Track borrowing and return dates

* Late Fee Calculation

* Improved Error Handling

* Additional Testing

* Final documentation and project improvements

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
* [ ] Borrowing Management
* [ ] Late Fee Calculation
* [ ] Error Handling & Additional Testing
* [ ] Final Documentation

---

**Author:** Omid Norouznezhad

**Project:** Library Management System

**Status:** 🚧 In Development
