Configuração do Framework Flask
Este tutorial tem como objetivo fornecer uma introdução à configuração do framework Flask, uma ferramenta para criação de aplicações web em Python.

Pré-requisitos
Antes de começar, é necessário ter o Python 3.x instalado em seu computador. Além disso, é recomendado que você tenha um ambiente virtual configurado para isolar as dependências do seu projeto.

Instalação
Para instalar o Flask, abra o seu terminal ou prompt de comando e digite o seguinte comando:
pip install Flask

Estrutura básica de um projeto Flask
Um projeto Flask consiste em uma estrutura básica de diretórios e arquivos que devem ser organizados da seguinte forma:
meu_projeto/
    app.py
    templates/
        index.html
    static/
        style.css

O arquivo app.py é o arquivo principal da sua aplicação, onde você irá definir as rotas e a lógica de negócio da sua aplicação. O diretório templates contém os arquivos HTML que serão renderizados pela sua aplicação e o diretório static contém os arquivos estáticos, como arquivos CSS e JavaScript.

Criando uma aplicação Flask
Para criar uma aplicação Flask, abra o arquivo app.py e digite o seguinte código:
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Olá, mundo!"

if __name__ == "__main__":
    app.run(debug=True)

Este código cria uma aplicação Flask que retorna a mensagem "Olá, mundo!" quando a rota raiz (/) é acessada. Para executar a aplicação, digite o seguinte comando em seu terminal:
python app.py

Isso iniciará o servidor de desenvolvimento embutido do Flask e a aplicação estará acessível em http://localhost:5000/.

Conclusão
O Flask é um framework web leve e fácil de usar para desenvolvimento de aplicações web em Python.
