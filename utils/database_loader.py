import pandas as pd
import sqlite3

# Read the CSV
df = pd.read_csv("data/healthcare_dataset.csv")

# Create SQLite database
conn = sqlite3.connect("database/hospital.db")

# Store CSV as a table named 'patients'
df.to_sql("patients", conn, if_exists="replace", index=False)

# Close connection
conn.close()

print("Database created successfully!")