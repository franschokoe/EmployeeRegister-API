from supabase import create_client ,Client
from sqlalchemy.orm import declarative_base , sessionmaker
from sqlalchemy import create_engine
from app.setup import settings

"""For fastapi"""
# SUPABASE_URL = settings.supabase_url
# SUPABASE_KEY = settings.supabase_key
"""For testing"""
# SUPABASE_URL = "https://axjtuszowtmfvddhfsko.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF4anR1c3pvd3RtZnZkZGhmc2tvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjU5MTYwNzIsImV4cCI6MjA4MTQ5MjA3Mn0.xQVdK_qDRkUif_f6z_cllP4dhYtkbf2ZvYUyV8xtcdg"

# supabase: Client = create_client(SUPABASE_URL , SUPABASE_KEY)

# supabase.table("project1T").insert({"first_name": "Frans Chokoe"}).execute()

# results_query = supabase.table("project1T").select("*").execute()
# print(results_query)
# results = supabase.table("project1T").select("*").execute()

# print(results)
"""DATABASE CONNSECTION"""
# DATABASE_URL = f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@db.{settings.database_host}/{settings.database_username}"
# DATABASE_URL = "postgresql+psycopg2://postgres:28franschokoe@db.axjtuszowtmfvddhfsko.supabase.co:5432/postgres"
"""Seccessfull connection"""
DATABASE_CONNECTION = settings.database_connection


engine = create_engine(DATABASE_CONNECTION)
SessionLocal = sessionmaker(bind=engine , autocommit = False , autoflush=False)

Base = declarative_base()
# Access to database
def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()