import sqlite3

# Create and return a SQLite database connection
def get_connection(db_path):
    # Connect to the SQLite database at the given path
    conn = sqlite3.connect(db_path)

    # Enable foreign key constraint enforcement
    conn.execute("PRAGMA foreign_keys = ON;")

    return conn
