import os 
import uvicorn

from src.database.scrapper import Scrapper

def pipeline():

    '''
    Execução de todo pipeline de extração dos dados
    '''
    
    scraper = Scrapper()

    scraper.run()

    uvicorn.run("endpoints.api:server.app", host="127.0.0.1", port=8000, reload=True)

if __name__ == '__main__':

    pipeline()
