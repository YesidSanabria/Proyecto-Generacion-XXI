from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola Generacion XXI"
if __name__ == '__main__':
    app.run(debug=True)

# Adaptación de bases de datos al Back-Endgit 
# auxiliooooo