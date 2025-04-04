from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_URL = 'sqlite:///./todosApp.db'

engine=  create_engine(SQLALCHEMY_URL,connect_args={'check_same_thread' : False })

sessionLocal = sessionmaker(autocommit = False, autoflush=False, bind = engine)

Base = declarative_base()
