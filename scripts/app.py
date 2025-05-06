from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from supabase import create_client, Client

app = Flask(__name__)
Bootstrap(app)

SUPABASE_URL = "https://ficxtkpygbmwydmiyaar.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZpY3h0a3B5Z2Jtd3lkbWl5YWFyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NTk3MjQ3NSwiZXhwIjoyMDYxNTQ4NDc1fQ.oJ2OjqwPCk0U1zVr4jLFR_ZRiwzq0P0rx1PRjZtCGts"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def index():
    poems = supabase.table("tsiattista").select("*").execute().data
    return render_template('index.html', poems=poems)

@app.route('/poem/<int:poem_id>')
def poem_detail(poem_id):
    poem = supabase.table("tsiattista").select("*").eq("id", poem_id).execute().data[0]
    return render_template('poem.html', poem=poem)

if __name__ == '__main__':
    app.run(debug=True)