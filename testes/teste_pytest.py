import requests


class TestCurso:
    headers = {'Authorization': 'Token f2a9a8356ad243de4666f7269e52805395772e94'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)
        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}5/', headers=self.headers)
        assert curso.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "testepytest",
            "url": "http://testepyteste.com"
        }
        resultado= requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)
        assert resultado.status_code == 201
        assert resultado.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizar = {
            "titulo": "novocursoteste",
            "url": "http://novocurso.com"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}5/', headers=self.headers, data=atualizar)
        assert resposta.status_code == 200
        # assert resposta.json()['titulo'] == atualizar['titulo']

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "novocursoteste2",
            "url": "http://novocursoteste2.com"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}5/', headers=self.headers, data=atualizado)
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}4/', headers=self.headers)
        assert resposta.status_code == 204 and len(resposta.text) == 0
