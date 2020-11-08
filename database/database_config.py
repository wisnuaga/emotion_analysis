import databases
from sqlalchemy import Integer, Float, Table, create_engine, Column, MetaData, String
from config.config import Config

OBJ_CONFIG = Config()

# Postgres DB
DATABASE_URL = OBJ_CONFIG.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = MetaData()

corpus_schema = Table(
    'corpus',
    metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('text', String),
    Column('anger', Float),
    Column('disgust', Float),
    Column('fear', Float),
    Column('happiness', Float),
    Column('sadness', Float),
    Column('surprise', Float)
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
