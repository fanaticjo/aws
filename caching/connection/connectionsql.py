from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from caching.secrets.getSecet import rdsSecret
import os


connection=rdsSecret(os.environ['rds'])
engine = create_engine(connection,echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()