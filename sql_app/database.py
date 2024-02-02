from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#TODO: remover estas credenciales de este lugar
HOST : str = "aws-0-us-west-1.pooler.supabase.com"
USERNAME : str ="postgres.wnsnlwsxdwoeetabejez"
PASSWORD : str ="~s*56K(!Pb-X5Nt"
NAME : str = "postgres"
PORT : str = "6543"

#para sqlLite
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SQLALCHEMY_DATABASE_URL_SUPABASE = "postgresql://postgres.wnsnlwsxdwoeetabejez:~s*56K(!Pb-X5Nt@aws-0-us-west-1.pooler.supabase.com:6543/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL_SUPABASE)

SessionLocal = sessionmaker(bind=engine , autocommit=False, autoflush=False)

Base = declarative_base()