import psycopg2

try:
    # Stripped down for Postgres.app Mac defaults
    connection = psycopg2.connect(
        dbname="postgres", user="srivastavaatharvaalok", host="localhost", port="5432"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    print("SUCCESS ->", cursor.fetchone())

    cursor.close()
    connection.close()

except Exception as error:
    print("SYSTEM ERROR ->", error)
