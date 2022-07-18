import json 

labels = {0: 'other', 1: 'cloth', 3: 'none',
          4: 'respirator', 5: 'surgical', 6: 'valve'}

filename = '/home/bringascastle/Documentos/repos/RetinaNet/JSONfiles_G/TEST_objects_G.json'

with open(filename, "r") as file:
    datos = json.load(file)

map = {
        1 : 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
       0 : 0
    }

acum = 0
for obj in datos:
    acum += len(obj['labels'])
    for lbl in obj['labels']:
        pass
        map[lbl] += 1

print('Total de objetos: {}'.format(acum))
print(map)

