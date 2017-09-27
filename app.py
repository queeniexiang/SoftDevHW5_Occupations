"""
Queenie Xiang and Kelly Wang 
SoftDev1 pd7
HW5 -- Jinja Tuning
2017-09-26
"""

import random
from flask import Flask, render_template
app = Flask(__name__)
import random_selector


#assign following fxn to run when root route requested 
@app.route("/")

#"Home" page the user sees 
def hello_world():
    retStr = ""
    retStr += "<center>Hello, nice to meet you! Click on the picture for some occupations information!<br>" 
    retStr += "<a href = /occupations>"
    retStr += "<img src = /static/quokka.jpg> </a> <br>  </center>"     
    return retStr


occupations={}
@app.route("/occupations")


def test_tmplt():
    #Grabs the dictionary of occupations from random_selector.py 
    occupations = random_selector.ret_occ()
    
    return render_template('occupations_template.html', occupations = occupations, Job = 'Job Class', Percentage = 'Percentage', rand_occ=random_selector.rand_selector())


if __name__ == "__main__":
    app.debug = True
    app.run()


