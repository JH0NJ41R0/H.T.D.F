from flask import Flask
from flask import render_template

app = Flask(__name__)

#ruteo
@app.route('/')
def index():
    return ('empleados/index.html')

if __name__ == '__main__':
    app.run(debug=True)