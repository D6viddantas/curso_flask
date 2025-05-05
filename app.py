from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def principal():
    conteudo1 = 'Manipulação de dados'
    conteudo2 = 'Herança e Template'
    conteudo3 = 'integração de API'
    conteudo4 = 'Banco de Dados'
    return render_template('index.html',
                           conteudo1=conteudo1,
                           conteudo2=conteudo2,
                           conteudo3=conteudo3,
                           conteudo4=conteudo4,
                           )

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')