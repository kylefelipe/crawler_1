import requests
url = 'https://michaelis.uol.com.br/moderno-portugues/busca/'
solicitacao = 'batata/'
requisicao = requests.get(url+str(solicitacao)).text.strip()
print(requisicao)