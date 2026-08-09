import sqlite3
import pandas as pd

conn = sqlite3.connect("database/hospital.db")

query = "SELECT * FROM patients LIMIT 5"

df = pd.read_sql(query, conn)

print(df)

conn.close()