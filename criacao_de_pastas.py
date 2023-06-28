import os
  
root_path = 'C:\\Users\\lucas\\Desktop\\testes_vscode'


num_inicio = 30
num_final = 139

list = []

while num_inicio <= num_final:
    list.append(f'NOT{num_inicio}')
    num_inicio += 1

  
for items in list:
    path = os.path.join(root_path, items)
    os.mkdir(path)