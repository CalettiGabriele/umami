from sqlalchemy import create_engine, Column, Integer, String, Date, Float, Boolean, ForeignKey, JSON, func
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()


class Associato(Base):
    __tablename__ = 'associato'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cognome = Column(String)
    data_nascita = Column(Date)
    luogo_nascita = Column(String)
    email = Column(String)
    cellulare = Column(String)
    data_associazione = Column(Date)
    collegamenti = Column(JSON)

class Prestazione(Base):
    __tablename__ = 'prestazione'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_servizio = Column(Integer, ForeignKey('Servizio.id'))
    usufruitore = Column(Integer, ForeignKey('Associato.id'))
    data_prestazione = Column(Date)

class Servizio(Base):
    __tablename__ = 'servizio'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    descrizione = Column(String)
    costo = Column(Float)
    personale = Column(Boolean)

class Transazione(Base):
    __tablename__ = 'transazione'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    ammontare = Column(Float)
    data_transazione = Column(Date)
    modalita = Column(String)
    id_associato = Column(Integer, ForeignKey('Associato.id'))
    id_prestazione = Column(Integer, ForeignKey('Prestazione.id'))