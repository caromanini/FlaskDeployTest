from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Holi me llamo Chiara!'
 
 
if __name__ == "__main__":
    app.run()