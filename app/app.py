from flask import Flask, request

app = Flask(__name__)

# Lista para armazenar os livros
backlog = []

# Rota para adicionar um novo livro
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    dados = request.get_json()
    titulo = dados.get('titulo')
    autor = dados.get('autor')
    status = dados.get('status')

    if not titulo or not autor or not status:
        return {'erro': 'Título, autor e status são obrigatórios.'}, 400

    livro = {
        'titulo': titulo,
        'autor': autor,
        'status': status
    }

    backlog.append(livro)
    return {'mensagem': 'Livro adicionado com sucesso!', 'livro': livro}, 201

# Rota para listar todos os livros
@app.route('/livros', methods=['GET'])
def listar_livros():
    return {'livros': backlog}

# Rota para filtrar livros por status
@app.route('/livros/status/<status>', methods=['GET'])
def filtrar_por_status(status):
    filtrados = [livro for livro in backlog if livro['status'] == status]
    return {'livros': filtrados}

if __name__ == '__main__':
    app.run(debug=True)

