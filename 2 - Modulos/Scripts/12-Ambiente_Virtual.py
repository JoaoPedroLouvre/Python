'''
A importância de criar um ambiente virtual de desenvolvimento é isolar o nosso projeto. De uma forma que
não aumentemos exponencialmente o tamanho da aplicação, pois, criando um ambiente virtual nós estamos iso-
lando aquele projeto. No meu computador tenho instalado a biblioteca opencv. Mas não quero que ela pese
o meu sistema em uma possível exportação do meu projeto de calculadora, sendo assim, crio um ambiente vir-
tual para baixar as bibliotecas da minha calculadora, não comprometendo o sistema ou o projeto.


Para criarmos este ambiente de desenvolvimento virtual rodamos:

        ****python -m venv .nome da virtualização****

Assim, podemos notar que o python criou uma pasta com o nome da nossa virtualização, mas ela ainda não es-
tá ativada! Para fazer isso, precisamos rodar:

        ****cd 'caminho para o arquivo activate'****
        ****chmod +x ./activate****
        ****source ./activate****

Agora o ambiente virtual está realmente habilitado! Basta voltar para a pasta padrão do projeto e instalar
as dependências necessárias.


Para rodarmos uma biblioteca que temos em uma ambiente de desenvolvimento no de produção. Para isso roda-
mos: 

        ****pip freeze****

Este comando irá nos dar cada biblioteca com sua versão específica. Para exportar isso para alguém rodamos:

        ****pip freeze -1 > requirements.txt****

Para instalar essas bibliotecas de uma vez podemos rodar um único comando com: 

        ****pip install -r requirements.txt****
'''