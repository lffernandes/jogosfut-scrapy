from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class campeonatosDB(DeclarativeBase):
    __tablename__ = "tbcampeonatos"
    campid = Column('campid', Integer,primary_key=True)
    campeonato_desc = Column('campeonato_desc', String(45))
    campeonato_dataini = Column('campeonato_dataini', Date())
    campeonato_datafim = Column('campeonato_datafim', Date())

class timesDB(DeclarativeBase):
    __tablename__ = "tbtimes"
    timeid =  Column('timeid', Integer,primary_key=True) 
    timedesc = Column('timedesc', String(45))
    timeabbr = Column('timecasaabbr', String(3))
    timeimg_url = Column('timeimg_url', String(100))

class jogosfutDB(DeclarativeBase):
    __tablename__ = "tbjogos"
    jogoid = Column('jogoid',Integer, primary_key=True)
    diahorario = Column('diahorario', DateTime())
    jogocampe = Column('jogocampe', String(45))
    timecasa = Column('timecasa', String(45))
    timecasaabbr = Column('timecasaabbr', String(3))
    timecasaimg_url = Column('timecasaimg_url', String(100))
    timevisitante = Column('timevisitante', String(45))
    timevisitanteabbr = Column('timevisitanteabbr', String(3))
    timevisitanteimg_url = Column('timevisitanteimg_url', String(100))  
    placar_timecasa = Column('placar_timecasa', String(3))
    placar_timevisitante = Column('placar_timevisitante', String(3))

