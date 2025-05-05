from flask import Flask,render_template,request

app = Flask(__name__)
conteudos = []

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