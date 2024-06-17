import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://mika:mika2306@host.docker.internal:3307/items")

# Création du moteur SQLAlchemy
engine = create_engine(DATABASE_URL)

# Création d'une session SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Déclaration de la classe de base pour les modèles SQLAlchemy
Base = declarative_base()

