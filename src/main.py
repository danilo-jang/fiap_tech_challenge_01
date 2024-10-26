import os 

from database.scrapper import Scrapper

def main():

    '''
    Execução de todo pipeline de extração dos dados
    '''
    scraper = Scrapper()

    scraper.run()

if __name__ == '__main__':

    main()
