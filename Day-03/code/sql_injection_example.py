Python

import sqlite3

# Example of a vulnerable SQL query
def vulnerable_query(user_input):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

# Example usage
user_input = "'; DROP TABLE users; --"
print(vulnerable_query(user_input))
