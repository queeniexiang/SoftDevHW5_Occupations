import random
from flask import Flask, render_template
app = Flask(__name__)
import random_selector


#assign following fxn to run when root route requested 
@app.route("/") 
def hello_world():
    retStr = ""
    retStr += "<center>Hello, nice to meet you! Click on the picture for a surprise!<br>" 
    retStr += "<a href = /occupations>"
    retStr += "<img src = /static/quokka.jpg> </a> <br>  </center>" 
    
    return retStr


occupations={}
@app.route("/occupations")



def test_tmplt():
    occupations = random_selector.ret_occ() 
    return render_template('occupations_template.html', occupations = occupations)


if __name__ == "__main__":
    app.debug = True
    app.run()
