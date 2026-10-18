import os
import time

import psycopg2
from dotenv import load_dotenv
from google import genai

# Load environment variables from the local .env file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("CRITICAL: GEMINI_API_KEY is missing from environment variables.")

# Initialize the V2 Gemini client securely
client = genai.Client(api_key=api_key)

try:
    connection = psycopg2.connect(
        dbname="gtm_engine", user="srivastavaatharvaalok", host="localhost", port="5432"
    )
    cursor = connection.cursor()

    cursor.execute(
        "SELECT lead_id, company_name, decision_maker, intent_score FROM outbound_prospects WHERE outreach_status = 'Pending';"
    )
    leads = cursor.fetchall()

    print("--- INITIATING AI OUTREACH GENERATION (SECURE V3.8 ENGINE) ---")

    for lead in leads:
        lead_id, company, dm_name, score = lead
        prompt = f"Write a strict 3-line cold email to {dm_name} at {company}. Mention we noticed their high intent score of {score} and offer a quick AI automation audit. Do not use generic greetings."

        # Exponential backoff loop for network or 503 high-demand spikes
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash", contents=prompt
                )
                print(f"\nTarget: {company} | Decision Maker: {dm_name}")
                print(f"Generated Copy:\n{response.text.strip()}")
                print("-" * 40)

                cursor.execute(
                    "UPDATE outbound_prospects SET outreach_status = 'Drafted AI Copy' WHERE lead_id = %s;",
                    (lead_id,),
                )
                break
            except Exception as api_error:
                if "503" in str(api_error) or "UNAVAILABLE" in str(api_error):
                    wait_time = 2**attempt
                    print(f"Server busy. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    raise api_error

    connection.commit()
    cursor.close()
    connection.close()

except Exception as error:
    print("AI EXECUTION FAILED ->", error)
