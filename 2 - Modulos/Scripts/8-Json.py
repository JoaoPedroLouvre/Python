import json

# 1 - Converter strings para dicionários
person = '{"name": "João Pedro", "languages":["Python", "Javascript"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languages'])

# 2 - Convertendo dicionário para json
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))
print(type(person_dict))

# 3 - Formatando um json
print(json.dumps(person_dict, indent=4, sort_keys=True))

# 4 - Salvando json em txt
with open("person.txt", "w") as json_file:
    json.dump(person_dict, json_file)

# 5 - Lendo um json externo
with open("iris.json", "r") as f:   # iris.json seria o nome do arquivo json que deseja ler
    data = json.load(f)
    print(data)