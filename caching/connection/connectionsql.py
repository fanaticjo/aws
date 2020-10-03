from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:legato123@localhost:5432/demo',echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()