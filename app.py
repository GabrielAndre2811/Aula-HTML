from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para a página de login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Aqui você pode adicionar lógica para verificar usuário/senha
    return f"Usuário: {username}, Senha: {password}"

# Rota para a página de contato
@app.route('/contato', methods=['POST'])
def contato():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Aqui você pode processar os dados, como enviar um e-mail ou armazenar no banco de dados
    return f"Nome: {name}, E-mail: {email}, Mensagem: {message}"

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
