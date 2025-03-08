import sqlite3

# Create a database file
connection = sqlite3.connect('PersonalLibrary.db')
cursor = connection.cursor()

print("Database created successfully!")

# Create the Books table with a UNIQUE constraint
create_table_query = '''
CREATE TABLE IF NOT EXISTS Books (
  BookID INTEGER PRIMARY KEY AUTOINCREMENT,
  Title TEXT NOT NULL,
  Author TEXT NOT NULL,
  YearPublished INTEGER NOT NULL,
  Genre TEXT NOT NULL,
  UNIQUE (Title, Author, YearPublished, Genre) -- Add this constraint to prevent duplicates
);
'''
cursor.execute(create_table_query)
connection.commit()
print("Table created successfully!")

# Books to insert
books = [
  ("Fiqir Eske Meqabir", "Haddis Alemayehu", 1968, "Tragedy, Fiction"),
  ("Cutting for Stone", "Abraham Verghese", 2009, "Historical Fiction"),
  ("Beneath the Lion's Gaze", "Maaza Mengiste", 2010, "Historical Fiction"),
  ("The Beautiful Things That Heaven Bears", "Dinaw Mengestu", 2007, "Fiction, Contemporary"),
  ("Oromay", "Baalu Girma", 1983, "Historical Fiction, Political Thriller")
]

# Insert books while ignoring duplicates
insert_query = '''INSERT OR IGNORE INTO Books (Title, Author, YearPublished, Genre)
VALUES (?, ?, ?, ?);
'''

cursor.executemany(insert_query, books)  # This will skip duplicates due to "INSERT OR IGNORE"
connection.commit()
print("Books inserted successfully without duplicates!")

# List all books
retrieve_all_query = "SELECT * FROM Books;"
cursor.execute(retrieve_all_query)
all_books = cursor.fetchall()
print("All Books:", all_books)

# Find books published after the year 2000
books_after_2000_query = "SELECT * FROM Books WHERE YearPublished > 2000;"
cursor.execute(books_after_2000_query)
recent_books = cursor.fetchall()
print("Books published after 2000:", recent_books)

# Find all books in the "Fiction" genre
fiction_books_query = "SELECT * FROM Books WHERE Genre LIKE '%Fiction%';"  # Adjusted for partial matches
cursor.execute(fiction_books_query)
fiction_books = cursor.fetchall()
print("Fiction Books:", fiction_books)

# Update the YearPublished for one book
update_year_query = '''UPDATE Books
SET YearPublished = 2025
WHERE Title = 'Oromay';'''
cursor.execute(update_year_query)
connection.commit()
print("Book's YearPublished updated successfully!")

# Delete a book
delete_book_query = """
DELETE FROM Books
WHERE Title = 'Pride and Prejudice';
"""  # Ensure "Pride and Prejudice" exists before running this
cursor.execute(delete_book_query)
connection.commit()
print("Book deleted successfully!")

# Remove duplicate records (if duplicates somehow exist)
delete_duplicates_query = """
DELETE FROM Books
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM Books
    GROUP BY Title, Author, YearPublished, Genre
);
"""
cursor.execute(delete_duplicates_query)
connection.commit()
print("Duplicate records removed (if any existed)!")

# Fetch the final list of books
retrieve_all_query = "SELECT * FROM Books;"
cursor.execute(retrieve_all_query)
all_books = cursor.fetchall()
print("All Books after cleanup:", all_books)

# Close the connection
cursor.close()
connection.close()
print("Connection closed!")

