import os 

from scraping import Scraping

def main():

    '''
    Execução de todo pipeline de extração dos dados
    '''

    scraper = Scraping(source_url='http://vitibrasil.cnpuv.embrapa.br')
    
    options = ['opt_02', 'opt_03', 'opt_04', 'opt_05', 'opt_06']

    download_data= scraper.get_all_download_urls(options=options)

    for data in download_data:
        opt = data['opt']
        sub_opt = data['sub_opt'] if data['sub_opt'] else 'default'
        download_url = data['download_url']
        file_name = f"{opt}_{sub_opt}.csv"
        file_path = 'src/database/temp_files'
        scraper.download_csv(download_url, file_path, file_name)

if __name__ == '__main__':

    main()
