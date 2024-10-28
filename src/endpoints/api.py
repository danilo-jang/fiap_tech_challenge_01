from typing import Union
import requests
import re
import os

#import uvicorn
from fastapi import FastAPI
#, APIRouter
#from fastapi_utils.cbv import cbv
#from fastapi_utils.inferring_router import InferringRouter

#app = FastAPI()
#router = APIRouter()

#@router.get("/", tags=["index"])
class Api:

    def __init__(self):
        self.app = FastAPI()
        self.source_url = 'http://vitibrasil.cnpuv.embrapa.br'

        def handle_csv(year, opt, sub_opt):
            file_path = "src/database/temp_files/"
            sopt = ""
            if sub_opt:
                sopt = f"_subopt_{sub_opt}([^ ]+|)"
            pattern = re.compile(f"{opt}([^ ]+|){sopt}.csv")
            print(f"pattern {pattern}")
            for fp in os.listdir(file_path):
                print(f"fp [{fp}]")
                match = pattern.match(fp)
                print(f"match {match}")
                found = False
                if match:
                    print(f"O CSV correspondente [{fp}] existe, tamanho [{os.path.getsize(file_path)}]")
                    response = {}
                    header=""
                    idx=0
                    with open(f"{file_path}{fp}", 'rb') as f:
                        lines = f.readlines()#.replace("\t", ";")
                        for l in lines:
                            print(f"l {l}")
                            if not header:
                                header = l
                                #print(f"header {header.decode().split(";")}")
                                print(f"header {re.split("[;,\t]", header.decode())}")
                                #idx = header.decode().split(";").index(f"{year}")
                                idx = re.split("[;,\t]", header.decode()).index(f"{year}")
                                print(f"idx {idx}")
                            else:
                                response[re.split("[;,\t]", l.decode())[1]]=re.split("[;,\t]", l.decode())[idx]
                                #response[l.decode().split(";")[1]]=l.decode().split(";")[idx]
                        print(f"response {response}")
                    found = True
                if found:
                    return response
        
        @self.app.get("/")
        async def read_root():
            return {"API": "V1"}
        
        @self.app.get("/producao")
        async def get_producao(ano: int):
            try:
                url = f"{self.source_url}/index.php?opcao=opt_02"
                if ano:
                    url = url + f"&ano={str(ano)}" 

                response = requests.get(url)
                response.raise_for_status()
                raise requests.RequestException
                return response.content
            except requests.RequestException as e:
                response = handle_csv(ano, "opt_02", "")
                if not response:
                    print(f'\nURL [{url}] \nERRO: [{e}]\n')
                    return None                
                #file_path = "../database/temp_files/"
                #pattern = re.compile("opt_02[^ ]+.csv")
                #print(f"pattern {pattern}")
                #for fp in os.listdir(file_path):
                #    print(f"fp [{fp}]")
                #    match = pattern.match(fp)
                #    print(f"match {match}")
                #    found = False
                #    if match:
                #        print(f"O CSV correspondente [{fp}] existe, tamanho [{os.path.getsize(file_path)}]")
                #        response = {}
                #        header=""
                #        idx=0
                #        with open(f"{file_path}{fp}", 'rb') as f:
                #            lines = f.readlines()
                #            for l in lines:
                #                if not header:
                #                    header = l
                #                    print(f"header {header.decode().split(";")}")
                #                    idx = header.decode().split(";").index(f"{ano}")
                #                    print(f"idx {idx}")
                #                else:
                #                    response[l.decode().split(";")[1]]=l.decode().split(";")[idx]
                #            print(f"response {response}")
                #        found = True
                #    if found:
                #        break
                #if not found:
                #    print(f'\nURL [{url}] \nERRO: [{e}]\n')
                #    return None

            return response

        @self.app.get("/processamento")
        async def get_processamento(sub_opcao: str, ano: int):
            try:
                print(f"sub_opcao {sub_opcao}")
                url = f"{self.source_url}/index.php?opcao=opt_03&sub_opt={sub_opcao}"
                if ano:
                    url = url + f"&ano={str(ano)}" 

                response = requests.get(url)
                response.raise_for_status()
                raise requests.RequestException
                return response.content
            except requests.RequestException as e:
                response = handle_csv(ano, "opt_03", sub_opcao)
                if not response:
                    print(f'\nURL [{url}] \nERRO: [{e}]\n')
                    return None                

            return response

        @self.app.get("/comercializacao")
        async def get_comercializacao(ano: int):
            try:
                url = f"{self.source_url}/index.php?opcao=opt_04"
                if ano:
                    url = url + f"&ano={str(ano)}" 

                response = requests.get(url)
                response.raise_for_status()
                raise requests.RequestException
                return response.content
            except requests.RequestException as e:
                response = handle_csv(ano, "opt_04", "")

            return response

        @self.app.get("/importacao")
        async def get_importacao(ano: int, sub_opcao: str = ""):
            try:
                print(f"sub_opcao {sub_opcao}")
                url = f"{self.source_url}/index.php?opcao=opt_05"
                if sub_opcao:
                    url = url + f"&sub_opt={sub_opcao}" 
                if ano:
                    url = url + f"&ano={str(ano)}" 

                response = requests.get(url)
                response.raise_for_status()
                raise requests.RequestException
                return response.content
            except requests.RequestException as e:
                response = handle_csv(ano, "opt_05", sub_opcao)
                if not response:
                    print(f'\nURL [{url}] \nERRO: [{e}]\n')
                    return None                

            return response
        
        @self.app.get("/exportacao")
        async def get_exportacoa(sub_opcao: str, ano: int):
            try:
                print(f"sub_opcao {sub_opcao}")
                url = f"{self.source_url}/index.php?opcao=opt_06&sub_opt={sub_opcao}"
                if ano:
                    url = url + f"&ano={str(ano)}" 

                response = requests.get(url)
                response.raise_for_status()
                raise requests.RequestException
                return response.content
            except requests.RequestException as e:
                response = handle_csv(ano, "opt_06", sub_opcao)
                if not response:
                    print(f'\nURL [{url}] \nERRO: [{e}]\n')
                    return None                

            return response
server = Api()

if __name__ == "__main__":
    server.run()