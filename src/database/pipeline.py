import os 

from scraping import Scraping

def main():

    '''
    Execução de todo pipeline de extração dos dados
    '''
    scraper = Scraping()

    scraper.run()

if __name__ == '__main__':

    main()
