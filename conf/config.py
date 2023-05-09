import os

def setDbConfig(db_name, stage):
    DB_HOST = os.getenv("DB_HOST")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD     = os.getenv("DB_PASSWORD")
    
    if stage == "development":
        psql_conn = os.getenv("PSQL_CONN", f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:5432/{db_name}")
    if stage == "production":
        psql_conn = os.getenv("PSQL_CONN", f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:5432/{db_name}")
    
    return psql_conn