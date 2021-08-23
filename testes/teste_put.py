import requests

headers = {'Authorization': 'Token f2a9a8356ad243de4666f7269e52805395772e94'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes'

curso_atualizado = {
    "titulo": "nova fruta",
    "url": "http://frutanova2.com"
}

# buscando curso
# curso = requests.get(url=f'{url_base_cursos}7/', headers=headers)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}3/', headers=headers, data=curso_atualizado)
# print(resultado.status_code)
# print(resultado.json())

# Testando o codigo de status http
assert resultado.status_code == 200

# Testando o titulo
assert resultado.json()['titulo'] == curso_atualizado['titulo']
