from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>DevOps Web Project</h1><p>Aplicação rodando com sucesso na EC2!</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
