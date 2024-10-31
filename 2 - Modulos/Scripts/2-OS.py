import os

# * 1 - Consultar funcionalidades do módulo OS
# help('os')

# * 2 - Retornar a pasta atual
print(os.getcwd())

# * 3 - Listar arquivos e pastas
print(os.listdir())

# * 4 - Apresentar a versão do sistema operacional
os.system('lsb_release -a') #! No windows: ver

# * 5 - Configurações da máquina
os.system('sudo dmidecode -t system') #! No windows: systeminfo

# * 6 - Limpar a tela
os.system('clear') #! No windows: cls

# * 7 - Ver o IP
os.system('hostname -I') #! No windows: ipconfig