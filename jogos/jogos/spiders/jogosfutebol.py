import scrapy
from datetime import datetime 
from datetime import timedelta


class JogosfutebolSpider(scrapy.Spider):
    name = 'JogosfutebolSpider'
    allowed_domains = ['https://globoesporte.globo.com']
    now = datetime.now()
    now = now - timedelta(days=60)
    start_urls = []
    i=1

    while i <= 63:
        url = 'https://globoesporte.globo.com/placar-ge/'+(now.strftime('%d-''%m-''%Y'))+'/jogos.ghtml'   
        start_urls.append(url)
        now = now + timedelta(days=1)
        i+=1
    

    def start_request(self):
        for url in start_urls:
            yield scrapy.Request(url,callback = self.parse)


    def parse(self, response):
            for article in response.css("article"):
                campeonato = article.css("header.header h1 span::text").get()
                diahorario= article.css("header.header h1 time::attr(datetime)").get()
                timecasa = article.css("div.resultado-time-container div.mandante span::text").get()
                timecasaabbr = article.css("div.resultado-time-container div.mandante abbr::text").get()
                timecasaimg_url = article.css("div.resultado-time-container div.mandante img::attr(src)").get()
                timevisitante = article.css("div.resultado-time-container div.visitante span::text").get()
                timevisitanteabbr = article.css("div.resultado-time-container div.visitante abbr::text").get()
                timevisitanteimg_url = article.css("div.resultado-time-container div.visitante img::attr(src)").get()
                placar_timecasa = article.css("div.resultado-time-container div.resultado span.placar-mandante::text").get()
                placar_timevisitante= article.css("div.resultado-time-container div.resultado span.placar-visitante::text").get()
                yield  {'campeonato':campeonato, 'diahorario':diahorario, 'timecasa':timecasa, 'timecasaabbr':timecasaabbr,
                    'timecasaimg_url':timecasaimg_url, 'timevisitante':timevisitante, 'timevisitanteabbr':timevisitanteabbr, 'timevisitanteimg_url':timevisitanteimg_url, 'placar_timecasa':placar_timecasa, 'placar_timevisitante':placar_timevisitante}
            

            