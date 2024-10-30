<p align="center">
  <img src="./images/fiap_logo.jpg" alt="Logo Embrapa"  width="300" height="300">
</p>

## Tech Challenge - Vitivinicultura Embrapa API
Este repositório foi criado com o objetivo de desenvolver uma API focada na vitivinicultura da Embrapa, como parte do desafio técnico da fase 1 da pós-graduação em Machine Learning Engineering.

### 👥 Grupo 
- Renato Martinelli
- Danilo Jang

### Objetivo
Baseado na Produção, Processamento e Comercialização, oferecer sugestões para melhoria da Exportação.

### Arquitetura

<a href="./2024-10-FIAP-3MLET-Arquitetura.pdf">FIAP-3MLET-Arquitetura.pdf</a>

A arquitetura da solução consiste de uma camada de APIs REST, cada qual apontando para um endpoint específco no site da EMBRAPA:
- Produção
- Processamento
- Comercialização
- Importação
- Exportação

As APIs podem ser consultadas isoladamente, internamente existe um mecanismo de download das informações para um arquivo CSV, que irá alimentar um banco de dados.
Este Banco de Dados serão as entradas para o Modelo de Machine Learning que construiremos na sequência.

### Pipeline

<a href="./2024-10-FIAP-3MLET-Pipeline.pdf">FIAP-3MLET-Pipeline.pdf</a>

A pipeline é construída usando GITHUB Actions seguindo o modelo Trunk-Based. Existe uma branch main e cada desenvolvimento é feito numa feature, que ao estarem prontas são integradas na main.
Ao ocorrer um push na branch main, inicia-se o workflow de CI que realiza as seguintes operações:
- Consultar os endpoints
- Baixar os CSV
- Gravar as informações no Banco de Dados
- Gerar Tag da versão atual criada

Caso o CI ocorra com sucesso, o Modelo de Machine Learning será criado / atualizado na sequência.


pipenv shell

pipenv install fastapi uvicorn requests
cd src/api/
uvicorn api:server.app --reload


>>> pattern = re.compile("opt_02_default[^ ]+")
>>> print(f"{pattern}")
re.compile('opt_02_default[^ ]+')
>>> match = pattern.match("opt_02_default.csv")
>>> print(f"{match}")
<re.Match object; span=(0, 18), match='opt_02_default.csv'>

p=r"" + file_name + "[^ ]+"
>>> pattern = re.compile(p)

>>> pattern = re.compile(r"opt_02_default[^ ]+")
>>> match = pattern.match(r"opt_02_default.csv")
>>> print(f"{match}")

Download CSV http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv ...
Baixando http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv src/database/temp_files opt_05_subopt_03.csv

URL [http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv] 
ERRO: [HTTPConnectionPool(host='vitibrasil.cnpuv.embrapa.br', port=80): Max retries exceeded with url: /download/ImpFrescas.csv (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x1169261e0>: Failed to establish a new connection: [Errno 61] Connection refused'))]

btendo a URL de download opt_06 subopt_04
[{'opt': 'opt_02', 'sub_opt': None, 'download_url': 'http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv'}, {'opt': 'opt_03', 'sub_opt': 'subopt_01', 'download_url': 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv'}, {'opt': 'opt_03', 'sub_opt': 'subopt_02', 'download_url': 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv'}, {'opt': 'opt_03', 'sub_opt': 'subopt_03', 'download_url': 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv'}, {'opt': 'opt_0

python3 src/pipeline.py

http://127.0.0.1:8000/docs#/

http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04


sudo apt install docker-compose
sudo usermod -aG docker <user>

export MONGODB_URL="mongodb+srv://pos3mlet:pos3mlet@127.0.0.1:27017/pos3mlet?retryWrites=true&w=majority"



