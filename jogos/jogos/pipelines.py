# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker, query
from jogos.models import jogosfutDB, db_connect, create_table, campeonatosDB, timesDB
from datetime import date, datetime
from datetime import timedelta


class JogosPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        engine = db_connect() 
        self.Session = sessionmaker(bind=engine)
        session = self.Session()
        gamesfutDB = jogosfutDB()
        gamesfutDB.diahorario = datetime.strptime(item["diahorario"],'%Y-%m-%dT%H:%M:%S')
        gamesfutDB.jogocampe = item["campeonato"]
        gamesfutDB.timecasa = item["timecasa"]
        gamesfutDB.timecasaabbr = item["timecasaabbr"]
        gamesfutDB.timecasaimg_url = item["timecasaimg_url"]
        gamesfutDB.timevisitante =  item["timevisitante"]
        gamesfutDB.timevisitanteabbr = item["timevisitanteabbr"]
        gamesfutDB.timevisitanteimg_url = item["timevisitanteimg_url"]
        gamesfutDB.placar_timecasa = item["placar_timecasa"]
        gamesfutDB.placar_timevisitante = item["placar_timevisitante"]
        j = session.query(jogosfutDB.jogoid).filter(jogosfutDB.jogocampe == gamesfutDB.jogocampe, jogosfutDB.timecasa == gamesfutDB.timecasa, jogosfutDB.timevisitante == gamesfutDB.timevisitante, jogosfutDB.diahorario == gamesfutDB.diahorario).first()
        #jogoexistente = session.query(jogosfutDB).get({'jogocampe':gamesfutDB.jogocampe, "timecasa":gamesfutDB.timecasa, "timevisitante":gamesfutDB.timevisitante, "jogocampe":gamesfutDB.jogocampe})
        print('Esse é o J', j)
        #print('Esse é o Jogoexistente', jogoexistente)
        if j is None:
            try:
                session.add(gamesfutDB)
                session.commit()
            except:
                session.rollback()
            finally:
                session.close()
        else:
            try:
                session.query(jogosfutDB).filter(jogosfutDB.jogoid == j).update({'timevisitanteimg_url':gamesfutDB.timevisitanteimg_url, 'placar_timecasa':gamesfutDB.placar_timecasa , 'placar_timevisitante':gamesfutDB.placar_timevisitante})
                session.commit()
            except:
                session.rollback()
            finally:
                session.close()

        
        

        return item