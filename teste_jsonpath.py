import requests
import jsonpath


avalaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')
resultados = jsonpath.jsonpath(avalaliacoes.json(), 'results')
print(resultados)

primeiro = jsonpath.jsonpath(avalaliacoes.json(), 'results[0]')
print(primeiro)

nome = jsonpath.jsonpath(avalaliacoes.json(), 'results[0].nome')
print(nome)

nota = jsonpath.jsonpath(avalaliacoes.json(), 'results[0].avaliacao')
print(nota)

curso_id = jsonpath.jsonpath(avalaliacoes.json(), 'results[0].id')
print(curso_id)

# todos os nomes das pessoas que avaliaram
nomes = jsonpath.jsonpath(avalaliacoes.json(), 'results[*].nome')
print(nomes)

# todas as notas
notas = jsonpath.jsonpath(avalaliacoes.json(), 'results[*].avaliacao')
print(notas)
