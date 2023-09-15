from supabase import create_client, Client
import os

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def get_all_jobs():
  data = supabase.table("Jobs").select("*").execute()
  return data.data

def add_job(company,title,location,salary):
  job = {
    "company": company,
    "title": title,
    "location": location,
    "salary": salary
  }
  data = supabase.table("Jobs").insert(job).execute()
  return data.data