from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)

bootstrap = Bootstrap5(app)
@app.route('/mytemplate')
def t_test():
    return render_template('template1.html', my_info=my_info)


@app.route('/bootstraptemplate')
def t_test1():
    return render_template('index.html', my_info=my_info)