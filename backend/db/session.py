from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import Settings

SQLALCHEMY_DATABASE_URL = Settings.DATABASE_URL
print("Database url is ",SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#once we have engine we need to create some set of sessions - sessionlocal
SESSION_LOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)
#if we create an instance of this session that gives me an actual database session that we can to actually query the database
#later -- in dependency injection section we will use dependency injection to actually to get a database session

