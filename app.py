from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def principal():
    conteudos = [
        'Manipulação de dados',
        'Herança e Template',
        'integração de API',
        'Banco de Dados',
        'Deploy App']
    return render_template('index.html',
                        conteudos=conteudos
                           )

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/diario')
def diario():
    diario = {
        'Maria':8.5,
        'Joao':10.0,
        'enzo':6.8,
        'enzo miguelito':3,
        'giumar':1.1,
    }
    return render_template(
        'diario.html',
        diario=diario)