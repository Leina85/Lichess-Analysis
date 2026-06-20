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
    gameID TEXT PRIMARY KEY,
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
        while game == True:
            game = chess.pgn.read_game(pgn)

            # gameID field
            gameID = "game" + str(i)

            # winner field
            if game.Round() == "1-0": winner = "white"
            elif game.Round() == "0-1": winner = "black"
            elif game.Round() == "1/2-1/2": winner = "draw"
            else:
                game = False
                break

            # eco field
            eco = game.ECO()

            # opening field
            opening = game.Opening()

            # termination field
            termination = game.Termination()

            # moves field
            moves = game.end().board().fullmove_number

            c.execute("INSERT INTO lichess_data VALUES (?, ?, ?, ?, ?, ?)", (gameID, winner, eco, opening, termination, moves))

c.close()