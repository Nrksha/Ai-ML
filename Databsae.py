import sqlite3

# Connect to the database
conn = sqlite3.connect('Librarian.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Librarian")

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Librarian (
        librarian_id TEXT PRIMARY KEY,
        name TEXT,
        class TEXT,
        year int
    )
''')

# Commit changes
conn.commit()

# Insert data
cursor.execute('''
    INSERT INTO Librarian (librarian_id, name,class,year)
    VALUES ('LIB001', 'Sam','3rd sem',2)
''')

# Commit changes
conn.commit()

# Retrieve data
cursor.execute("SELECT * FROM Librarian")
print(cursor.fetchall())

# Close connection
conn.close()




