"""Data base for the banking system."""
import sqlite3
from dataclasses import dataclass

@dataclass
class DataBase:
    """Banking system database"""
    def __init__(self):
        self.connecting = sqlite3.connect('database.sqlite')
        self.cursor = self.connecting.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, number TEXT NOT NULL, pin TEXT, balance INTEGER DEFAULT 0 NOT NULL);')
        self.connecting.commit()
