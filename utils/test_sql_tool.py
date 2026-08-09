from sql_tool import execute_sql

query = 'SELECT * FROM patients LIMIT 5'

results = execute_sql(query)

print(results)