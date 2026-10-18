import psycopg2

try:
    connection = psycopg2.connect(
        dbname="gtm_engine", user="srivastavaatharvaalok", host="localhost", port="5432"
    )
    cursor = connection.cursor()

    # Querying the database to prove data persistence
    cursor.execute(
        "SELECT lead_id, company_name, intent_score, outreach_status FROM outbound_prospects;"
    )
    records = cursor.fetchall()

    print("--- LIVE BDE PIPELINE DATA ---")
    for row in records:
        print(
            f"Lead ID: {row[0]} | Company: {row[1]} | Intent: {row[2]} | Status: {row[3]}"
        )

    cursor.close()
    connection.close()

except Exception as error:
    print("READ FAILED ->", error)
