from urllib.request import urlretrieve
import zstandard as zstd

def download_lichess_data(url):

    # download lichess data from url
    urlretrieve(url, "data/raw/lichess_db_standard_rated_2015-05.pgn.zst")

    # opens compressed file as read
    with open("data/raw/lichess_db_standard_rated_2015-05.pgn.zst", "rb") as compressed_file:
        dctx = zstd.ZstdDecompressor()

        # opens file to write decompressed data to
        with open("data/raw/decompressed_lichess_db_standard_rated_2015-05.pgn", "wb") as decompressed_file:
            dctx.copy_stream(compressed_file, decompressed_file)

url = "https://database.lichess.org/standard/lichess_db_standard_rated_2015-05.pgn.zst"
download_lichess_data(url)