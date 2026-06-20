import sqlite3

# connects to db or creates it if it doesnt exist
connect = sqlite3.connect("data/processed/lichess_data.db")

# creates cursor which can execute SQL
c = connect.cursor()

# deletes db if it already exists, then recreates it
c.execute("DROP TABLE IF EXISTS lichess_data")

# write table creation statement as multiline string to pass into execute method later to maintain readability
table_creation = """
CREATE TABLE lichess_data (
    gameID TEXT PRIMARY KEY,
    winner TEXT,
    eco TEXT,
    opening TEXT,
    termination TEXT,
    moves INTEGER,
    duration REAL
)
"""

c.execute(table_creation)

c.close()