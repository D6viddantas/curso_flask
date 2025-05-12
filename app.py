from flask import Flask,render_template,request
from list_filmes import list_filmes
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.sqlite3'

db = SQLAlchemy()
db.init_app(app)


class Livro(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    valor = db.Column(db.Integer)

    def __init__(self,nome,descricao,valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
with app.app_context():
    db.create_all()

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