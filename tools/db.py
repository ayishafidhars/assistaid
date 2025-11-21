import sqlite3
import os

DB_PATH = "assistaid.db"

class IncidentDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            raw_text TEXT,
            cleaned_text TEXT,
            incident_type TEXT,
            assigned_team TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_incident(self, raw_text, cleaned_text, incident_type, assigned_team):
        query = """
        INSERT INTO incidents (raw_text, cleaned_text, incident_type, assigned_team)
        VALUES (?, ?, ?, ?);
        """
        self.conn.execute(query, (raw_text, cleaned_text, incident_type, assigned_team))
        self.conn.commit()

    def list_incidents(self):
        cursor = self.conn.execute("SELECT * FROM incidents ORDER BY id DESC;")
        return cursor.fetchall()
