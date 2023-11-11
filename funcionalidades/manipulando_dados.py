import requests
import base64
import pandas as pd


# Extraindo dados dos repositórios

##  especificando a versão da API do github utilizada para realizar a requisição:
headers = {'X-Github-Api-Version': '2022-11-28'}

api_base_url = 'https://api.github.com' # base da url que irá ser utilizada;
owner = 'amzn' #username de quem vamos extrair os dados - nome do usuário da amazon;
url = f'{api_base_url}/users/{owner}/repos' #Endpoint que utilizaremos para extrair os dados necessários do usuário da amzon;

response = requests.get(url, headers = headers)
response.status_code
response.json()

len(response.json()) #retornando o tamanho da lista;

acess_token = 'your_token'
headers = {'Authorization': 'Bearer ' + acess_token, 
           'X-Github-Api-Version': '2022-11-28'}


## Paginação

api_base_url = 'https://api.github.com' 
owner = 'amzn' 
url = f'{api_base_url}/users/{owner}/repos'

repos_list = []
for page_num in range(1, 6):
    try:
        url_page = f'{url}?page={page_num}'
        response = requests.get(url_page, headers=headers)
        repos_list.append(response.json())
    except:
        repos_list.append(None)
        
len(repos_list)
len(repos_list[0])

# Transformando os dados

repos_list.json()
repos_list[0][3]['name']

# percorrendo uma lista para retornar todos os nomes a fim de alimentar uma lista;

repos_name = []
for page in repos_list:
    for repo in page:
        repos_name.append(repo['name'])

## Linguagens dos repositórios

repos_list[1][2]['language']

repos_language = []
for page in repos_list:
    for repo in page:
        repos_language.append(repo['language'])
    

## Criando um DataFrame com Pandas;

dados_amazon = pd.DataFrame()
dados_amazon['repository_name'] = repos_name
dados_amazon['repository_language'] = repos_language

## salvando a tabela no formato csv;

dados_amazon.to_csv('Amazon.csv')

# Armazenando Dados

# criando repositório no git hub
data = {
    'name': 'languages-used',
    'description': 'Repository with programming languages ​​used on Amazon',
    'private': False
        }

response = requests.post(url, json = data, headers = headers)
response.status_code

#Transformando o formato do arquivo para base64

# import base64 - Importado no inicio do arquivo

with open('Amazon.csv', 'rb') as file:
    file_content = file.read()
    
encoded_content = base64.b64encode(file_content)

# upload do arquivo por meio da requisição put

api_base_url = 'https://api.github.com' # API BASE;
username = 'thelastbeto' # Username do github para que se possa enviar o conteúdo ao meu repositório;
repo = 'languages-used' # Nome do repositório no github que desejo enviar o conteúdo;
path = 'Amazon.csv' # Caminho do arquivo no qual desejo que seja salvo em nosso repositório;

url = f'{api_base_url}/repos/{username}/{repo}/contents/{path}' # URL do arquivo por meio da requisição put;

# Definindo dicionário com as informações que desejamos passar no momento de fazer o upload do arquivo

data = {
   'message' : 'Adding a new file',
    'content': encoded_content.decode('utf-8'), 
}

# requisição put usada para criar ou atualizar um recurso no servidor

response = requests.put(url, json=data, headers=headers)
response.status_code

