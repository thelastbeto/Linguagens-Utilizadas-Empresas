import requests
import pandas as pd

class DadosRepositorios:

        def __init__(self, owner):
                self.owner = owner # User do github para que se possa enviar o conteúdo ao meu repositório;
                self.api_base_url = 'https://api.github.com'  # API BASE;
                self.access_token ='your_token' # Token acess
                self.headers = {'Authorization': 'Bearer' + self.access_token,
                    'X-GitHub-Api-Version': '2022-11-28'}
                
        def listaRepositorios(self):
            reposList = []
            
            for pageNum in range(1, 30):
                try:
                    url = f'{self.api_base_url}/users/{self.owner}/repos?page={pageNum}'
                    response = requests.get(url, headers = self.headers);
                    reposList.append(response.json())
                except:
                    reposList.append(None);
                    
                return reposList;
            
        def nomesRepos(self, reposList):
            repoNames=[]
            for page in reposList:
                for repo in page:
                    try:
                        repoNames.append(repo['name'])
                    except:
                        pass
                    
            return repoNames;
        
        def nomesLinguagens(self, reposList):
            repoLanguages=[]
            for page in reposList:
                for lang in page:
                    try:
                        repoLanguages.append(lang['language'])
                    except:
                        pass
                    
            return repoLanguages;
        
        def criaDfLinguagens(self):
            repositorios = self.listaRepositorios();
            nomes = self.nomesRepos(repositorios);
            linguagens = self.nomesLinguagens(repositorios);
            
            dados = pd.DataFrame();
            dados['repositoryName'] = nomes;
            dados['language'] = linguagens
            
            return dados;
                    