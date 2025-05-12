from projeto import app
from flask import Flask,render_template,request
from projeto.models import Livro
from projeto.list_filmes import list_filmes

conteudos = []
registros = {}

@app.route('/',methods=['GET','POST'])
def principal():
    if request.method == 'POST':
        if request.form.get('conteudo'):
            conteudos.append(request.form.get('conteudo'))
    return render_template('index.html',
                        conteudos=conteudos,
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

@app.route('/filmes/<propriedade>')
def listar_filmes(propriedade):
    return render_template('filmes.html',filmes=list_filmes(propriedade))

@app.route('/livros')
def lista_livros():
    livros = Livro.query.all()
    print(f'livros:{livros}')
    return render_template(
        'livros.html',
        livros=Livro.query.all()
    )