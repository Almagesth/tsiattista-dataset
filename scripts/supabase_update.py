import requests
from supabase import create_client, Client

# Your Supabase details
SUPABASE_URL = "https://ficxtkpygbmwydmiyaar.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZpY3h0a3B5Z2Jtd3lkbWl5YWFyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NTk3MjQ3NSwiZXhwIjoyMDYxNTQ4NDc1fQ.oJ2OjqwPCk0U1zVr4jLFR_ZRiwzq0P0rx1PRjZtCGts"

# Connect to Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get tsiattista.json from GitHub
url = "https://raw.githubusercontent.com/Almagesth/tsiattista-dataset/main/tsiattista.json"
response = requests.get(url)
poems = response.json()

# Upsert poem into the table
for poem in poems:
    try:
        supabase.table("tsiattista").upsert({
            "id": poem["id"],
            "text": poem["text"],
            "title": poem["title"],
            "author": poem["author"],
            "theme": poem["theme"],
            "secondary_themes": poem.get("secondary_themes", []),
            "verses": poem["verses"],
            "short_verses": poem.get("short_verses", []),
            "syllables": poem["syllables"],
            "rhyme": poem["rhyme"],
            "notes": poem.get("notes", ""),
            "syllable_pattern": poem.get("syllable_pattern")
        }, on_conflict='id').execute()
        print(f"Processed poem {poem['id']}: {poem['title']}")
    except Exception as e:
        print(f"Error processing poem {poem['id']}: {e}")

print("All done!")