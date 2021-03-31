from flask import Flask  

app = Flask(__name__)    

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'

if __name__ == '__main__':
    app.run(debug=True) 
