import sqlite3

db_connection = sqlite3.connect("db/movie.sqlite3") ## Establish a connection
db_cursor = db_connection.cursor() ## Enables you to inject data/ intaract with the db
