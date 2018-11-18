from flask import Flask, render_template
import connexion

# app = Flask(__name__)
app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')

@app.route('/')
def hello_world():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
