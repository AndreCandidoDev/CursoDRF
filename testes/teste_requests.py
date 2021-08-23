import requests

# GET avaliações
avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')
print(avaliacoes)

# status da requisição
print(avaliacoes.status_code)

# header da response
print(avaliacoes.headers)

# dados da respose
print(avaliacoes.text)
print(type(avaliacoes.text))   # <class 'str'>
print(avaliacoes.json())
print(type(avaliacoes.json()))  # <class 'dict'>

# quantidade de itens e resultados
print(avaliacoes.json()['count'])
print(avaliacoes.json()['results'])


# GET avaliação
avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/1/')
print("\n", avaliacao.json())


# GET cursos
headers = {'Authorization': 'Token 56703e2b34ee133537d7107f5421cdeb0699b515'}
cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/', headers=headers)
print(cursos.status_code)
print(cursos.json())

# POST avaliação
headers = {'Authorization': 'Token 56703e2b34ee133537d7107f5421cdeb0699b515'}
data = {"curso": 1, "nome": "testerequest", "email": "algosdsdsd@gmail.com", "avaliacao": 4}
req = requests.post(url='http://127.0.0.1:8000/api/v2/avaliacoes/', headers=headers, data=data)
print(req.status_code)
print(req.json())
