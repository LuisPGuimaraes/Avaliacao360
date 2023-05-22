from flask import Flask
from routes.avaliacao import bp as avaliacao
from routes.criacoes import bp as criacoes
from routes.devolutivas import bp as devolutivas
from routes.padroes import bp as padroes
from routes.updates import bp as updates
from utils.darkmode import bp as darkmode

app = Flask(__name__)

app.register_blueprint(avaliacao)
app.register_blueprint(criacoes)
app.register_blueprint(devolutivas)
app.register_blueprint(padroes)
app.register_blueprint(updates)
app.register_blueprint(darkmode)


app.secret_key = 'wxyz@mtwjer123123%213'

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
