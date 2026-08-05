

from config import *
from supabase import create_client , Client



supabase : Client = create_client(supabase_url= SUPABASE_URL, supabase_key=SUPABASE_SERVICE_ROLE_KEY)



def insert_card(uid):
    #look into supabase table - cards, select uid column, equals to uid column and execute this 
    existing = supabase.table("cards").select("uid").eq("uid" , uid).execute()

    #check if duplicate data
    if existing.data:
        print(f"UID {uid} already exists, skipping")
        return existing

    result = supabase.table("cards").insert({"uid" : uid , "valid" : True}).execute()


    return result