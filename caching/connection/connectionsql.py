from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:legato123@database-1.cp1izo9cyb3k.us-east-1.rds.amazonaws.com:5432/demo')
Session = sessionmaker(bind=engine)

Base = declarative_base()