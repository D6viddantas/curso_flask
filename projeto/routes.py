from projeto import app,db
from flask import Flask,render_template,request,redirect,url_for
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
    return render_template(
        'livros.html',
        livros=Livro.query.all()
    )

@app.route('/add_livro',methods=['GET','POST'])
def adicionar_livro():
    
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    valor = request.form.get('valor')
    if request.method == 'POST':
        livro_add = Livro(
            nome,
            descricao,
            valor,
        )
        db.session.add(livro_add)
        db.session.commit()
        return redirect(url_for('lista_livros'))
    return render_template(
        'novo_livro.html',

    )
@app.route('/<int:id>/atualizar_livro',methods=['GET','POST'])
def atualizar_livro(id):
    livro_bd = Livro.query.filter_by(id=id).first()
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        valor = request.form.get('valor')
        Livro.query.filter_by(id=id).update(
            {
                'nome':nome,
                'descricao':descricao,
                'valor':valor,
            }
        )
        db.session.commit()
        return redirect(url_for('lista_livros'))
    return render_template(
        'atualizar_livro.html',
        livro = livro_bd
        )