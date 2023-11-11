from manipulaRepos import ManipulaRepositorios

# instanciando um objeto:

novoRepo = ManipulaRepositorios('thelastbeto') #usuario da conta do github

# Criando um repositorio;

nomeRepo = 'Linguagens-Utilizadas-Empresas'
novoRepo.criaRepos(nomeRepo);

#Adicionando arquivos salvos no repositório criado;

novoRepo.addArquivo(nomeRepo, 'linguagens_amazon.csv', 'dados/linguagensAmzn.csv')#nome do repo pra fazer upload do arquivo, #nome do que queremos dar para o arquivo no rep do git, #caminho do arquivo na maquina
novoRepo.addArquivo(nomeRepo, 'linguagens_netflix.csv', 'dados/linguagensNetflix.csv')
novoRepo.addArquivo(nomeRepo, 'linguagens_netflix.csv', 'dados/linguagensSpotify.csv') 