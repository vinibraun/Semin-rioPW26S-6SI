from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/pessoas', methods=['GET', 'POST'])
def pessoas():
    conn = sqlite3.connect('pessoas.db') #Conecta com o banco
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM pessoas") #quando o método for GET, ele retorna todas as pessoas cadastradas no banco
        pessoas = cursor.fetchall()
        return jsonify(pessoas)

    if request.method == 'POST':
        nome = request.json['nome']
        idade = request.json['idade']
        email = request.json['email'] #quando o método for post, ele pegas as informações dadas com o JSON e cadastra no banco com o INSERT

        cursor.execute("INSERT INTO pessoas (nome, idade, email) VALUES (?, ?, ?)", (nome, idade, email))
        conn.commit()

        return jsonify({'mensagem': 'Pessoa criada com sucesso!'})


@app.route('/pessoas/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def pessoa(id):
    conn = sqlite3.connect('pessoas.db')
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM pessoas WHERE id=?", (id,)) #quando chamar um GET com uma rota de um id em específico, ele dá um select naquele id
        pessoa = cursor.fetchone()
        return jsonify(pessoa)

    if request.method == 'PUT':
        nome = request.json['nome']
        idade = request.json['idade']
        email = request.json['email']

        cursor.execute("UPDATE pessoas SET nome=?, idade=?, email=? WHERE id=?", (nome, idade, email, id)) #quando for PUT, ele pega as informações do JSON e dá um UPDATE no banco
        conn.commit()

        return jsonify({'mensagem': 'Pessoa atualizada com sucesso!'})

    if request.method == 'DELETE':
        cursor.execute("DELETE FROM pessoas WHERE id=?", (id,)) #quando for o método DELETE, ele deleta a pessoa do ID especificado
        conn.commit()

        return jsonify({'mensagem': 'Pessoa excluída com sucesso!'})


if __name__ == '__main__':
    app.run(debug=True) #Flask em modo de depuração
