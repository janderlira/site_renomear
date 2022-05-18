from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
import os

class PhotoForm(FlaskForm):
    qt_img = IntegerField('Quantidade De Fotos')
    destino = StringField('Destino Da Imagem')
    codigo = StringField('Codigo')
    photo1 = FileField([FileRequired()])
    photo2 = FileField([FileRequired()])
    photo3 = FileField([FileRequired()])
    photo4 = FileField([FileRequired()])
    photo5 = FileField([FileRequired()])
    photo6 = FileField([FileRequired()])
    photo7 = FileField([FileRequired()])
    photo8 = FileField([FileRequired()])
    photo9 = FileField([FileRequired()])
    photo10 = FileField([FileRequired()])
    photo11 = FileField([FileRequired()])
    photo12 = FileField([FileRequired()])
    photo13 = FileField([FileRequired()])
    photo14 = FileField([FileRequired()])



app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/rename', methods=['GET', 'POST'])
def raname():
    form = PhotoForm()

    if form.validate_on_submit():
        f1 = form.photo1.data
        f2 = form.photo2.data
        f3 = form.photo3.data
        f4 = form.photo4.data
        f5 = form.photo5.data
        f6 = form.photo6.data
        f7 = form.photo7.data
        f8 = form.photo8.data
        f9 = form.photo9.data
        f10 = form.photo10.data
        f11 = form.photo11.data
        f12 = form.photo12.data
        f13 = form.photo13.data
        f14 = form.photo14.data
        destino = form.destino.data
        codigo = form.codigo.data

        qt = form.qt_img.data

        f1.save(os.path.join(app.instance_path, destino, codigo + "_01_Foto do modem.png"))
        f2.save(os.path.join(app.instance_path, destino, codigo + "_02_PC com Internet.png"))
        f3.save(os.path.join(app.instance_path, destino, codigo + "_03_Parte de FRENTE da antena com logo.png"))
        f4.save(os.path.join(app.instance_path, destino, codigo + "_04_Parte de TRÁS da antena exibindo Parafusos.png"))
        f5.save(os.path.join(app.instance_path, destino, codigo + "_05_Haste de Aterramento.png"))
        f6.save(os.path.join(app.instance_path, destino, codigo + "_06_Bloco de aterramento.png"))
        f7.save(os.path.join(app.instance_path, destino, codigo + "_07_Isolamento da ETRIA.png"))
        f8.save(os.path.join(app.instance_path, destino, codigo + "_08_Serial da ETRIA.png"))
        f9.save(os.path.join(app.instance_path, destino, codigo + "_09_Serial do Modem.png"))
        f10.save(os.path.join(app.instance_path, destino, codigo + "_10_Entrada do cabo no prédio J pingadeira.png"))
        f11.save(os.path.join(app.instance_path, destino, codigo + "_11_Facha do prédio.png"))
        f12.save(os.path.join(app.instance_path, destino, codigo + "_12_TIPP.png"))
        f13.save(os.path.join(app.instance_path, destino, codigo + "_13_Visada da ETRIA.png"))
        f14.save(os.path.join(app.instance_path, destino, codigo + "_14_eSVT.png"))



        return render_template('index.html')
    return render_template('rename.html', form=form)

if __name__ == __name__:
    app.run(host='0.0.0.0', debug=True)

    # servidor do heroku


'''
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = PhotoForm()

    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, '/home/will/PycharmProjects/Renomeia-IMG', filename
        ))
        print(filename)
        print(os.path.join(app.instance_path))
        return "<h1>Parabens Deu Tudo Certo!</h1>"

    return render_template('index.html', form=form)
'''