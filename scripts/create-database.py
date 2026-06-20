import sqlite3

# connects to db or creates it if it doesnt exist
connect = sqlite3.connect("data/processed/lichess_data.db")

# creates cursor which can execute SQL
c = connect.cursor()