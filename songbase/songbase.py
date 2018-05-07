from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/form-basics')
def formbasics ():
    return render_template('form-basics.html')


@app.route('/users/<string:username>')
def users(username):
    return render_template('user.html',uname=username)

@app.route('/user')
def user():
    return "this is the page for users"



if __name__ == '__main__':
    app.run()
