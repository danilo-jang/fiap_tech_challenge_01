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

        @self.app.get("/")
        async def read_root():
            return {"Hello": "World"}
        
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
                file_name = "op_02_default"
                pattern = re.compile(r"op_02_default[^ ]+")
                print(f"pattern {pattern}")
                for fp in os.listdir("../database/temp_files/"):
                    print(f"fp {fp}")
                    match = pattern.match(fp)
                    print(f"match {match}")

                    if match:
                        print(f"O CSV correspondente [{file_name}] existe, tamanho [{os.path.getsize(file_name)}]")
                        response = {}
                        header=""
                        idx=0
                        with open(file_path, 'rb') as file:
                            lines = f.readlines()
                            for l in lines:
                                if not header:
                                    header = l
                                    idx = header.split(";").index(str(ano))
                                else:
                                    response[l.split(";")[1]]=l.split(";")[idx]
                    else:
                        print(f'\nURL [{url}] \nERRO: [{e}]\n')

                        return None

            return response

        @self.app.get("/processamento")
        async def get_processamento(ano: int):
            return {"Teste": "Processamento"}

        @self.app.get("/comercializacao")
        async def get_comercializacao(ano: int):
            return {"Teste": "Comercializacao"}

        @self.app.get("/importacao")
        async def get_importacao(ano: int):
            return {"Teste": "Importacao"}

        @self.app.get("/exportacao")
        async def get_exportacoa(ano: int):
            return {"Teste": "Exportacao"}

server = Api()

if __name__ == "__main__":
    server.run()