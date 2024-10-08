import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


class Scraping:

    def __init__(self, source_url):
        
        self.source_url = source_url

    def get_content(self, url):
        '''
        Realizar a requisição HTTP e retornar o conteúdo
        '''

        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            print(f'ERRO: {e}')
            return None

    def get_subopt(self, opt):

        '''
        Identificar e retornar todas subopções de uma opção
        '''

        url = f'{self.source_url}/index.php?opcao={opt}' 

        content = self.get_content(url)

        if content:

            soup = BeautifulSoup(content, 'lxml')
            return [btn['value'] for btn in soup.find_all('button', class_='btn_sopt')]

        return []

    def get_download_url(self, opt, sub_opt = None):

        '''
        Identificar e retornar a URL de download do CSV para cada opção e subopção
        '''

        if sub_opt:
            url = f'{self.source_url}/index.php?subopcao={sub_opt}&opcao={opt}'
        else:
            url = f'{self.source_url}/index.php?opcao={opt}'

        content = self.get_content(url)

        if content:

            soup = BeautifulSoup(content, 'lxml')
            btn_download = soup.find('a', class_='footer_content')

            if btn_download and 'href' in btn_download.attrs:

                return f"{self.source_url}/{btn_download['href']}"

        return None

    def get_all_download_urls(self, options):

        '''
        Realizar o mapeamento das combinação de opção, subopção e URL de download
        '''

        result = []
        
        for opt in options:
            sub_opts = self.get_subopt(opt)

            if sub_opts:
                for sub_opt in sub_opts:
                    download_url = self.get_download_url(opt, sub_opt)
                    if download_url:
                        result.append({
                            'opt': opt,
                            'sub_opt': sub_opt,
                            'download_url': download_url
                        })
            else:
                download_url = self.get_download_url(opt)
                if download_url:
                    result.append({
                        'opt': opt,
                        'sub_opt': None,
                        'download_url': download_url
                    })
        
        return result

    def download_csv(self, download_url, folder_path, file_name):

        '''
        Realizar o download e escrita do CSV
        '''

        content = self.get_content(download_url)

        if content:

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            file_path = os.path.join(folder_path, file_name)

            with open(file_path, 'wb') as file:
    
                file.write(content)

