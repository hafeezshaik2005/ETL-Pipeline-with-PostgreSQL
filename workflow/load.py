from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

# PostgreSQL configuration
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def load_to_postgres(df,table_name):

    engine=create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    df.to_sql(table_name,
              engine,
              if_exists="replace",
              index=False)

    print("Data loaded to postgres successfully")
