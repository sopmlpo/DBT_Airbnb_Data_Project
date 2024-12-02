import os
from google.cloud import translate_v2 as translate
import psycopg2

# Set up the Google Translate client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/google-credentials.json'
translate_client = translate.Client()

# Database connection details
DB_CONNECTION = {
    'dbname': 'your_database',
    'user': 'your_username', 
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port'
}

def translate_text(text, target_language='en'):
    """Translate text using Google Translate API."""
    if isinstance(text, str):
        return translate_client.translate(text, target_language=target_language)['translatedText']
    return text

def fetch_and_translate():
    """Fetch untranslated reviews, translate them, and update the database."""
    conn = psycopg2.connect(**DB_CONNECTION)
    cursor = conn.cursor()

    # Fetch untranslated reviews
    cursor.execute("SELECT id, review_text FROM src_reviews WHERE translated_review_text IS NULL")
    rows = cursor.fetchall()

    for row in rows:
        review_id, review_text = row
        translated_text = translate_text(review_text)

        # Update the translated text in the database
        cursor.execute(
            "UPDATE src_reviews SET translated_review_text = %s WHERE id = %s",
            (translated_text, review_id)
        )
        conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    fetch_and_translate()
