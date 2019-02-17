from flask import Flask
import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
   return 'home page'

@app.route('/about')
def about():
   return 'about page'

if __name__ == '__main__':
	app.run(debug = True)