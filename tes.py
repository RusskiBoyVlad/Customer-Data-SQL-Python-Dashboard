import duckdb

# Connect to DuckDB. If the database does not exist, it will be created.
con = duckdb.connect(database='transaction.db', read_only=False)

select * from transactions t
where (select count(*) from transactions tr
where t.transaction_id = tr.transaction_id) > 1


# Verify the table was created by listing tables in the database
tables = con.execute("SELECT * FROM transactions LIMIT 3").fetchall()
print(tables)

# Close the connection
con.close()