import sqlite3

def initDB():
    DB = "Meteo.db"
    connection = sqlite3.Connection(DB)
    return connection