import requests
import base64

class ManipulaRepositorios:
    
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'  # API BASE;
        self.access_token ='your_token' # Token acess
        self.headers = {'Authorization': "Bearer " + self.access_token, # Focar no espaço após o Bearer
                         'X-GitHub-Api-Version': '2022-11-28'}
        
    def criaRepos(self, nomeRepo):
        data = {
            "name": nomeRepo,
            "description": "Dados utilizados por algumas das maiores empresas do mundo no GitHub",
            "private": False
        }
        
        response = requests.post(f"{self.api_base_url}/user/repos", json=data, headers=self.headers)
        
        print(f'status_code da criação do repositorio: {response.status_code}')
        
    def addArquivo(self, nomeRepo, nomeArquivo, caminhoArquivo):
        
        # codificando o arquivo
        with open(caminhoArquivo, 'rb') as file:
            fileContent = file.read()
        encodedContent = base64.b64encode(fileContent);
        
        # realizando o upload
        
        url = f"{self.api_base_url}/repos/{self.username}/{nomeRepo}/contents/{nomeArquivo}"
        data = {
            "message": "Adicionando um novo arquivo",
            "content": encodedContent.decode("utf-8")
            }
            
        
        response = requests.put(url, json=data, headers=self.headers);
        print(f'status_code do upload do arquivo: {response.status_code}');
        

        
        
        
        
        