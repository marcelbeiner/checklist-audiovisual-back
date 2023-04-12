from model import Base
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship


class Checklist(Base):
    __tablename__ = 'check-list'
    
    id = Column('pk_checklist', Integer, primary_key = True)
    nome = Column(String(140))
    valor = Column(Float)
    serial_number = Column(String, unique = True)
    observacao = Column(String)
    
    def __init__(self, nome:str, valor:float, serial_number:str, observacao:str):
    
        self.nome = nome
        self.valor = valor
        self.serial_number = serial_number
        self.observacao = observacao
    
     