<h2>Configuração do Framework Flask</h2>

<p>Este tutorial tem como objetivo fornecer uma introdução à configuração do framework Flask, uma ferramenta para criação de aplicações web em Python.</p>

<h3>Pré-requisitos</h3>

<p>Antes de começar, é necessário ter o Python 3.x instalado em seu computador. Além disso, é recomendado que você tenha um ambiente virtual configurado para isolar as dependências do seu projeto.</p>

<h3>Instalação</h3>

<p>Para instalar o Flask, abra o seu terminal ou prompt de comando e digite o seguinte comando:</p>

<code>pip install Flask</code>

<p>Este comando instalará o Flask e suas dependências em seu ambiente virtual.</p>

<h3>Estrutura básica de um projeto Flask</h3>

<p>Um projeto Flask consiste em uma estrutura básica de diretórios e arquivos que devem ser organizados da seguinte forma:</p>

<pre>
meu_projeto/
    app.py
    templates/
        index.html
    static/
        style.css
</pre>

<p>O arquivo <code>app.py</code> é o arquivo principal da sua aplicação, onde você irá definir as rotas e a lógica de negócio da sua aplicação. O diretório <code>templates</code> contém os arquivos HTML que serão renderizados pela sua aplicação e o diretório <code>static</code> contém os arquivos estáticos, como arquivos CSS e JavaScript.</p>

<h3>Criando uma aplicação Flask</h3>

<p>Para criar uma aplicação Flask, abra o arquivo <code>app.py</code> e digite o seguinte código:</p>

<pre>
<code>
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Olá, mundo!"

if __name__ == "__main__":
    app.run(debug=True)
</code>
</pre>

<p>Este código cria uma aplicação Flask que retorna a mensagem "Olá, mundo!" quando a rota raiz (<code>/</code>) é acessada. Para executar a aplicação, digite o seguinte comando em seu terminal:</p>

<code>python app.py</code>

<p>Isso iniciará o servidor de desenvolvimento embutido do Flask e a aplicação estará acessível em <code>http://localhost:5000/</code>.</p>

<h3>Conclusão</h3>

<p>O Flask é um framework web leve e fácil de usar para desenvolvimento de aplicações web em Python.</p>
