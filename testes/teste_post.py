import requests

headers = {'Authorization': 'Token 56703e2b34ee133537d7107f5421cdeb0699b515'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes'

novo_curso = {
    "titulo": "frutas",
    "url": "http://frutas.com"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o código de status http
assert resultado.status_code == 201

# Testando se o titulo do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']
