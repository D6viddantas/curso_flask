from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def principal():
    conteudos = [
        'Manipulação de dados',
        'Herança e Template',
        'integração de API',
        'Banco de Dados']
    return render_template('index.html',
                        conteudos=conteudos
                           )

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')