#def ambiente_virtual():

    #1 - Definição do diretório e abertura do terminal:
 
    # Antes de iniciar o projeto, foi necessário criar o ambiente virtual. Para tal, é necessário abrir o terminal desejado.
    #No caso desse projeto, utilizei o terminal C:\Users\blank\Desktop\python - em que "python" é a pasta que criei no desktop para salvar 
    #o projeto do VsCode.
    #Depois de criado o diretório do projeto e selecionado esse caminho no terminal do Vs code, vamos a criação do ambiente virtual.

    #2 - Criação do ambiente virtual Python:

    #Para criar o ambiente virtual, utilizar no terminal, no caminho onde está salvo o arquivo os seguintes comandos:
    #Exemplo do projeto paralelo: PS C:\Users\blank\Desktop\pyhon2> pip install virtualenv
    #Isso vai instalar a opção de criar um ambiente virtual para o projeto.
    #Depois, para criar o ambiente em si, utilizar o comando no terminal: virtualenv <nome do ambiente virtual>
    #No caso coloquei: PS C:\Users\blank\Desktop\pyhon2> virtualenv ambiente2 --python=python3.9

    #3 - Ativação do ambiente virtual:

    #Para ativar, ou utilizar comandos específicos para a área de trabalho no ambiente virtual, utilizar o seguinte comando no Windows:
    #./ambiente2/Scripts/activate
    #Note que o caminho do terminal vai estar diferente depois de ativado: (ambiente2)C:\Users\blank\Desktop\pyhon2> 

    #4 - Instalação de bibliotecas essenciais para esse projeto Rest API:
    #(ambiente2)C:\Users\blank\Desktop\pyhon2> pip install Flask
    #" pip install Flask-Restful
    #" pip freeze  (você consegue ver todas as bibliotecas instaladas)

    #5 - Criação da primeira APi:
    #Antes de tudo, vamos criar um arquivo .py dentro da pasta de trabalho e importar as bibliotecas que foram baixadas.

#def find_hotel(hotel_id):
        #for hotel in hoteis:
        #    if hotel['hotel_id'] == hotel_id:
        #       return hotel
        #return None
#A função find hotel acima deixou de ser usada pois ela estava conectada com a lista de hoteis criada dentro do post.
#Como passamos a utilizar o banco de dados SQL, ela n faz mais sentido permanecer no código.

#Como importar os projetos para o GitHub:
#acessar - https://www.youtube.com/watch?v=peGUkhXD3Vw