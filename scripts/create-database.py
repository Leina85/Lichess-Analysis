import sqlite3
import chess.pgn

# connects to db or creates it if it doesnt exist
connect = sqlite3.connect("data/processed/lichess_data.db")

# creates cursor which can execute SQL
c = connect.cursor()

# deletes db if it already exists, then recreates it
c.execute("DROP TABLE IF EXISTS lichess_data")

# write table creation statement as multiline string to pass into execute method later to maintain readability
table_creation = """
CREATE TABLE lichess_data (
    gameID INTEGER PRIMARY KEY AUTOINCREMENT,
    winner TEXT,
    eco TEXT,
    opening TEXT,
    termination TEXT,
    moves INTEGER
)
"""
# create table
c.execute(table_creation)


with open("data/raw/decompressed_lichess_db_standard_rated_2015-05.pgn") as pgn:
    for i in range(5):
        game = chess.pgn.read_game(pgn)

        # winner field
        if game.headers["Result"] == "1-0": winner = "white"
        elif game.headers["Result"] == "0-1": winner = "black"
        elif game.headers["Result"] == "1/2-1/2": winner = "draw"
        else: winner = "unknown"

        # eco field
        eco = game.headers["ECO"]

        # opening field
        opening = game.headers["Opening"]

        # termination field
        termination = game.headers["Termination"]

        # moves field
        moves = len(list(game.mainline_moves()))

        c.execute("INSERT INTO lichess_data (winner, eco, opening, termination, moves) VALUES (?, ?, ?, ?, ?)", (winner, eco, opening, termination, moves))
        print(i)

connect.commit()
c.close()

print("done")