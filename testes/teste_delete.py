import requests

headers = {'Authorization': 'Token f2a9a8356ad243de4666f7269e52805395772e94'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes'

resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

# Testando codigo http
assert resultado.status_code == 204

# Testando se o tamanho do conteudo retornado é zero
assert len(resultado.text) == 0
