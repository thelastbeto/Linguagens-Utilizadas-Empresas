from repositorios import DadosRepositorios; 

amazonRep = DadosRepositorios('amzn')
linguagensUsadasAmazon = amazonRep.criaDfLinguagens();

netflixRep = DadosRepositorios('netflix')
linguagensUsadasNetflix = netflixRep.criaDfLinguagens();

spotifyRep = DadosRepositorios('spotify')
linguagensUsadasSpotify = spotifyRep.criaDfLinguagens();

# Salvando os dados

linguagensUsadasAmazon.to_csv('dados/linguagensAmzn.csv')
linguagensUsadasNetflix.to_csv('dados/linguagensNetflix.csv')
linguagensUsadasSpotify.to_csv('dados/linguagensSpotify.csv')