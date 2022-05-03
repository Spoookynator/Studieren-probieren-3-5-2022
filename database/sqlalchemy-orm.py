from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, create_engine, MetaData, Table, Column, Integer, String, Float

engine = create_engine('sqlite:///database/example2.db', echo=False)

Base = declarative_base()

class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key = True )
    name = Column(String)
    salary = Column(Float)
    email = Column(String)

    
    def __init__(self, name, salary, email):
        self.name = name,
        self.salary = salary,
        self.email = email
    
    Base.metadata.create_all(engine)
    
    from sqlalchemy.orm import sessionmaker
    SessionClass = sessionmaker(bind = engine)
    
    session = SessionClass()
    
    session.commit()
    session.close()
    