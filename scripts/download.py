#download lichess data
from urllib.request import urlretrieve
import zstandard as zstd

url = "https://database.lichess.org/standard/lichess_db_standard_rated_2026-05.pgn.zst"
urlretrieve(url, "data/raw/lichess_db_standard_rated_2026-05.pgn.zst")

with open("data/raw/lichess_db_standard_rated_2026-05.pgn.zst", "rb") as compressed_file:
    dctx = zstd.ZstdDecompressor()
    with open("data/raw/lichess_db_standard_rated_2026-0598765.pgn", "wb") as decompressed_file:
        dctx.copy_stream(compressed_file, decompressed_file)