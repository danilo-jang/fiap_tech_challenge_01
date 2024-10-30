import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re

class Scrapper:

    def __init__(self):
        
        self.source_url = 'http://vitibrasil.cnpuv.embrapa.br'

    def get_content(self, url, options = "", sub_options = ""):
        '''
        Realizar a requisição HTTP e retornar o conteúdo
        '''

        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            #file_name = url.split("=")[-1]
            file_name = url.split("/")[-1]
            print(f"options[file_name] {options[file_name]}")
            if options and not options[file_name]:
                file_name = f"{options[file_name]}_default.csv"
            elif sub_options and not sub_options[file_name]:
                file_name = f"{sub_options[file_name]}.csv"
            print(f"file_name {file_name}")
            pattern = re.compile(f"{file_name}[^ ]+.csv")
            found = False
            #print(f"pattern {pattern}")
            for fp in os.listdir("src/database/temp_files/"):
                match = pattern.match(fp)
                #print(f"fp {fp} match {match}")
                if match:
                    file_name = f"src/database/temp_files/{str(match.group(0))}"
                    print(f"O CSV correspondente [{file_name}] existe, tamanho [{os.path.getsize(file_name)}]")
                    #response = BeautifulSoup(open(file_name, "rb"), 'lxml')
                    #response = open(file_name, "rb")
                    #print(f"response {response}")
                    #return response
                    found = True
                    #break
            if not found:
                print(f'\nURL [{url}] \nERRO: [{e}]\n')

            return None

    def get_subopt(self, opt):

        '''
        Identificar e retornar todas subopções de uma opção
        '''

        url = f'{self.source_url}/index.php?opcao={opt}' 

        print(f"Pegando subopcao {url} {opt}")
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

        print(f"Obtendo a URL de download {opt} {sub_opt}")
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

    def download_csv(self, download_url, folder_path, file_name, options, sub_options):

        '''
        Realizar o download e escrita do CSV
        '''

        print(f"Baixando {download_url} {folder_path} {file_name}")
        content = self.get_content(download_url, options, sub_options)

        if content:

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            file_path = os.path.join(folder_path, file_name)

            with open(file_path, 'wb') as file:
    
                file.write(content)

    def run(self):

        #options = ['opt_02', 'opt_03', 'opt_04', 'opt_05', 'opt_06']
        options = {'Producao.csv':'opt_02', 'opt_03':'opt_03', 'Comercio.csv':'opt_04', 'opt_05':'opt_05', 'opt_06':'opt_06'}
        sub_options = {'ProcessaViniferas.csv':'opt_03_subopt_01', 'ProcessaAmericanas.csv':'opt_03_subopt_02', 'ProcessaMesa.csv':'opt_03_subopt_03', 'ProcessaSemclass.csv':'opt_03_subopt_04', 
                       'ImpVinhos.csv':'opt_05_subopt_01', 'ImpEspumantes.csv':'opt_05_subopt_02', 'ImpFrescas.csv':'opt_05_subopt_03', 'ImpPassas.csv':'opt_05_subopt_04', 'ImpSuco.csv':'opt_05_subopt_05',
                       'ExpVinho.csv':'opt_06_subopt_01', 'ExpEspumantes.csv':'opt_06_subopt_02', 'ExpUva.csv':'opt_06_subopt_03', 'ExpSuco.csv':'opt_06_subopt_04'}

        print(f"Baixando os dados da EMBRAPA ...")
        download_data= self.get_all_download_urls(options=options)
        print(f"{download_data}\n")

        for data in download_data:
            opt = data['opt']
            sub_opt = data['sub_opt'] if data['sub_opt'] else 'default'
            download_url = data['download_url']
            file_name = f"{opt}_{sub_opt}.csv"
            file_path = 'src/database/temp_files'
            print(f"Download CSV {download_url} ...")
            self.download_csv(download_url, file_path, file_name, options, sub_options)
        