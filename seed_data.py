import psycopg2

try:
    # Connecting to your newly created GTM database
    connection = psycopg2.connect(
        dbname="gtm_engine", user="srivastavaatharvaalok", host="localhost", port="5432"
    )
    connection.autocommit = True
    cursor = connection.cursor()

    # Injecting real-world BDE mock data
    insert_query = """
    INSERT INTO outbound_prospects (company_name, decision_maker, intent_score, outreach_status)
    VALUES 
    ('TechNova India', 'Rahul Sharma', 85, 'Pending'),
    ('DataFlow Systems', 'Priya Patel', 92, 'Drafted AI Copy'),
    ('Apex Logistics', 'Amit Singh', 40, 'Cold');
    """

    cursor.execute(insert_query)
    print("PIPELINE LIVE -> 3 target accounts injected into outbound_prospects table.")

    cursor.close()
    connection.close()

except Exception as error:
    print("EXECUTION FAILED ->", error)
