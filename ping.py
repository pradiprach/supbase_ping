import os
import requests

# These will be pulled from GitHub Secrets for security
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def ping_supabase():
    # We call a simple select on any table (e.g., 'todos' or 'users')
    # Use your actual table name here
    url = f"{SUPABASE_URL}/rest/v1/users?select=id&limit=1"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("Successfully pinged Supabase. Project is active!")
        else:
            print(f"Ping failed with status: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ping_supabase()
