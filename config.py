import platform
import os
from dotenv import load_dotenv

DEV_MODE= platform.system() != "Linux"


BASE_URL = "https://loyal-gold.vercel.app/pass/"

load_dotenv()

SUPABASE_URL = os.getenv("PUBLIC_SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("PUBLIC_SUPABASE_ANON_KEY")