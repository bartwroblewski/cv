from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/echo')
def echo():
    return 'hi'
    
if __name__ == '__main__':
    app.run(host="0.0.0.0")
