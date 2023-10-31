from flask import Flask, render_template

app = Flask(__name__)


@app.route('/login')
def index():
  return render_template('auth/login.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
