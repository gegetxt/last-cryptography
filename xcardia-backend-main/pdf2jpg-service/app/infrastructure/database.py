from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL bağlantı URL'sini buraya yaz
DATABASE_URL = "postgresql://postgres:projecT41@db/xcardia"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
from app.infrastructure.database import engine, Base
from app.domain.models import ConversionLog
Base.metadata.create_all(bind=engine)
