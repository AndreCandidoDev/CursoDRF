import requests

headers = {'Authorization': 'Token 56703e2b34ee133537d7107f5421cdeb0699b515'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes'

resultado_cursos = requests.get(url=url_base_cursos, headers=headers)
# print(resultado_cursos.json())

# Testando se o endpoint esta correto
assert resultado_cursos.status_code == 200

# Testando a quantidade de registros
assert resultado_cursos.json()['count'] == 8

# Testando se o titulo do primeiro curso esta correto
assert resultado_cursos.json()['results'][0]['titulo'] == 'teste'
