from flask import Flask,render_template,request
from list_filmes import dados_json
app = Flask(__name__)
conteudos = []

registros = {'teste:':123}

@app.route('/',methods=['GET','POST'])
def principal():
    if request.method == 'POST':
        if request.form.get('conteudo'):
            conteudos.append(request.form.get('conteudo'))
    return render_template('index.html',
                        conteudos=conteudos
                           )

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/diario',methods=['GET','POST'])
def diario():
    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get('nota'):
            registros[request.form.get('aluno')] =request.form.get('nota')
    return render_template(
        'diario.html',
        registros=registros)

@app.route('/filmes')
def listar_filmes():
    return render_template('filmes.html',filmes=dados_json)