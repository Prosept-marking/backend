from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost/db_prosept'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class DealerproductPG(Base):
    __tablename__ = 'dealer_products'

    id = Column(Integer, primary_key=True, index=True)
    product_key = Column(String)
    price = Column(Float)
    product_url = Column(String)
    product_name = Column(String)
    date = Column(String)
    dealer_id = Column(Integer)


Base.metadata.create_all(bind=engine)
